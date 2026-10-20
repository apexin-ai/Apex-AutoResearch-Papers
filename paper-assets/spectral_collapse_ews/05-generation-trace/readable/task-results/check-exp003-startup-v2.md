# check exp003 startup v2

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_exp003_startup_v2_20260517T040830_result.json`
- **Structured JSON:** [`a5b8a92ed318632776c3.json`](../../sessions/a5/a5b8a92ed318632776c3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 验证结果

| 检查项 | 状态 |
|--------|------|
| PID 78069 存活 | ✓ 进程在运行 |
| 模型从本地缓存加载 | ✓ 无网络错误，成功加载 |
| Gen 0 训练开始 | ✓ 正在计算 Gen 0 指标（effective rank / perplexity / distinct-4） |
| cuda:1 显存占用 | ✓ PID 78074 占用 19034MiB |

**exp_003 已成功启动。** 模型从本地缓存加载成功（HF_HUB_OFFLINE=1 生效），当前正在执行 Generation 0 的 baseline 评估阶段。日志中有两个 padding 警告但不影响运行。

---
