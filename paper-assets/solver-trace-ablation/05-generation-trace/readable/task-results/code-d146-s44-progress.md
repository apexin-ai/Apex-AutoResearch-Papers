# code d146 s44 progress

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d146-s44-progress_20260519T192746_result.json`
- **Structured JSON:** [`888735dde5cf48dbcd13.json`](../../sessions/88/888735dde5cf48dbcd13.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## D146 exec-s44 进度报告

| 指标 | 值 |
|------|-----|
| **当前 step** | 367 / 1000（36.7%） |
| **GPU 显存** | 84,759 MiB，利用率 100% |
| **parse_rate** | 1.0（稳定） |

### 最近 20 步趋势（step 348–367）

| 指标 | 范围 | 备注 |
|------|------|------|
| **prove_rate** | 0.5–1.0 | 多数步 1.0，偶尔掉到 0.5（step 355/358/360/361/365） |
| **ISR** | 0.0–0.127 | 极低，均值约 0.04；step 367 出现一个 0.127 的跳跃 |
| **loss** | 基本 0.0 | 仅 step 350 (0.0075) 和 352 (-0.0485) 有非零值 |

训练正常推进，~15s/step，预计还需约 2.6 小时完成。prove_rate 已饱和接近 1.0，ISR 极低符合 exec-only 预期（C006：冗余编码而非无推理）。

---
