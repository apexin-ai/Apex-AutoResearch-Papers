# ops llama70b infer confirm

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_llama70b_infer_confirm_20260523T160731_result.json`
- **Structured JSON:** [`de87baec06763b482239.json`](../../sessions/de/de87baec06763b482239.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总：

## 状态：推理已开始 ✓

| 项目 | 值 |
|------|-----|
| **推理状态** | YES — 正在运行 |
| **当前基准** | gsm8k（第 2 个，共 5 个：mmlu/gsm8k/arc/hellaswag/math） |
| **MMLU** | 已跳过（输出已存在） |
| **GPU utilization** | 4 × 100%，各 ~87.7GB/98GB |
| **进程** | PID 334256，运行 2 分钟 |

## 进度与 ETA

- **总量**：5 个基准 × 288 conditions × 200 items = **288,000 evals**
- **gsm8k 进度**：Condition 1/288 完成（181/200 correct），Condition 2 刚开始
- **Condition 1 耗时**：~73 秒（200 items，~2,627 input toks/s，~401 output toks/s）
- **gsm8k 剩余**：287 conditions × 73s ≈ **5.8 小时**
- **全部 4 个剩余基准**（gsm8k+arc+hellaswag+math）：4 × 288 × 73s ≈ **23.5 小时**（假设各基准速度相近）
- **预计完成**：约 **5 月 25 日 00:00**（服务器时间，当前 00:08）

速度可能因基准不同略有差异（不同 prompt 长度/生成长度），以上为粗略估算。

---
