# ops pipeline monitor deploy v1

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_pipeline_monitor_deploy_v1_20260522T101131_result.json`
- **Structured JSON:** [`26bbba8b5f2eaa425d4f.json`](../../sessions/26/26bbba8b5f2eaa425d4f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 5 个新实验已注册并推进到 RUNNING。

---

## 已完成 + 已部署

### 收割 SR

| 完成的实验 | 服务器 | SR |
|---|---|---|
| l2norm_k05_spatial_s43 | westd-38929 GPU 0 | **58.2%** |
| random_k03_spatial_s43 | westd-38929 GPU 1 | **51.2%** |
| l2norm_k03_spatial_s43 | westd-38929 GPU 2 | **52.0%** |
| random_k03_object_s43_v4 | westd-38929 GPU 3 | **32.2%** |
| random_k085_obj_s43 | westd-41074 GPU 0 | **3.8%** |
| baseline_goal | cqa1 GPU 0 | CRASHED (网络) |
| baseline_long | cqa1 GPU 2 | CRASHED (网络) |

### 新部署（已验证）

| 新实验 | 服务器/GPU | PID | GPU 内存 | 验证 |
|---|---|---|---|---|
| l2norm_k095_long_s42 | westd-38929 GPU 0 | 931551 | 10753 MiB | ✓ |
| random_k09_goal_s42 | westd-38929 GPU 1 | 931818 | 10520 MiB | ✓ |
| l2norm_k09_goal_s42 | westd-38929 GPU 2 | 932076 | 10520 MiB | ✓ |
| random_k085_goal_s42 | westd-38929 GPU 3 | 931023 | 9700 MiB | ✓ |
| l2norm_k085_goal_s42 | westd-41074 GPU 0 | 399612 | 10514 MiB | ✓ T0 ep30 |
| baseline_goal (重部署) | cqa1 GPU 0 | 352950 | 10288 MiB | ✓ |
| baseline_long (重部署) | cqa1 GPU 2 | 353384 | 10512 MiB | ✓ |

## 仍在运行

| 实验 | 服务器 | 进度 | 预计完成 |
|---|---|---|---|
| l2norm_k09_obj_s43 | cqa1 GPU 1 | T9 ep20/50 (98%+) | ~30 min |

## 问题与修复

**三台服务器网络均不可达**（`[Errno 101] Network is unreachable`），导致 tokenizer `google/paligemma-3b-pt-224` 下载失败。

**修复**：所有重新部署均添加 `HF_HOME=/root/autodl-tmp/.hf_cache TRANSFORMERS_OFFLINE=1`，使用本地缓存的 tokenizer。westd-38929 GPU 0-2 首次部署漏设此变量导致崩溃，已修复并重新部署成功。

## Phase 2 进度

- **已部署**: 5 new + 2 baseline redeploys = **7 running**
- **完成**: 5 (spatial s43 × 3, object s43 × 2)
- **待部署**（等 cqa1 baselines 和 l2norm_k09_obj 完成）:
  - `random_k09_long_s42` → cqa1 GPU 0 (after baseline_goal)
  - `l2norm_k09_long_s42` → cqa1 GPU 2 (after baseline_long)
  - `random_k085_long_s42` → cqa1 GPU 1 (after l2norm_k09_obj_s43，因 westd-38929 已部署 l2norm_k095_long)

---
