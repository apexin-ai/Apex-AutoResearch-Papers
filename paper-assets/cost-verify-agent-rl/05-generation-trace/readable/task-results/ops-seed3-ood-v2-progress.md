# ops seed3 ood v2 progress

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_seed3-ood-v2-progress_20260521T024207_result.json`
- **Structured JSON:** [`14428ef6cef7465ca1ea.json`](../../sessions/14/14428ef6cef7465ca1ea.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp029_seed3_ood_v2 进度

- **进程状态**: alive（PID 530289, 运行 2h03m）
- **GPU 利用率**: cuda:0 0%, cuda:1 0%（显存占用 46GB/98GB 和 45GB/98GB）
- **已完成**: 134/134 tasks — eval 已全部完成
- **当前阶段**: PPO update（compute_policy_loss），total_training_steps=1，即将结束
- **预估剩余**: <30min（PPO update 接近尾声）
- **异常**: 无严重错误（8547 条 `anchor_obs` 非数值型 metric 警告，无害）

### Eval 结果（step 15, 134 OOD games）

| 指标 | 值 |
|------|-----|
| **success (pass@1)** | **10.45%** (≈14/134) |
| action_is_effective | 92.6% |
| action_is_valid | 48.8% |
| avg num_actions | 41.9 |
| manager_invalid_action | 7.4% |
| avg response_length | 7500.7 tokens |

### W&B
- run_id: `gqr6ux4z`
- run name: `exp029-seed3-ood-final`
- project: `cost-verify-agent-rl`

---
