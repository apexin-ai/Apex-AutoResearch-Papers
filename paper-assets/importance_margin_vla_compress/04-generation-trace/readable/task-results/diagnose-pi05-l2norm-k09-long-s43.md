# diagnose pi05 l2norm k09 long s43

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_pi05_l2norm_k09_long_s43_20260525T124055_result.json`
- **Structured JSON:** [`2a467d5e03a9afb524a6.json`](../../sessions/2a/2a467d5e03a9afb524a6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

**实验已正常完成**，不是崩溃。cron 监控未检测到是因为没有写 sentinel 文件，且日志文件名不含 `postfix` 后缀（registry 注册名和实际日志名不匹配）。

### 结果

**π0.5 L2norm k=0.9 Long seed43 — overall SR = 80.8%** (404/500, 194.3 min)

Per-task:

| Task | SR |
|------|-----|
| T0: put alphabet soup & tomato sauce in basket | 92% |
| T1: put cream cheese & butter in basket | 96% |
| T2: turn on stove, put moka pot | 92% |
| T3: put black bowl in drawer & close | 100% |
| T4: white mug left plate, yellow mug right plate | 88% |
| T5: pick up book, place in caddy | 96% |
| T6: white mug on plate, chocolate pudding right | 14% |
| T7: put alphabet soup & cream cheese in basket | 82% |
| T8: put both moka pots on stove | 58% |
| T9: yellow/white mug in microwave & close | 90% |

结果 JSON 路径：`/root/autodl-tmp/importance_margin_vla_compress/eval_results/pi05_l2norm_k0.90_libero_10_seed43.json`

### GPU 状态

- **GPU 0：空闲**（1MiB / 24564MiB, 0% util）— 可立即重新部署
- GPU 1-3：被其他 python 进程占用

### 问题原因

监控未检测到结果的原因：
1. **无 sentinel 文件** — 评估脚本完成后没有写 `.sentinel`
2. **日志名不匹配** — registry 注册为 `eval_pi05_l2norm_k09_long_seed43_postfix`，实际日志名为 `eval_pi05_l2norm_k09_long_seed43.log`（无 `_postfix` 后缀）

---
