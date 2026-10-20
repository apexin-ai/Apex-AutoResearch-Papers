# ops llama31 taxei s0 diagnose

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_llama31-taxei-s0-diagnose_20260516T103834_result.json`
- **Structured JSON:** [`919560da2d32f578d892.json`](../../sessions/91/919560da2d32f578d892.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

### GPU 状态
| GPU | 显存占用 | 利用率 | 用途 |
|-----|---------|--------|------|
| cuda:0 | 16.8/32.6 GiB | 88% | llama31-vanilla-s0 eval（injected_eval.py） |
| cuda:1 | 25.9/32.6 GiB | 99% | **llama31-taxei-s0 v1 重试**（PID 262833） |
| cuda:2 | 26.0/32.6 GiB | 99% | **llama31-random-s0**（PID 260936） |
| cuda:3 | 0/32.6 GiB | 0% | 空闲 |

### llama31-taxei-s0 失败原因
- **原因**：SIGHUP（SSH 断连或父进程终止），非 OOM
- v0 在 step 1120/3387（33%）时被杀，内存稳定在 30.73/32 GiB

### 重试状态
- v1 重试**已在运行中**（18:18 启动），当前 step 540/3387（~16%），预计 ~1h50m 后完成
- 配置与 v0 完全一致：cuda:1, seed=0, 3 epochs, batch_size=4, ga=2, lr=1e-4
- Registry 已更新为 RUNNING

### 风险
v1 是通过交互式终端 + `tee` 启动的（非 tmux），如果 SSH 再断连会重蹈覆辙。训练已进行 ~21min，剩余 ~1h50m，目前没必要中断重启。完成后需手动更新 registry 到 DONE。

---
