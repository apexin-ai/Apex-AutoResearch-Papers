# infra fix westd15695 olmo yi

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_fix_westd15695_olmo_yi_20260521T151037_result.json`
- **Structured JSON:** [`8219223edf36ee7c76b6.json`](../../sessions/82/8219223edf36ee7c76b6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Yi 推理正常运行。以下是完整汇报。

---

## 汇报

### 1. OLMo 崩溃原因

**不是崩溃**。原始运行使用了错误的 items 文件 `data/mmlu_items.json`（50 items）而非 `data/mmlu_items_exp001.json`（200 items）。432 条件 × 50 items = 21,600 行，运行实际上已正常完成，只是输出只有预期的 25%。

### 2. OLMo 重启状态

- **已完成** — 86,400/86,400 行，432 条件 × 200 items
- 用时约 5 分钟（Blackwell sm120 非常快）
- 输出: `results/exp001_olmo/olmo_mmlu.jsonl`
- 修复措施：
  - 添加了 `VLLM_USE_FLASHINFER_SAMPLER=0` 绕过 flashinfer 不支持 Blackwell sm120 的问题
  - Patch 了 flashinfer 的 `check_cuda_arch()` 
  - 给 `run_experiment.py` 加了 `--resume` 功能（条件级别跳过）
  - 旧数据备份在 `olmo_mmlu_50items_backup.jsonl`

### 3. Yi 排队状态

- **已自动启动** — 监控脚本检测到 OLMo 完成后于 23:25:51 自动启动
- PID: 24023，GPU 99% 利用率
- 当前进度: 2,600/86,400 (3%)，约 5 分钟可完成
- 输出: `results/exp001_yi/yi_mmlu.jsonl`

### 4. westd-32570 MATH 进度

| 模型 | 行数 | 目标 | 进度 |
|------|------|------|------|
| Gemma | 21,000 | 57,600 | 36.5% |
| Qwen | 29,800 | 57,600 | 51.7% |
| Mistral | 44,200 | 57,600 | 76.7% |
| Llama | 45,600 | 57,600 | 79.2% |

4 张 GPU 均在 88-100% 利用率运行。

### 5. OLMo 完成时间

已完成。从启动到完成约 5 分钟（~1.15 条件/秒，Blackwell RTX PRO 6000 96GB）。Yi 预计也是约 5-7 分钟完成。

---
