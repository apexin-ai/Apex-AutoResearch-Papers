# eval check eval progress

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_check-eval-progress_20260516T173845_result.json`
- **Structured JSON:** [`0f5fe616ab526bc43523.json`](../../sessions/0f/0f5fe616ab526bc43523.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

两个 eval 进程**均在运行中**（日志持续更新至 01:39，即当前时刻）。

### τ=0.2 (`gated_warmstart_v3_s43_r2`) — GPU 1

| 指标 | 值 |
|------|-----|
| 进度 | **24/100**（23 完成 + 1 进行中） |
| 已证明 | 1/23 (4.3%) |
| 失败 | 22/23 |
| 平均 gen 时间 | ~34s/sample |
| 已运行 | ~13 min（01:26 开始） |
| **预估剩余** | **~44 min** |

### τ=0.15 (`gated_warmstart_v3_t015_s43`) — GPU 0

| 指标 | 值 |
|------|-----|
| 进度 | **16/100**（15 完成 + 1 进行中） |
| 已证明 | 4/15 (26.7%) |
| 失败 | 11/15 |
| 平均 gen 时间 | ~88s/sample |
| 已运行 | ~22 min（01:17 开始） |
| **预估剩余** | **~125 min (~2h)** |

### GPU 使用

| GPU | 利用率 | 显存 |
|-----|--------|------|
| 0 | 4% | 15.3 / 97.9 GB |
| 1 | 24% | 16.5 / 97.9 GB |

### 备注

- τ=0.15 生成明显更慢（88s vs 34s），可能因为更严格的 gating 使模型产生更长的 trace
- τ=0.2 当前 prove rate 很低 (4.3%)，远低于 τ=0.15 (26.7%)——但仅 23 个 sample，后续可能上升
- 两个 eval 都没有 classify_h7 进程运行，classify_h7 可能是 eval 完成后才执行

---
