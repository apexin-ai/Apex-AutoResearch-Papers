# infra full gpu status check

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_full-gpu-status-check_20260512T142131_result.json`
- **Structured JSON:** [`d9244c35efa0cfcbb898.json`](../../sessions/d9/d9244c35efa0cfcbb898.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇总

### seetacloud-westd-4x5090 (4× RTX 5090)

| GPU | 状态 | PID | 进程 | 显存 |
|-----|------|-----|------|------|
| 0 | **占用** | 34681 | `train_repo_verifier.py` (repo-level-cls) | 31133/32607 MiB |
| 1 | **空闲** | — | — | 0 MiB |
| 2 | **占用** | 47236 | `train_cwm_baseline.py` (cwm8b-seed456) | 26207/32607 MiB |
| 3 | **空闲** | — | — | 0 MiB |

### home-1x5090 (1× RTX 5090)

| GPU | 状态 | PID | 进程 | 显存 |
|-----|------|-----|------|------|
| 0 | **占用** | 2810148 | `train_verifier.py` (cls8b-seed456) | 26221/32607 MiB |

---

### 实验真实状态

| 实验 | 状态 | 进度 | 位置 | 备注 |
|------|------|------|------|------|
| **repo-level-cls** | **运行中** | 1150/6633 (17%), ~2h49m | westd GPU 0 | ~8.5s/it, ETA ~13h |
| **repo-level-cwm** | **已崩溃** | 694/6633 (10%) 时终止 | westd (已退出) | `EXIT_CODE=143` (SIGTERM 被杀) |
| **cwm8b-seed456** | **运行中** | 423/1434 (29%), ~24min | westd GPU 2 | Qwen3-8B, ~3.4s/it, ETA ~60min |
| **cls8b-seed456** | **运行中** | ~150/948 eval中 | home GPU 0 | Qwen3-8B, 正在 eval 迭代 |

### 缺失产出

- `eval_repo_cls.json` — 不存在
- `eval_repo_cwm.json` — 不存在
- `*cls_cwm*.json` / `*5paired*.json` — 不存在

---

**关键发现：repo-level-cwm 已死（SIGTERM），GPU 1 和 GPU 3 空闲。** Director 的判断部分正确：repo-level-cls 确实在跑，但 repo-level-cwm 已被杀掉，需要重启。westd 有 2 个空闲 GPU 可用。

---
