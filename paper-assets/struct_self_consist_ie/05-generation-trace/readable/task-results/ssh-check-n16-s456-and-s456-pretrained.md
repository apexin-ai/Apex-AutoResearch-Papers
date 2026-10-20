# ssh check n16 s456 and s456 pretrained

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_n16_s456_and_s456_pretrained_20260521T192743_result.json`
- **Structured JSON:** [`dfb231677d5a3eb4e97d.json`](../../sessions/df/dfb231677d5a3eb4e97d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

### 实验 1: fewnerd_n16_s456_v2 — 已完成

| 项 | 值 |
|---|---|
| PID 54277 | 已退出 |
| samples.jsonl | 37648 行 (完整) |
| greedy_f1 | 0.7884 |
| oracle_f1 | 0.9058 |
| oracle_headroom | +11.74pp |
| fleiss_kappa_mean | 0.4540 |
| soft_jaccard_mean | 0.7046 |
| structural_beats_surface | true (rho_advantage=0.052) |
| verdict | FAIL (MVP single-subtask threshold) |

---

### 实验 2: e2_pretrained_fewnerd_s456 — 仍在运行

| 项 | 值 |
|---|---|
| PID 47635 | **运行中** |
| 进度 | **36% (13734/37648)**，已运行 ~11 min |
| 预计剩余 | ~29 min |
| 速度 | ~15 it/s |
| GPU 3 | 74% util, 30540/32607 MiB |
| samples.jsonl | 尚未写入（推断为完成后一次性写出） |

与你说的"之前 95%"不符——当前只有 36%。可能是进程重启过，或之前看到的是另一个实验的进度。

**recompute 暂不执行**，等实验 2 完成后再跑。预计还需 ~30 分钟。

---
