# deploy fill 3 free gpus s45 extension

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_fill-3-free-gpus-s45-extension_20260523T223615_result.json`
- **Structured JSON:** [`068c3adcf6ba72bd61cc.json`](../../sessions/06/068c3adcf6ba72bd61cc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

部署完成，总结：

| 实验 | 服务器 | GPU | 状态 |
|------|--------|-----|------|
| `eval-supp-reconvla-obj-s45` (Object Reconvla s45) | bjb1-32546 | cuda:5 | RUNNING ✅ |
| `eval-supp-obj-k2mean-s45` (Object K2mean s45) | cqa1-32758 | cuda:2 | RUNNING ✅ |
| Goal K2mean s46 | bjb2-40593 | cuda:0 | **跳过** — 磁盘仅 5.7GB 可用 ❌ |

两个实验日志已确认参数正确（n_rollouts=20, n_action_steps=10, max_steps=280），模型正在加载中。

---
