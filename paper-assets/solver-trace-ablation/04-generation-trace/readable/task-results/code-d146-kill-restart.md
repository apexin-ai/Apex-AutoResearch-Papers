# code d146 kill restart

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d146-kill-restart_20260519T150245_result.json`
- **Structured JSON:** [`5a847b7c3b73eaf68267.json`](../../sessions/5a/5a847b7c3b73eaf68267.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

### 报告

| 项目 | 状态 |
|------|------|
| 旧进程 kill | 成功，GPU 完全释放（0 MiB） |
| Config 确认 | `per_device_batch_size: 2`, `gradient_accumulation_steps: 4` ✓ |
| 新 pipeline session | `d146-pipeline`, PID 441009 |
| GPU 显存 | **82,215 MiB / 97,887 MiB (84%)** — 在安全范围内（< 90 GiB） |
| 训练进度 | step 1-2 正常运行，~15.4s/step，reward=0.0（初始阶段正常） |

GPU 占用 82 GiB，相比旧配置（batch_size=4 时 step 4 已 95.7 GiB）显著下降，config 修复已生效。

---
