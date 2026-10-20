# ops loop16 status check

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_loop16_status_check_20260521T084406_result.json`
- **Structured JSON:** [`578b371d272a371c8a67.json`](../../sessions/57/578b371d272a371c8a67.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 17855 GPU 状态

| GPU | Util | VRAM Used | 实验 | 运行时间 | 状态 |
|-----|------|-----------|------|----------|------|
| 0 | 94% | 21.2/95.6 GB | interv_react_s43 + D37-G eval (a075) | 12h18m / 1h26m | 运行中 |
| 1 | 70% | 15.2/95.6 GB | (truncated, 预期 gen_gpt2m_s43) | — | 运行中 |
| 2 | 72% | 14.2/95.6 GB | (truncated, 预期 a000_s45) | — | 运行中 |
| 3 | 99% | 69.1/95.6 GB | scale_69b_bf16 (pythia-6.9b s43) | 9h21m | 运行中 |
| 4 | 96% | 20.3/95.6 GB | a052_s43_fp32 + phase_diagram dryrun | 1h47m / 1h11m | 运行中 |
| 5 | 86% | 14.2/95.6 GB | a046_s43_fp32 | 1h47m | 运行中 |

**注意**: GPU 0 上 interv_react_s43（非预期的 a000_s47_fp32）占据了 cuda:0，同时 D37-G eval 也在 cuda:0 上运行。a000_s47_fp32 进程确实存在（1h47m），但 GPU 分配可能与预期不同（部分进程信息被截断）。

## 19828 GPU 状态

| GPU | Util | VRAM Used | 实验 | 运行时间 | 状态 |
|-----|------|-----------|------|----------|------|
| 0 | 94% | 24.6/95.6 GB | a000_s48_fp32 | 38m + 34m | **⚠️ 双实例** |
| 1 | 97% | 13.9/95.6 GB | a000_s46_fp32 | 2h29m | 运行中 |

**⚠️ 问题**: GPU 0 上有**两个** a000_s48_fp32 进程（PID 655861 和 656193），都绑定 CUDA_VISIBLE_DEVICES=0。VRAM 比 GPU 1 高 ~11GB，确认双实例在争抢资源。应终止其中一个。

## Phase Diagram 代码

**存在** — `scripts/phase_diagram/` 目录包含 12 个脚本：

| T | α 值 |
|---|------|
| T=5 | a045, a050, a060, a075 |
| T=15 | a045, a050, a060, a075 |
| T=25 | a045, a050, a060, a075 |

所有脚本均为 s42，创建于 2026-05-21 16:39。项目根目录无 `run_phase_diagram*.sh`。17855 上有一个 phase_diagram dryrun 正在 cuda:4 运行（1h11m）。

## 已完成实验

**无** — 两台服务器所有 GPU 利用率均 ≥70%，全部实验仍在运行中。

## 需关注

1. **19828 GPU 0 双实例**: 两个 a000_s48_fp32 竞争同一 GPU，需 kill 其中一个
2. **17855 GPU 0**: interv_react_s43 占用了预期给 a000_s47_fp32 的 GPU，两者可能共存但 VRAM 偏高

---
