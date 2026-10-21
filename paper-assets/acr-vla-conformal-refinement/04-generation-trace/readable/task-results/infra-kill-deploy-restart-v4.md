# infra kill deploy restart v4

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_kill-deploy-restart-v4_20260513T184751_result.json`
- **Structured JSON:** [`83ea1fa6174ed20d16e6.json`](../../sessions/83/83ea1fa6174ed20d16e6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

| # | 项目 | 状态 |
|---|------|------|
| 1 | GPU 清空 | 4 GPU 全部释放 |
| 2 | Wrapper 部署 | 281行，flip/resize_with_pad/_unnormalize_action 全部验证通过 |
| 3 | evaluate.py | **已修复** 2 个 bug：`get_eef_state`→`get_robot_state`(6D→8D+gripper_qpos)、`eef_state=`→`robot_state=` |
| 4 | train_crm.py | `--cache_dir` 有效，默认 `/root/autodl-tmp/crm_cache/`，旧 cache 已清除 |
| 5 | 最小验证 | Import + split_action 通过 |
| 6 | 实验提交 | 4 个实验已启动 |

| exp_id | PID | GPU |
|--------|-----|-----|
| eval-spatial-v4-full | 69379 | cuda:0 |
| precompute-v4-shard0 | 69647 | cuda:1 |
| precompute-v4-shard1 | 69793 | cuda:2 |
| precompute-v4-shard2 | 69937 | cuda:3 |

---
