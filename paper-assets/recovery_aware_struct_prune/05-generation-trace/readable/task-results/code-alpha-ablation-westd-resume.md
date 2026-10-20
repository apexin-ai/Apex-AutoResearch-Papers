# code alpha ablation westd resume

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_alpha-ablation-westd-resume_20260515T084042_result.json`
- **Structured JSON:** [`58e66f744a30e2623c16.json`](../../sessions/58/58e66f744a30e2623c16.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-11672 状态报告

### 1. 进程状态
- **PID 7186 存活**，已运行 ~1h05m，nohup 方式（非 tmux）
- 当前双卡并行执行 Phase A Eval：
  - GPU0: α=2.0 eval — ~48/100（约 22 min 剩余）
  - GPU1: α=4.0 eval — ~14/100（约 43 min 剩余）

### 2. GPU / 磁盘
| 资源 | 状态 |
|------|------|
| GPU0 | 83%, 12969 MiB |
| GPU1 | 84%, 12957 MiB |
| 根分区 | 6.6/30GB (22%) |
| 数据盘 | 72/250GB (29%) |

### 3. 已完成的计算结果

**Phase 0:** ✅
- `importance_scores.pt` (17KB)
- `cka_scores.pt` (122KB)

**Phase A Prune:** ✅ 全部 5 个 α 值已完成
- `/root/autodl-tmp/recovery_aware_struct_prune/alpha_ablation/alpha_{0.0,0.5,1.0,2.0,4.0}/`

**Phase A Eval（已完成 3/5）:**

| α | Accuracy |
|---|----------|
| 0.0 | 0.30 |
| 0.5 | 0.25 |
| 1.0 | 0.27 |
| 2.0 | 🔄 运行中 |
| 4.0 | 🔄 运行中 |

**Phase B (SFT + Post-SFT Eval):** 尚未开始

### 4. 后续进度预估

Pipeline 会自动按顺序执行：
1. Phase A Eval 完成 — ~43 min
2. Phase B SFT（5 个 α，双卡并行，2 epochs）— ~2-3h
3. Phase B Post-SFT Eval — ~1-1.5h

**预计全部完成：~4-5h 后（约 UTC 21:00-22:00）**

### 5. 无需干预

Pipeline 通过 nohup 运行，状态健康，无需 kill 或重启。自动跳过已完成步骤（脚本有 `[SKIP]` 逻辑）。唯一风险是 nohup 进程可能因 OOM 或其他原因死亡——建议过几小时后回来检查。

---
