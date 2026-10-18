# ops server audit and deploy

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_server_audit_and_deploy_20260528T062149_result.json`
- **Structured JSON:** [`2bc7eff60249767d9f27.json`](../../sessions/2b/2bc7eff60249767d9f27.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验都在加载模型，启动正常。

---

## 产出汇总

### 1. GPU 审计

| 服务器 | GPU 0 | GPU 1 | GPU 2 | GPU 3 |
|--------|-------|-------|-------|-------|
| w27 | ⚡ 69% | 空闲 | — | — |
| cqa1 | 空闲→已部署 | cron占用 | ⚡ 94% | cron占用 |
| w41 | ⚡ 39% | ⚡ 71% | ⚡ 34% | ⚡ 53% |
| w38 | ⚡ 28% | 空闲→已部署 | ⚡ 19% | ⚡ 39% |

### 2. 过期实验清理（8个→全部 DONE）

| # | exp_id | 结果 | SR |
|---|--------|------|-----|
| 1 | pi05_l2norm_k09_long_s43_cqa1 | ✅ success | **81.2%** |
| 2 | pi05_l2norm_k095_long_s43_w38 | ✅ success | **85.8%** |
| 3 | ov_attn_k075_long_s42 | ⚠️ killed (TIMEOUT T9@ep30) | 37.4% partial |
| 4 | pi05_l2norm_k085_long_s42 | ✅ success | **77.8%** |
| 5 | ov_random_k095_object_s42 | ✅ success | **67.4%** |
| 6 | pi05_random_k07_long_s42 | ✅ success | **62.4%** |
| 7 | ov_random_k075_goal_s42 | ✅ success | **72.0%** |
| 8 | ov_attn_k075_goal_s42 (w27) | ❌ killed (无效) | 67.4% invalid |

注：#3 的 v3 已在 w38 完成（SR=34.2%），无需再跑。

### 3. 新实验部署（2个）

| exp_id | 服务器:GPU | 状态 |
|--------|-----------|------|
| eval_pi05_l2norm_k05_long_seed46_strict | cqa1:0 | ✅ 启动中 |
| eval_pi05_attn_k05_long_seed46_strict | w38:1 | ✅ 启动中 |

剩余空闲: w27:1（仅支持 l2norm/random，无待部署实验）。

---
