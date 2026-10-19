# deploy bjb2 28827 5gpu batch

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_bjb2-28827-5gpu-batch_20260520T193948_result.json`
- **Structured JSON:** [`3b345d88987d1a75e40e.json`](../../sessions/3b/3b345d88987d1a75e40e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

没有 MCP 的 delete_cron 工具。seed48 的旧 cron 会因为旧 PID 不存在而自动失效，新进程已在跑，不影响监控。

部署完成。汇总：

| GPU | exp_id | PID | norm | seed | registry | cron |
|-----|--------|-----|------|------|----------|------|
| 0 | eval-obs-only-object-norm02-seed53 | 797335 | 0.2 | 53 | RUNNING | ✓ |
| 1 | eval-obs-only-object-norm003-seed45 | 798783 | 0.03 | 45 | RUNNING | ✓ |
| 3 | eval-obs-only-object-norm005-seed47 | 800192 | 0.05 | 47 | RUNNING | ✓ |
| 4 | eval-obs-only-object-norm01-seed48 | 801681 | 0.1 | 48 | RUNNING | 旧cron存在 |
| 5 | eval-obs-only-object-norm02-seed54 | 803103 | 0.2 | 54 | RUNNING | ✓ |

nvidia-smi 确认 GPU 0/1/3/4/5 均有进程（~5.7GB显存），GPU 2 空闲（cuda:2 的 seed43-r3 已自然结束）。

---
