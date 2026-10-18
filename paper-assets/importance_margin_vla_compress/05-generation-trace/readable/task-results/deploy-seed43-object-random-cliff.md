# deploy seed43 object random cliff

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_seed43_object_random_cliff_20260523T015443_result.json`
- **Structured JSON:** [`22c9299dc44ec9a9a074.json`](../../sessions/22/22c9299dc44ec9a9a074.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

部署汇报：

| 实验 | 状态 | 服务器 | PID | 显存 |
|------|------|--------|-----|------|
| eval_pi05_random_k095_object_seed43 (k=0.95) | **跳过** — registry 已有 DONE 结果 (SR=72.8%) | - | killed 101650 | - |
| eval_pi05_random_k09_object_seed43_v3 (k=0.9) | **RUNNING** | westd-27271:cuda:1 | 101722 | 10535 MiB |
| eval_pi05_random_k085_object_seed43 (k=0.85) | **跳过** — registry 已有 DONE 结果 (SR=3.8%) | - | killed 260638 | - |

实际部署 1 个实验（k=0.9 v3），2 个因 registry 已有完成结果而跳过并 kill。日志路径：`/tmp/eval_pi05_random_k09_object_seed43_v3.log`。

---
