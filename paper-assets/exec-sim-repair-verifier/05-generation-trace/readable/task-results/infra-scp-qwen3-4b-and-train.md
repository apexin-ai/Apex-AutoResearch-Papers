# infra scp qwen3 4b and train

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_scp-qwen3-4b-and-train_20260518T215731_result.json`
- **Structured JSON:** [`64119b87b9e801a042a2.json`](../../sessions/64/64119b87b9e801a042a2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练运行正常，32/147 steps (~22%)，约 2s/step。

## 报告

| 项目 | 结果 |
|------|------|
| **模型传输** | 直接从 hf-mirror.com 下载到 seetacloud，7.6GB，耗时 462.9s (~7.7 min) |
| **模型验证** | 通过 (vocab_size=151643, 3 个 safetensors shards 完整) |
| **训练启动** | 成功，PID 767245，GPU 0 |
| **训练进度** | 32/147 steps，~2s/step |
| **预估总时间** | ~5 min（147 steps × 2s/step ≈ 294s），比 DeepSeek TRAJ 快（模型更小） |
| **Registry** | `qwen3-4b-traj-repo-s42` → RUNNING |

---
