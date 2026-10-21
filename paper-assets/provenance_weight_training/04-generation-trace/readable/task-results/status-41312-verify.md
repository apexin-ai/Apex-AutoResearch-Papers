# status 41312 verify

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_status_41312-verify_20260516T191004_result.json`
- **Structured JSON:** [`191eb92f1a9074f634a9.json`](../../sessions/19/191eb92f1a9074f634a9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-41312 状态验证报告

### Hostname 确认
`autodl-container-qz2syaltqs-0f5bd8e6` — 连接到 westd-41312（非 47453）。

### GPU 状态表

| GPU | PID | 实验 | 显存 | 利用率 |
|-----|-----|------|------|--------|
| 0 | 3112 | llama3b_uniform_seed42 | 71,362 / 97,887 MiB | 100% |
| 1 | 4005 | llama3b_adaptive_seed42 | 71,362 / 97,887 MiB | 100% |
| 2 | 3661 | hybrid_rho04_seed42 | 75,014 / 97,887 MiB | 100% |
| 3 | 3732 | hybrid_rho06_seed42 | 75,014 / 97,887 MiB | 100% |

硬件：4× NVIDIA RTX PRO 6000 Blackwell Server Edition (96GB)

### 实验进度

总步数计算：200M tokens / (4 × 4 × 2048) = **6,104 步**

每步在 step_metrics.jsonl 中写 4 行（每个 grad_accum micro-batch 一行）。

| 实验 | 当前 step | 总 step | 进度 | 模型 |
|------|-----------|---------|------|------|
| hybrid_rho04 | 3,954 | 6,104 | **64.8%** | Qwen3-0.6B |
| hybrid_rho06 | 3,999 | 6,104 | **65.5%** | Qwen3-0.6B |
| llama3b_uniform | 1,999 | 6,104 | **32.7%** | Llama-3.2-3B |
| llama3b_adaptive | 1,999 | 6,104 | **32.7%** | Llama-3.2-3B |

### hybrid_rho04 完成检查
- `final/` 目录：**不存在**
- `eval_perplexity_results.json`：**不存在**
- 仍在训练中，**未完成**

### 磁盘
```
/dev/md0  250G  60G  191G  24%  /root/autodl-tmp
```
充裕。

### 与 Reviewer 声称的差异

Reviewer 之前声称的状态与当前实际**不符**：

| 项目 | Reviewer 声称 | 实际 |
|------|--------------|------|
| hybrid_rho04 | eval loop 95%，即将完成 | training 64.8%，未进入 eval |
| hybrid_rho06 | training 59% | training 65.5% |
| llama3b_uniform | eval loop 进行中 | training 32.7% |
| llama3b_adaptive | 正常 | training 32.7% |

PID 匹配（3112/4005/3661/3732 全部正确），但进度百分比和阶段描述与 Reviewer 之前的报告有明显出入。可能是时间差异（Reviewer 的数据更早/更晚）或计算方式不同。

---
