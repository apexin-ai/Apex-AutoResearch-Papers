# ssh full status check 20260522T3

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_full_status_check_20260522T3_20260522T221637_result.json`
- **Structured JSON:** [`e3c79073bc0863e86a09.json`](../../sessions/e3/e3c79073bc0863e86a09.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 全面状态报告

### 任务 1: westd-32935 GPU 状态

| GPU | Util | VRAM | 进程 | 任务 |
|-----|------|------|------|------|
| 0 | 0% | 0/98GB | 无 | **空闲** |
| 1 | 98% | 17.0/98GB | PID 75284 | CKA-only MATH-500 |
| 2 | 0% | 0/98GB | 无 | **空闲**（α=0.5 已完成） |
| 3 | 87% | 13.0/98GB | PID 79030 | α=1.0 MATH-500 v2 |

### 任务 2: westb-23072 GPU 状态

| GPU | Util | VRAM | 进程 | 任务 |
|-----|------|------|------|------|
| 0 | **100%** | **0 MiB** | 无 | **异常** — 高 util 但无进程无显存 |
| 1 | 96% | 16.5/98GB | PID 220343 | MF3 v3 Qwen-Math |

### 任务 3: 所有 MATH-500 结果汇总

| 模型 | Accuracy | Correct/Total | Truncated | 位置 |
|------|----------|---------------|-----------|------|
| **Unpruned** (DeepSeek-R1-Qwen-7B) | **73.6%** | 368/500 | 124 | autodl-tmp |
| SFT Standard 20% | 26.0% | 130/500 | 211 | autodl-tmp |
| GRPO Standard 20% (fair 2048 v2) | 26.4% | 132/500 | 222 | relative |
| SFT RASP (α=1.0 default) | 24.2% | 121/500 | 174 | autodl-tmp |
| SFT RASP α=0.5 | 25.4% | 127/500 | 220 | autodl-tmp |
| SFT RASP α=2.0 | 24.0% | 120/500 | 155 | relative |
| SFT RASP α=3.0 | 23.2% | 116/500 | 144 | autodl-tmp |
| SFT RASP α=4.0 | **26.6%** | 133/500 | 190 | autodl-tmp |
| SFT Random 20% (v3) | 14.4% | 72/500 | 329 | relative |
| SFT RASP α=1.0 v2 | **进行中** | ~306/500 | — | — |
| SFT CKA-only | **进行中** | ~290/500 | — | — |

### 任务 4: α=0.5 — **已完成**
accuracy=25.4%, 结果已保存。

### 任务 5: α=1.0 v2 — **进行中**
306/500 (61%)，~56 min elapsed，ETA ~30-40 min。

### 任务 6: CKA-only — **进行中**
290/500 (58%)，日志从 05-23 04:08 开始，已跑 ~2h，ETA ~1.5h（该模型每步较慢，~30s/it 平均）。

### 任务 7: MF3 v3 (westb:1) — **进行中**
PID 220343 活跃，占用 16.5GB VRAM。结果文件尚未生成。

### 任务 8: α=3.0 GSM8K
- `eval_gsm8k_sft_alpha3p0_20.json`: accuracy=**64.1%** (846/1319)

### 异常项
- **westb GPU 0**: 100% utilization 但 0 MiB 显存、无计算进程 — 持续异常，可能需要重启实例或 `nvidia-smi -r` 重置。

---
