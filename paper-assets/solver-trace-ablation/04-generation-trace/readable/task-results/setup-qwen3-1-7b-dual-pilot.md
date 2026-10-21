# setup qwen3 1 7b dual pilot

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_setup_qwen3-1_7b-dual-pilot_20260516T105518_result.json`
- **Structured JSON:** [`195c37bfa0dbd99a56a4.json`](../../sessions/19/195c37bfa0dbd99a56a4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

双卡训练成功启动。

**汇报：**

| 项目 | 值 |
|------|------|
| 模型 | `Qwen/Qwen3-1.7B` (ModelScope 下载) |
| 下载路径 | `/root/autodl-tmp/models/Qwen3-1.7B` |
| GPU 0 (exec-only) | 34511 MiB / 97887 MiB, 83% util, step 1 完成 (5.00 s/it) |
| GPU 1 (ISR β=0.1) | 34511 MiB / 97887 MiB, 76% util, step 1 完成 (5.17 s/it) |
| step 1 指标 | exec: prove_rate=0.625, isr=0.416; ISR: prove_rate=0.625, isr=0.416, beta=0.1 |
| 预计完成 | ~42 分钟 (500 steps × 5s/step) |
| 修复 | config 需要显式 `optim: adamw_torch`（argparse default=None 时 getattr 不回退） |

---
