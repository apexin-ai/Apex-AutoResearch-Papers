# ops westd results collect

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd-results-collect_20260515T143402_result.json`
- **Structured JSON:** [`60fd4388fd5d838958e2.json`](../../sessions/60/60fd4388fd5d838958e2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇总

### nvidia-smi
| GPU | 型号 | 温度 | 功耗 | 显存 | 利用率 |
|-----|------|------|------|------|--------|
| 0 | RTX PRO 6000 | 56°C | 361/600W | 65.6/97.9 GB | 95% |
| 1 | RTX PRO 6000 | 80°C | 600/600W | 22.6/97.9 GB | 99% |

GPU 0 上 2 个进程：PID 38514 (GraSP SFT, 52.5GB) + PID 38120 (GraSP pre-SFT eval n=100, 13GB)
GPU 1 上 1 个进程：PID 40494 (α=0.0 post-SFT eval, 22.6GB)

---

### GraSP SFT (cuda:0)
**仍在运行** — 1263/1870 steps (67%), ~19min 剩余
- 最新 loss=0.5828, token_accuracy=0.8455, epoch=1.348
- 速度 ~1.85s/step

### GraSP post-SFT eval
不存在（SFT 未完成）

### GraSP pre-SFT eval n=100 (cuda:0, PID 38120)
**运行中** — 24/100, ~107s/sample（因与 SFT 共享 GPU 0 导致很慢）
- ETA ≈ 2.3 小时

### α=0.0 post-SFT eval (cuda:1, PID 40494)
**运行中** — 30/100, ~2.4s/sample（非常快）
- 预计 3-4 分钟完成
- 尚无最终结果

### α=2.0 SFT
**失败 — CUDA OOM**。尝试在 GPU 0 上启动，但 GPU 0 已被 GraSP SFT + GraSP eval 占满（合计 ~64GB），Adam optimizer 分配 26MB 时爆内存。需要等 GPU 0 空闲后重跑，或改到 GPU 1。

### GraSP 1319-sample eval (`logs/graspune_eval.log`)
73/1319 (5.5%), ~51s/sample, 已无对应活跃进程 — 看起来是之前被杀掉或已失效的旧进程日志。当前只有 n=100 的 eval 在跑。

---

**关键问题**：α=2.0 SFT OOM 失败了，需要决定：
1. 等 GraSP SFT 完成 (~19min) + GraSP eval 完成后在 GPU 0 重跑
2. 等 α=0.0 eval 完成 (~3min) 后在 GPU 1 上启动

---
