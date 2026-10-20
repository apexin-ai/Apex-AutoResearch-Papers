# eval collect pending results

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_collect_pending_results_20260517T015739_result.json`
- **Structured JSON:** [`fac4f52986d4bef61b6b.json`](../../sessions/fa/fac4f52986d4bef61b6b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

---

### 任务 1: eval_pass_k8_rasp_20_grpo_deepseek (westd-11672)

**状态: 已完成** (PID 61473 已退出)

```json
{
  "model": "grpo_stage2_rasp_20_v9",
  "pass_at_k": 0.89,
  "k": 8,
  "temperature": 0.7,
  "n_problems": 200,
  "stderr": 0.0221,
  "eos_rate": 0.995,
  "avg_response_length": 162.58,
  "truncated": 8
}
```

---

### 任务 2: eval_grpo_standard_25 (westd-11672)

**状态: 运行中** (PID 48540, GPU 1)

进度: **1205/1319 (91.4%)**, 当前 acc=**0.5117**, eos_rate=96.50%, avg_len=285

预计剩余 ~5-8 分钟。结果文件尚未生成。

---

### 任务 3: eval_grpo_rasp_25 (westb-23072)

**状态: 运行中** (PID 639423, CPU 103%, 已运行 383 分钟)

结果文件尚未生成。无独立 log 可查（进程在前台 pts/0 运行）。

---

### 任务 4: Alpha Sweep 结果 (westd-11672)

模型路径: `outputs/alpha_ablation/sft_alpha_{α}`, greedy decoding, N=200

| α | Accuracy | n_correct | stderr | eos_rate | avg_len |
|---|----------|-----------|--------|----------|---------|
| 0.0 | 0.700 | 140 | 0.0324 | 1.000 | 132.96 |
| 0.3 | 0.730 | 146 | 0.0314 | 1.000 | 123.15 |
| 0.5 | 0.740 | 148 | 0.0310 | 1.000 | 131.09 |
| 0.7 | 0.735 | 147 | 0.0312 | 1.000 | 129.25 |
| 1.0 | **0.755** | 151 | 0.0304 | 1.000 | 127.36 |
| 2.0 | **0.755** | 151 | 0.0304 | 0.995 | 145.08 |

模型路径中未标注 sparsity 比例（仅 `sft_alpha_{val}`），无法仅从 JSON 判断是 20% 还是 25%。

---

### 任务 5: westd-11672 GPU 使用情况

| GPU | 型号 | Util | 显存 | PID | 用途 |
|-----|------|------|------|-----|------|
| 0 | RTX PRO 6000 | 0% | 0 / 97887 MiB | — | 空闲 |
| 1 | RTX PRO 6000 | 99% | 28911 / 97887 MiB | 48541 | eval_grpo_standard_25 |
| 2 | RTX PRO 6000 | 91% | 17623 / 97887 MiB | 67337 | 未知 python 进程 |
| 3 | RTX PRO 6000 | 99% | 29595 / 97887 MiB | 64889 | 未知 python 进程 |

GPU 2 和 GPU 3 上有未识别的 python 进程（PID 67337, 64889），不在本次检查的实验列表中。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "model": "grpo_stage2_rasp_20_v9",
    "pass_at_k": 0.89,
    "k": 8,
    "temperature": 0.7,
    "n_problems": 200,
    "stderr": 0.0221,
    "eos_rate": 0.995,
    "avg_response_length": 162.58,
    "truncated": 8
  }
}
```

</details>

---
