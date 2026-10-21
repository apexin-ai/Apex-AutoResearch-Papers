# ops server diagnostic and eval

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_server-diagnostic-and-eval_20260515T025241_result.json`
- **Structured JSON:** [`56466f1a4588a4a8367e.json`](../../sessions/56/56466f1a4588a4a8367e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 诊断 + Eval 报告

### 1. GPU 状态

| GPU | 显存 | 利用率 | 用途 |
|-----|------|--------|------|
| cuda:0 | 83123/97887 MiB (85%) | 91% | exp1-random-b03-s43-r4 训练 |
| cuda:1 | 0/97887 MiB | 0% | 空闲 |

### 2. 磁盘
82G / 250G = **33%**，无需清理。

### 3. exp1-random-b03-s43-r4 — 训练中

- **Step**: 105/500 (21%)，预计剩余 ~1h42m
- PID: 117571, tmux: `exp1-random-b03-s43-r4`
- 仅有 checkpoint-50（训练未达 500）
- Reward 大部分 step 为 0，偶发非零（step 73: 0.298, step 104: 0.149）
- **eval 无法执行**，需等训练完成生成 checkpoint-500

来源：`~/runs/solver-trace-ablation/exp1-random-b03-s43-r4.log`

### 4. exp1-random-b03-s44-r2 — Eval 完成

来源：`/root/autodl-tmp/outputs/eval_sta_exp1_random_b03_s44_r2.json`

| 指标 | 值 |
|------|-----|
| n_problems | 100 |
| n_proved | 23 |
| **prove_rate** | **0.23 (23%)** |
| **mean_isr** | **0.0000** |
| isr_std | 0.0000 |
| median_isr | 0.0000 |
| proved_only_mean_isr | 0.0000 |
| solver | Prover9Solver |
| logic_type | fol |

**按 answer type 分解：**

| 类型 | 数量 | proved | prove_rate | mean_isr |
|------|------|--------|------------|----------|
| false | 25 | 3 | 12.0% | 0.0 |
| unknown | 41 | 12 | 29.3% | 0.0 |
| true | 34 | 8 | 23.5% | 0.0 |

**H7 分类**（来源：`/root/autodl-tmp/outputs/h7_classification/h7_exp1_random_b03_s44_r2.json`）：

| 分类 | 结果 |
|------|------|
| H7 strict | 0/23 (0%) |
| H1 strict | 23/23 (100%) |
| H7+H1 | 23/23 (100%) |
| H7 relaxed | 0/23 (0%) |

### 5. 测试集确认
**proofwriter_fol_100.jsonl** — 命令行参数 `--data_path data/proofwriter_fol_100.jsonl` 验证通过 ✅

### 6. 待办
s43-r4 训练完成后（~1h40m），需在 cuda:1（或空闲 GPU）上运行 eval：
```bash
CUDA_VISIBLE_DEVICES=1 python3 scripts/eval_sta.py \
  --model_path /root/autodl-tmp/outputs/exp1_random_b03_s43_r4/checkpoint-500 \
  --data_path data/proofwriter_fol_100.jsonl \
  --output_path /root/autodl-tmp/outputs/eval_sta_exp1_random_b03_s43_r4.json \
  --logic_type fol
```

---
