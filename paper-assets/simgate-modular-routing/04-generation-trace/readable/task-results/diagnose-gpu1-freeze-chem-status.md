# diagnose gpu1 freeze chem status

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_gpu1-freeze-chem-status_20260514T051149_result.json`
- **Structured JSON:** [`bab724238e1d86c95def.json`](../../sessions/ba/bab724238e1d86c95def.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

### GPU 状态
| GPU | 型号 | VRAM 占用 | 利用率 |
|-----|------|-----------|--------|
| GPU0 | RTX 5090 | **0 MiB** / 32607 MiB | 0% — 空闲 |
| GPU1 | RTX 5090 | **28013 MiB** / 32607 MiB | 0% (vLLM inference) |

### plan-001b-gpu1-freeze-chem (GPU1) — 存活
- **主进程**: PID 788063, 启动于 11:12 UTC, 仍在运行
- **vLLM 引擎**: PID 789051, 占用 28004 MiB
- **freeze**: **20/20 episodes — 已完成** (全部新采集, 无复用)
- **chemistry-mix**: **15/20 episodes — 进行中** (最后写入 13:10 UTC)
  - 目录名为 `chemistry-mix`，不是 `chemistry-mix-paint-secondary-color`

预计 chemistry-mix 剩余 5 个 episode，按当前速率还需约 20-30 分钟。

### plan-002-dryrun (GPU0) — 已死
- **PID 171059: 不存在**, GPU0 完全空闲
- 最后日志 (`logs/plan002_dryrun.log`, 13:04 UTC): Qwen3-1.7B LoRA 分类器训练, 停在 **step 310/1163 (27%)**, 速率 1.37 it/s
- 日志无错误信息，可能是 OOM 或被其他进程挤掉（GPU0 上还有 PID 43429 的 lifespan 恢复进程在跑 CPU 密集任务）

### GPU0 其他进程
- PID 43429: 99.9% CPU, 正在做 lifespan 数据恢复（非 GPU 任务）
- PID 36879: `run_gpu0_v6_lifespan.sh` 包装脚本

---
