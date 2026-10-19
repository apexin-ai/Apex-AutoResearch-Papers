# ops kill duplicates and deploy magnitude

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_kill-duplicates-and-deploy-magnitude_20260517T225855_result.json`
- **Structured JSON:** [`916e900735e1a3a98dc8.json`](../../sessions/91/916e900735e1a3a98dc8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

**bjb2-28827 kill 结果**：PID 449339、476536 已成功 kill（exit code 0）。GPU0-5 仍有其他实验在跑。

**bjb1-18228 GPU 状态**：
| GPU | 状态 | 显存 |
|-----|------|------|
| GPU0 | 占用 (PID 713405) | 3342MiB |
| GPU1 | 空闲 | 4MiB |
| GPU2 | 空闲 | 4MiB |
| GPU3 | 占用 (PID 749547) | 5200MiB |

**部署实验**：

| 实验 | exp_id | GPU | PID | 参数 |
|------|--------|-----|-----|------|
| obs_only norm01 seed48 | `eval_obs_only_norm01_seed48` | GPU1 | 774337 | `--max_correction_norm 0.1` |
| obs_only norm03 seed48 | `eval_obs_only_norm03_seed48` | GPU2 | 774538 | `--max_correction_norm 0.3` |

---
