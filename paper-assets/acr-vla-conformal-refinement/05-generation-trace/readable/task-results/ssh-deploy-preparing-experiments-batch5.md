# ssh deploy preparing experiments batch5

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_deploy-preparing-experiments-batch5_20260517T070743_result.json`
- **Structured JSON:** [`6dfed452b33391c02077.json`](../../sessions/6d/6dfed452b33391c02077.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GPU 4 进程确认启动成功（从 1 MiB → 5664 MiB）。

## 部署结果

| 实验 | 服务器 | GPU | PID | 状态 |
|------|--------|-----|-----|------|
| eval-obs-only-object-norm01-seed46 | bjb2-28827 | 4 | 365893 | ✅ 运行中 |
| eval-obs-only-object-norm01-seed47 | — | — | — | ❌ 无空闲 GPU |
| eval-perdof-object-norm01-seed46 | — | — | — | ❌ 无空闲 GPU |
| eval-perdof-object-norm01-seed47 | — | — | — | ❌ 无空闲 GPU |

**结论**：4 台服务器共 17 张卡中只有 bjb2-28827 GPU 4 空闲，已部署 1 个实验。其余 3 个实验无可用 GPU，需等待现有任务完成后再部署。

---
