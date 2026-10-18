# diagnose westd servers status registration

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_westd_servers_status_registration_20260527T060212_result.json`
- **Structured JSON:** [`b7617a75c2d6636f29a2.json`](../../sessions/b7/b7617a75c2d6636f29a2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。以下是三台服务器 GPU 状态表和注册汇总。

---

## GPU 状态表

### westd-27271 (2× RTX PRO 6000 Blackwell)

| GPU | 内存使用 | 利用率 | 进程 | 实验 | 状态 |
|-----|---------|--------|------|------|------|
| 0 | 15964/97887 MiB | 80% | PID 728571 | OV Attn k=0.95 Goal s42 v2 | **RUNNING** (Task 1/10) |
| 1 | 1/97887 MiB | 0% | — | OV Attn k=0.95 Object s42 | **已完成 SR=71.2%** |

### westd-38929 (4× RTX PRO 6000 Blackwell)

| GPU | 内存使用 | 利用率 | 进程 | 实验 | 状态 |
|-----|---------|--------|------|------|------|
| 0 | 1/97887 MiB | 0% | — | OV L2norm k=0.5 Long s42 (原 PID 623613) | **已完成 SR=16.4%** |
| 1 | 16394/97887 MiB | 70% | PID 949447 | OV L2norm k=0.95 Long s42 | RUNNING (registry) |
| 2 | 15780/97887 MiB | 71% | PID 968309 | OV L2norm k=0.75 Long s42 v2 | RUNNING (registry) |
| 3 | 16394/97887 MiB | 66% | PID 950007 | OV Attn k=0.95 Long s42 | RUNNING (registry) |

原 GPU 3 PID 811418 (OV Random k=0.75 Goal) 已完成 → **SR=72.0%**

### westd-41074 (4× RTX PRO 6000 Blackwell)

| GPU | 内存使用 | 利用率 | 进程 | 实验 | 状态 |
|-----|---------|--------|------|------|------|
| 0 | 15978/97887 MiB | 68% | PID 32184 | OV Random k=0.95 Long s42 | RUNNING (registry) |
| 1 | 10724/97887 MiB | 20% | PID 177597 | π0.5 Random k=0.75 Long strict | **RUNNING** (Task 1 done, 84%) |
| 2 | 10486/97887 MiB | 32% | PID 94308 | π0.5 Attn k=0.9 Long strict | RUNNING (registry) |
| 3 | 10824/97887 MiB | 51% | PID 94384 | π0.5 Attn k=0.85 Long strict | RUNNING (registry) |

原始 PID 全部已死：856148 (Random k=0.75 Object) → **SR=50.4%**，934369 (Random k=0.95 Object) → **SR=67.4%**，824210 (Attn k=0.75 Long) → **超时 EXIT_CODE=124**

---

## Registry 操作汇总

| 实验 | 操作 | SR |
|------|------|----|
| `eval_openvla_attn_k095_goal_seed42_v2` | PENDING → RUNNING，更新 spec (westd-27271 GPU0, PID 728571) | 进行中 |
| `eval_pi05_random_k075_long_seed42_strict` | PREPARING → RUNNING (westd-41074 GPU1, PID 177597) | 进行中 |
| `eval_openvla_random_k075_goal_seed42` | PREPARING → DONE | **72.0%** |
| `eval_openvla_random_k075_object_seed42` | PREPARING → DONE | **50.4%** |
| `eval_openvla_random_k095_object_seed42` | PREPARING → DONE | **67.4%** |
| `eval_openvla_attn_k095_object_seed42` | RUNNING → DONE (额外发现) | **71.2%** |

**空闲 GPU**：westd-27271 GPU1、westd-38929 GPU0 可用于新实验。

---
