# eval bjb2 setup object eval

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_bjb2-setup-object-eval_20260515T014457_result.json`
- **Structured JSON:** [`1af5feb27b1728f77bdd.json`](../../sessions/1a/1af5feb27b1728f77bdd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**已在 bjb2-40593 上成功启动 `eval-reconvla-object`：**

| 项目 | 值 |
|------|-----|
| 实验 | ReconVLA baseline (argmin K=10) on LIBERO object |
| 服务器 | bjb2-40593, cuda:0 (RTX 4090 D) |
| Python PID | 211962 |
| GPU 占用 | ~5 GB |
| 规模 | 10 tasks × 20 rollouts = 200 episodes |
| 日志 | `/root/runs/acr-vla-conformal-refinement/eval-reconvla-object.log` |
| 输出 | `/root/autodl-tmp/eval_results/reconvla_object_K10.json` |
| 预计时长 | ~10-12h |

**跳过的步骤：**
- Git 修复：两台服务器都无 .git，但 bjb2 代码比 bjb1 更新，直接可用
- CRM checkpoint：reconvla 模式不需要
- v5 cache：reconvla 模式不需要

**此实验的价值：** 为 object benchmark 提供 reconvla argmin baseline，后续可与 VLA mean 和 CRM 变体对比。对应 spatial 上已在跑的 `eval-argmin-only-spatial`。

---
