# ops full status check both servers

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_full-status-check-both-servers_20260516T121927_result.json`
- **Structured JSON:** [`7e53a35c424fc8045619.json`](../../sessions/7e/7e53a35c424fc8045619.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据收集完毕。汇总如下：

## GPU 进程状态汇总

### westd-47453（4×H800 97GB）

| GPU | PID | 实验 | 状态 | step/total | ETA | 备注 |
|-----|-----|------|------|-----------|-----|------|
| 0 | 324550 | threshold_q07 resume | 运行中 | 3368/8477 | ~26min | 从 ckpt-2000 恢复，GPU util 71% |
| 1 | 316988 | rho02_uniform | 运行中 | 1759/6103 | ~2h33m | **未完成**，29% 进度 |
| 2 | 326280 | batch_adaptive_tau_rho04 | 运行中 | 908/6103 | ~3h14m | 15% 进度，最晚启动 |
| 3 | 325202 | threshold_q03 restart | 运行中 | 2785/8477 | ~29min | 33% 进度 |

### westd-41312（4×H800 97GB）

| GPU | PID | 实验 | 状态 | step/total | ETA | 备注 |
|-----|-----|------|------|-----------|-----|------|
| 0 | 3112 | llama3b_uniform | 运行中 | 1011/8477 | ~1h16m | Llama-3.2-3B，gradient_checkpointing |
| 1 | 4005 | llama3b_adaptive | 运行中 | 852/8477 | ~1h17m | Llama-3.2-3B，gradient_checkpointing |
| 2 | 3661 | hybrid_rho04 | 运行中 | 6562/8477 | ~10min | Qwen3-0.6B，接近完成 |
| 3 | 3732 | hybrid_rho06 | 运行中 | 6703/8477 | ~9min | Qwen3-0.6B，接近完成 |

### 与预期对比

- **rho02_uniform**：预期"可能已完成"→ 实际仍在跑（29%，total=6103 而非 8477，因为 200M tokens / 更大 batch）
- **所有 PID** 与预期匹配（子进程偏移 +2~8 正常）
- **无状态不一致**：8 个实验全部正常运行中

### 预计完成顺序
1. hybrid_rho06 (~9min)
2. hybrid_rho04 (~10min)
3. threshold_q07 (~26min)
4. threshold_q03 (~29min)
5. llama3b_uniform (~1h16m)
6. llama3b_adaptive (~1h17m)
7. rho02_uniform (~2h33m)
8. batch_adaptive_tau_rho04 (~3h14m)

---
