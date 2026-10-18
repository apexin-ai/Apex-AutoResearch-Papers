# ops e1 deploy 9 table gaps

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_e1_deploy_9_table_gaps_20260523T060827_result.json`
- **Structured JSON:** [`0ba998210df085eab284.json`](../../sessions/0b/0ba998210df085eab284.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 8 个实验确认存活且正在产出结果。

---

## 部署完成报告

**原始 9 个实验中，1 个已完成，8 个刚部署成功：**

| # | exp_id | server | GPU | PID | status |
|---|--------|--------|-----|-----|--------|
| 1 | eval_pi05_random_k09_goal_seed42 | westd-41074 | 0 | 427737 | RUNNING (ep10, 50%) |
| 2 | eval_pi05_l2norm_k07_goal_seed42 | westd-41074 | 1 | 427998 | RUNNING (ep10, 70%) |
| 3 | eval_xvla_random_k07_spatial_seed42 | — | — | — | **DONE** (SR=76.6%) |
| 4 | eval_xvla_random_k05_goal_seed42 | westd-27271 | 0 | 250272 | RUNNING |
| 5 | eval_xvla_random_k09_long_seed42 | westd-27271 | 1 | 251117 | RUNNING |
| 6 | eval_xvla_l2norm_k07_long_seed42 | westd-38929 | 0 | 457656 | RUNNING |
| 7 | eval_xvla_random_k07_long_seed42 | westd-38929 | 1 | 458574 | RUNNING |
| 8 | eval_xvla_l2norm_k05_long_seed42 | westd-38929 | 2 | 459651 | RUNNING |
| 9 | eval_xvla_random_k05_long_seed42 | westd-38929 | 3 | 461085 | RUNNING |

**修复过的问题：**
- westd-38929 X-VLA 模型：相对导入 → 绝对导入、`_supports_sdpa` 安全访问、`_tied_weights_keys = None`、transformers 升级 5.5.3→5.5.4
- westd-41074 π0.5：缺少 `HF_HOME=/root/autodl-tmp/.hf_cache` 导致 tokenizer 下载失败
- X-VLA `--mode l2norm` → `--mode l2_norm`（脚本参数带下划线）

**使用 GPU：** 8/14（westd-41074 × 2, westd-27271 × 2, westd-38929 × 4）

---
