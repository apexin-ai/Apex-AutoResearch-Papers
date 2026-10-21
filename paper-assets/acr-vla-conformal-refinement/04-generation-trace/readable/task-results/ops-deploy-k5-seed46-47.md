# ops deploy k5 seed46 47

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_deploy-k5-seed46-47_20260519T032508_result.json`
- **Structured JSON:** [`f903998fa9625990a7ae.json`](../../sessions/f9/f903998fa9625990a7ae.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验都已成功启动并进入 rollout 阶段。

部署报告：

| 实验 | 服务器 | GPU | 状态 |
|------|--------|-----|------|
| `eval-obs-only-object-norm02-k5-seed46` | bjb1-18228 | cuda:3（与 2 个 K=10 eval 共享） | RUNNING |
| `eval-obs-only-object-norm02-k5-seed47` | bjb1-18228 | cuda:0（与 2 个 K=10 eval 共享） | RUNNING |

**补充说明：**
- 三台服务器所有 GPU 都有负载，但 GPU 0/3 各有 ~17GB 空闲显存，eval 仅需 ~3.5GB，可安全共享
- 修复了 evaluate.py 第 404 行的 SyntaxError（f-string 内转义引号问题，可能由其他 agent 引入）
- K=5 + GPU 共享，预估每个实验需 6-8h（因共享可能稍慢于正常 4-6h），预计约 UTC 09:30-11:30 完成

---
