# maintenance disk check plan006 prep

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_maintenance_disk-check-plan006-prep_20260514T064110_result.json`
- **Structured JSON:** [`bbff04c57779f3885bd2.json`](../../sessions/bb/bbff04c57779f3885bd2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 磁盘 + plan006 准备报告

### 磁盘状态
- /root/autodl-tmp: **250G 总量 / 79G 已用 / 172G 可用 (32%)**
- outputs/ 目录占 61G，内含：
  - `plan002_additive_b01_s42/` — 31G
  - `plan016_extended_1000_s42/` — 16G
  - `plan001_exec_only_s42/` — 15G
  - 其余为 eval JSON/log 文件（几乎不占空间）
- Step 2 中列出的 5 个旧实验目录**已不存在**（之前已清理）

### plan006 Prolog 就绪检查
| 项目 | 状态 |
|------|------|
| Prolog config | **有** — `grpo_prolog_exec_only.yaml`, `grpo_prolog_exec_sta.yaml` |
| 训练数据 | **有** — config 引用 `data/train_500_seed42.jsonl`（符合 C001） |
| SWI-Prolog | **有** — `/usr/bin/swipl` |
| 脚本支持 | `train_grpo.py`, `eval_sta.py`, `sta_prolog.py` 均含 Prolog 逻辑 |

### 结论
- **磁盘充足**：172G 可用，plan006 需 ~30G（10G × 3 seeds），无需清理
- **plan006 可以直接启动**，config/数据/SWI-Prolog/脚本全部就绪

---
