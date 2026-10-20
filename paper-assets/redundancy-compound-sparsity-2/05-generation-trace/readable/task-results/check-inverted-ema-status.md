# check inverted ema status

**redundancy compound sparsity 2** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_inverted_ema_status_20260512T164737_result.json`
- **Structured JSON:** [`f5d11d287ec4e566e599.json`](../../sessions/f5/f5d11d287ec4e566e599.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态汇总

### 1. inverted_ema (Reasoning traces) — PID 39560
- **状态**: 运行中，已 16 分钟
- **进度**: 生成 reasoning traces 70% (14/20)，~60s/trace
- **阶段**: 仍在数据生成阶段，尚未开始 PPL 评估
- **预计**: 还需 ~6 min 完成 trace 生成，之后才进入评估
- **GPU**: GPU 0, 29198 MiB

### 2. inverted_ema_wikitext (WikiText-2) — PID 39080
- **状态**: 运行中，已 18 分钟
- **进度**:
  - `full` 策略已完成: **PPL = 7.1822**（这是全 KV cache 参考值）
  - `inverted_ema_0.9` 策略: prefill 阶段 88% (46/52)，之后还有 eval 阶段
- **GPU**: GPU 1, 32402 MiB

### 3. analysis_gamma_sweep — PID 40063
- **状态**: 运行中但有问题，已 14 分钟
- **问题**: 遇到 **CUDA OOM** — GPU 0 上与 PID 39560 争抢显存（两个进程共用 GPU 0，合计 ~61 GB / 95 GB）
- **当前进度**: `[random] eval` 17% (1167/6554)，OOM 可能被 try/except 捕获后继续执行
- **GPU**: GPU 0, 31852 MiB

### GPU 使用
| GPU | 利用率 | 显存 | 进程 |
|-----|--------|------|------|
| 0 | 95% | 61024 / 97887 MiB | PID 39560 (29 GB) + PID 40063 (31 GB) |
| 1 | 27% | 32411 / 97887 MiB | PID 39080 (32 GB) |

### Decision Gate 状态
- **Reasoning**: 尚无 PPL 结果，仍在生成 traces（阈值 < 1.2271）
- **WikiText**: full baseline PPL=7.1822，inverted_ema_0.9 正在 prefill 88%（阈值 < 7.6432）
- **结果文件**: 均未生成

### 风险
GPU 0 上两个进程（inverted_ema + gamma_sweep）显存竞争已触发 OOM。gamma_sweep 的结果可能不可靠，且可能拖慢 inverted_ema 的后续评估阶段。

---
