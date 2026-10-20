# diagnose phase diagram t25 a075 s43 fp32

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_phase_diagram_t25_a075_s43_fp32_20260522T035645_result.json`
- **Structured JSON:** [`d34be7ca31b5f4fc7afa.json`](../../sessions/d3/d34be7ca31b5f4fc7afa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

### 失败根因: 进程被外部信号静默杀死（SIGHUP / OOM killer）

**依据:**
- 日志中**无任何 Traceback、Error、Killed** 记录
- 日志最后一行是 `Generating synthetic data …`（Gen 9），之后突然截断
- 进程在 GPU 密集型操作（文本生成）期间死亡，无机会写错误输出
- 符合 SIGHUP（SSH/tmux 断连）或 Linux OOM killer 的特征

**不是磁盘满** — 排除该项目的常见原因。

### 关键数据

| 项目 | 状态 |
|------|------|
| **训练进度** | **8/25 代完成**，gen_9 开始生成时死亡 |
| **最后完整代** | gen_8: ppl=73.31, entropy=2.2452, eff_rank=79.3, mauve=0.0311 |
| **磁盘** | 140G 可用 (45%)，实验目录 3.1G |
| **GPU** | 2× RTX PRO 6000 (98GB) 均空闲，状态正常 |
| **gen_9 状态** | 目录已创建但为空 |

### 可恢复性

- gen_8 checkpoint 存在且完整（model.safetensors 1.6GB + tokenizer + config）
- 无 `all_metrics.json`（仅在全部 25 代完成后生成）
- **可以 resume**，前提是 `iterative_train.py` 支持 `--resume_from_gen` 或类似参数；否则需要修改脚本从 gen_8 checkpoint 继续
- 重启前应清空 gen_9 空目录

---
