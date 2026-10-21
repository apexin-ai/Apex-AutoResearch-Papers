# audit westd41074 gpu3 deploy 20260526b

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_westd41074-gpu3-deploy-20260526b_20260526T182559_result.json`
- **Structured JSON:** [`953dcba67506e7f144e2.json`](../../sessions/95/953dcba67506e7f144e2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

一切正常。

## 汇报

### GPU 审计 (westd-41074)
| GPU | 显存 | 利用率 | 任务 |
|-----|------|--------|------|
| 0 | 15980/97887 MiB | 81% | `random_k085_object_seed42` (PID 682346) |
| 1 | 15980/97887 MiB | 70% | `attn_k05_object_seed42` (PID 652888) |
| 2 | 15980/97887 MiB | 88% | `attn_k075_object_seed42` (PID 755986) |
| 3 | 16188/97887 MiB | 70% | **新部署** ← |

### eval_openvla_l2norm_k075_object_seed42 最终结果
- **SR = 57.4%** (287/500)
- 完成时间：2026-05-27 02:02:55
- 耗时：289 分钟
- 结果文件：`eval_results/openvla_l2norm_prune_k075_object_seed42.json`

### 新实验部署
- **exp_id**: `eval_openvla_attn_k075_long_seed42`
- **PID**: 824210
- **tmux session**: `eval_openvla_attn_k075_long_seed42`
- **GPU**: westd-41074 cuda:3 (16188 MiB)
- **模型**: `/root/autodl-tmp/openvla-7b-finetuned-libero-10` (unnorm_key=`libero_10`)
- **日志确认**: 模型已加载，Attention pruning 256→192 tokens (k=0.75)，Task 1/10 已开始

注：任务模板中 `--model_path` 和 `--unnorm_key` 已修正为与现有 Long 实验一致的 `/root/autodl-tmp/openvla-7b-finetuned-libero-10` + `libero_10`（原模板用了不存在的 `models/` 路径和不匹配的 `bridge_orig`）。

---
