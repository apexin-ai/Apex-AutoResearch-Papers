# ops falcon3 full status check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_falcon3-full-status-check_20260522T121016_result.json`
- **Structured JSON:** [`4de4d9d842954846f517.json`](../../sessions/4d/4de4d9d842954846f517.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

d050 eval 已提交（PID 631968, cuda:3）。

## 状态汇报

### 1. GPU 状态 (westd-29999)
| GPU | Memory Used | Total | Utilization |
|-----|------------|-------|-------------|
| 0 | 0 MiB | 97887 MiB | 0% |
| 1 | 0 MiB | 97887 MiB | 0% |
| 2 | 0 MiB | 97887 MiB | 0% |
| 3 | 0 MiB | 97887 MiB | 0% |

无运行中进程。4 卡全空闲。

### 2. Eval 结果（d000/d005/d025 全部完成，有 `.done` 标记）

| Dosage | MMLU (%) | ARC (%) |
|--------|----------|---------|
| d000 | 58.77 | 81.57 |
| d005 | 59.02 | 83.11 |
| d025 | 61.23 | 84.81 |
| d050 | **pending** (刚提交, PID 631968, cuda:3, ~3-4min) | **pending** |

MMLU 和 ARC 均呈单调上升趋势：d000→d025 MMLU +2.46pp, ARC +3.24pp。

### 3. d050 训练状态
**已完成**。epoch=1.0, train_loss=1.064, lora_adapter 已保存（177MB）。lora_alpha=32 确认合规（C006）。已自动提交 d050 eval。

### 4. d100 训练 (cqa1-21977)
Registry 显示 `sft_falcon3_7b_d100_s42` 仍标 RUNNING（在 cqa1-21977 cuda:0，lr=5e-5 重启后 PID 666107）。需要到 cqa1 服务器查进度。

### 5. evaluate.py 版本
westd-29999 上 evaluate.py 为 37775 bytes（C009 参考值 37591 bytes 有差异）。d000/d005/d025/d050 四个 eval 均使用同一版本，C010 一致性满足。

---
