# ssh deploy seed47 pair

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_deploy-seed47-pair_20260516T202044_result.json`
- **Structured JSON:** [`3911380169d12f5112f8.json`](../../sessions/39/3911380169d12f5112f8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**bjb1-18228 GPU 审计结果：全部 4 张 GPU 均在使用中，无法部署。**

| GPU | 显存占用 | 利用率 | 实验 |
|-----|---------|--------|------|
| 0 | 3804 MiB | 21% | crm_obs_only norm=0.1 seed45 object |
| 1 | 11288 MiB | 99% | vla_only seed46 + crm_perdof norm01 seed44（两个进程共享） |
| 2 | 4268 MiB | 22% | crm_perdof norm=0.3 seed44 object |
| 3 | 4268 MiB | 21% | crm_obs_only norm=0.2 seed46 object |

5 个 evaluate.py 进程分布在 4 张 GPU 上，所有 GPU 均有活跃模型加载。**没有空闲 GPU，无法部署 seed47 配对实验。**

需要等现有实验完成释放 GPU，或在其他服务器部署。

---
