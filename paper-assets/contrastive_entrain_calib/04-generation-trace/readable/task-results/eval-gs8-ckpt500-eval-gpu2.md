# eval gs8 ckpt500 eval gpu2

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_gs8-ckpt500-eval-gpu2_20260522T211147_result.json`
- **Structured JSON:** [`7a89e7a87c0a738cbacd.json`](../../sessions/7a/7a89e7a87c0a738cbacd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

eval 已经跑完了，结果已存在。同时确认 GPU0 PID 958710 已不存在。

## gs8 ckpt-500 Eval 结果

| 指标 | 值 |
|------|-----|
| **SYCONScore** | **0.1045** |
| **ToF** | 0.0552 |
| **NoF** | 0.9558 |
| n_total | 362 (181 valid + 181 invalid) |
| 耗时 | 4070s |

## 对比

| 配置 | SYCONScore | 对比 |
|------|-----------|------|
| vanilla (baseline) | 0.1335 | — |
| gs=2 R3-only s1 ckpt-500 | 0.116 | -13.1% vs vanilla |
| gs=2 R3-only s2 ckpt-500 | 0.085 | -36.3% vs vanilla |
| **gs=8 ckpt-500** | **0.1045** | **-21.7% vs vanilla** |

gs8 ckpt-500 的 SYCONScore 0.1045，低于 vanilla 0.1335（降低 21.7%），介于 gs2-s1（0.116）和 gs2-s2（0.085）之间。ToF 仅 5.5%，说明模型几乎不翻转正确答案。NoF 高达 95.6%，说明面对错误压力时模型保持原答案的比例很高——抗 sycophancy 能力较强。

## GPU0 PID 958710

进程已不存在（ps 返回空），可能已自行结束。

---
