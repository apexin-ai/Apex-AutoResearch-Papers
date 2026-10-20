# infra confirm launch

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_confirm-launch_20260514T075157_result.json`
- **Structured JSON:** [`62b0ed9b59a57be8af81.json`](../../sessions/62/62b0ed9b59a57be8af81.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

MVP 全量实验已成功启动，汇总如下：

| 检查项 | 结果 |
|--------|------|
| **PID 13678** (rep42, cuda:0) | 存活，状态 `Ss+`，已运行 ~40s |
| **PID 13758** (rep43, cuda:1) | 存活，状态 `Ss+`，已运行 ~38s |
| **GPU 0** | 6527 / 97887 MiB，利用率 62% |
| **GPU 1** | 6527 / 97887 MiB，利用率 70% |
| **rep42 日志** | 模型 `pythia-410m` 已加载，数据已加载，进入 Generation 0 (baseline) 评估阶段 |
| **rep43 日志** | 同上，Generation 0 baseline 评估中 |
| **tmux** | `tmux list-sessions` 被 read-only 模式拦截，跳过 |

两个实验刚启动约 40 秒，当前处于 Generation 0 baseline 评估（生成阶段的 padding 警告属正常现象）。训练 step 循环尚未开始，符合预期。

---
