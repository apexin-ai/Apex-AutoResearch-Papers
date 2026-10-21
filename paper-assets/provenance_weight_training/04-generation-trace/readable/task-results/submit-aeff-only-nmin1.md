# submit aeff only nmin1

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_submit_aeff_only_nmin1_20260523T134218_result.json`
- **Structured JSON:** [`ab2b0b225aae2805e860.json`](../../sessions/ab/ab2b0b225aae2805e860.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 块 GPU 全部有负载，确认正常。

### 汇总

| 项目 | 状态 |
|------|------|
| **磁盘** | /root/autodl-tmp 68GB 可用 |
| **aeff_only_nmin1_seed42** | PID 875527, cuda:1, 28.7GB 显存占用 |
| **aeff_only_nmin1_seed123** | PID 875597, cuda:3, 28.7GB 显存占用, GPU util 100% |
| **GPU 0** (既有实验) | 100% util, 92GB 占用 — 正常运行 |
| **GPU 2** (既有实验) | 100% util, 92GB 占用 — 正常运行 |

GPU 1 的 utilization 暂时 0% 是因为刚启动在加载模型/数据，很快会上来。4 块卡全部在用。

---
