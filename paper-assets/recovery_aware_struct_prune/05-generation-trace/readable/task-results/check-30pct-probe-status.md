# check 30pct probe status

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_30pct_probe_status_20260520T050717_result.json`
- **Structured JSON:** [`4365f5c43dcd431b0ff1.json`](../../sessions/43/4365f5c43dcd431b0ff1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇报

### 原始进程 (PID 191446/191519)
**已被 Terminated**。两个都在 43/1319 (~3.3%) 处被杀掉，大约在 12:44。

### Retry 进程（正在运行）
已经有人在 12:53 重启了两个 eval：

| 方法 | PID | GPU | 进度 | 速度 |
|------|-----|-----|------|------|
| CKA-only 30% | 201928 | cuda:0 (85%, 11.5GB) | ~16/1319 | ~48s/sample |
| Standard 30% | 202006 | cuda:1 (85%, 11.6GB) | ~16/1319 | ~48s/sample |

### 预估完成时间
1319 × 48s ≈ **17.6 小时**。已跑 ~15 分钟，剩余约 **17.3 小时**。

**ETA: 明天 (5/21) ~06:00-06:30**。

### 与 20% 的对比（待结果出来）
- 20% post-prune: CKA-only ~31%, Standard ~1%, RASP ~31%
- 30% post-prune: 预计 accuracy 会进一步下降

目前无需操作，等明天早上结果出来后再更新 registry。

---
