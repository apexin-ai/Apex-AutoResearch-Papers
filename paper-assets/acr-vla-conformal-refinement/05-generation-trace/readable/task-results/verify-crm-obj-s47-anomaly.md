# verify crm obj s47 anomaly

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_crm-obj-s47-anomaly_20260524T115755_result.json`
- **Structured JSON:** [`e5e20b35a3b1f80c06e4.json`](../../sessions/e5/e5e20b35a3b1f80c06e4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All checks complete. Here's the summary:

## CRM s47 验证

参数全部正确：
- mode: `crm_obs_only` ✓
- benchmark: `object` ✓
- max_correction_norm: `0.05` ✓
- K: `10` ✓
- seed: `47` ✓
- crm_checkpoint: `/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt` ✓
- conformal_threshold: `0.074855` ✓
- JSON 输出确认 10 tasks × 20 rollouts = 200 total, SR=82.5%

**结论：合法结果（随机波动），无需重跑**

## Long s47 假失败检查

| exp_id | 实际状态 | SR | 操作 |
|--------|---------|-----|------|
| eval-supp-long-crm-norm005-s47 | 已修正为 success | 56.5% | 无需操作（已修正） |
| eval-supp-long-reconvla-s47 | 已修正为 success | 55.0% | 无需操作（已修正） |
| eval-supp-long-adapt-tau025-s47 | **真失败** | — | 需要重跑（cqa1-32758 上日志在 KITCHEN_SCENE8 中断，无 JSON 输出） |
| eval-supp-long-k2mean-s47 | **真失败** | — | 需要重跑（同上，cqa1-32758 上中断于 KITCHEN_SCENE8） |

## 其他假失败扫描

扫描范围：最近 48h，conclusion=failed 的 eval-supp-* 实验

发现 **0 个假失败**，全部为真失败：

| exp_id | 服务器 | 失败原因 |
|--------|--------|---------|
| eval-supp-obj-adapt-tau025-s45 | bjb2-40593 | FileNotFoundError: CRM checkpoint 不存在 |
| eval-supp-k2mean-goal-s42 | bjb2-40593 | log=n/a，未成功启动 |
| precompute-smolvla-goal-bjb1-32546 | bjb1-32546 | LIBERO data not found at libero_goal 路径 |

---
