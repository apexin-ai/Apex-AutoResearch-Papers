# deploy pi05 crm ao bjb1 18228

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_pi05-crm-ao-bjb1-18228_20260528T030655_result.json`
- **Structured JSON:** [`c7865eb9314704cda045.json`](../../sessions/c7/c7865eb9314704cda045.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个实验全部正常启动，正在加载 Pi05 模型。

## 部署汇总

| 实验 | GPU | PID | 状态 |
|------|-----|-----|------|
| `pi05-crm-always-on-long-s43` | cuda:0 | 982384 | 加载模型中 |
| `pi05-crm-always-on-spatial-s43` | cuda:1 | 982668 | 加载模型中 |
| `pi05-crm-always-on-long-s44` | cuda:2 | 983101 | 加载模型中 |
| `pi05-crm-always-on-spatial-s44` | cuda:3 | 983391 | 加载模型中 |

服务器 bjb1-18228，4 个 GPU 全部占满。Long suite max_steps=520，Spatial suite max_steps=280。

---
