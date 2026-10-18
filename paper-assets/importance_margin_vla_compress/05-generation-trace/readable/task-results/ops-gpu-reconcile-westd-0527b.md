# ops gpu reconcile westd 0527b

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu_reconcile_westd_0527b_20260527T005836_result.json`
- **Structured JSON:** [`472433bd6193e60998b3.json`](../../sessions/47/472433bd6193e60998b3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。汇总报告：

---

## GPU 占用表

### westd-38929 (2/4 GPU 活跃)
| GPU | VRAM | Util | PID | 实验 | Registry | Cron |
|-----|------|------|-----|------|----------|------|
| 0 | 15.9 GB | 70% | 623613 | `eval_openvla_l2norm_k05_long_seed42` | ✓ RUNNING | ✓ 已注册 |
| 1 | 0 | 0% | — | **空闲** | — | — |
| 2 | 16.1 GB | 71% | 732931 | `eval_openvla_l2norm_k075_long_seed42` | ✓ RUNNING | ✓ 已注册 |
| 3 | 0 | 0% | — | **空闲** | — | — |

### westd-41074 (4/4 GPU 活跃)
| GPU | VRAM | Util | PID | 实验 | Registry | Cron |
|-----|------|------|-----|------|----------|------|
| 0 | 16.2 GB | 61% | 32184 | `eval_openvla_random_k095_long_seed42` | ✓ RUNNING | ✓ 已注册 |
| 1 | 16.2 GB | 70% | 856656 | `eval_openvla_random_k075_long_seed42` | ✓ RUNNING | ✓ 已注册 |
| 2 | 16.0 GB | 69% | 934369 | `eval_openvla_random_k095_object_seed42` | ✓ **刚注册** | ✓ 已注册 |
| 3 | 16.1 GB | 71% | 824210 | `eval_openvla_attn_k075_long_seed42` | ✓ RUNNING | ✓ 已注册 |

---

## 已完成实验（之前在跑，现已结束）

| 实验 | 服务器 | 退出码 | SR | 完成时间 | Registry |
|------|--------|--------|-----|---------|----------|
| `eval_openvla_random_k085_long_seed42_v3` | westd-38929 | 0 | **45.0%** | 05-27 00:43 UTC | ✓ 已标记 DONE |
| `eval_openvla_random_k075_object_seed42` | westd-41074 | 0 | **50.4%** | 05-27 00:18 UTC | ⚠️ 需确认是否已标记 DONE |

之前 westd-38929 GPU3 的 PID 811418 (random k=0.75 Goal s42) 已消失，无对应 exit 文件——可能未通过 agent 提交，需单独排查。

---

## 空闲 GPU

- **westd-38929 GPU1** — 可部署新实验
- **westd-38929 GPU3** — 可部署新实验

---

## Cron 监控

两个 cron 已创建（每 13 分钟轮询）：
- `5c850866` — 监控 westd-38929 (2 个实验)
- `5841b8ae` — 监控 westd-41074 (4 个实验)

---
