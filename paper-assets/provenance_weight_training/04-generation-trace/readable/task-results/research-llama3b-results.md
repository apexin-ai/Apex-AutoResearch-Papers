# research llama3b results

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_llama3b_results_20260519T051512_result.json`
- **Structured JSON:** [`d14a8f6a4b1ab7d4c58b.json`](../../sessions/d1/d14a8f6a4b1ab7d4c58b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完成。以下是完整结果表。

---

## Llama-3.2-3B Cross-Architecture 实验完整结果

### 训练配置

| 参数 | 值 |
|------|-----|
| Model | `unsloth/Llama-3.2-3B` (3.21B params) |
| Data | `data/scored_data.jsonl` (371,499 samples, ρ=0.4) |
| Tokens | 200M |
| Batch size | 4 (grad_accum=4, effective=16) |
| LR | 5e-5 |
| Max length | 2048 |
| Seed | 42 |
| Precision | bf16 + gradient checkpointing |
| Steps | 6,103 |
| Runtime | ~26h each |
| Server | westd-41312 (RTX PRO 6000 Blackwell) |
| Adaptive τ | 0.8, n_min=2 |

---

### PPL (Holdout Perplexity)

| exp_id | Method | Eval Loss | PPL | Eval Tokens | Source |
|--------|--------|-----------|-----|-------------|--------|
| `llama3b_uniform_seed42` | Uniform | 2.3397 | **10.38** | 1,526,195 | eval log + registry |
| `llama3b_adaptive_seed42` | Adaptive | 2.3590 | **10.58** | 4,017,316 | reeval JSON + registry |

> **⚠️ PPL 不可直接比较**: eval tokens 差 2.6x（1.5M vs 4.0M），说明使用了不同 eval 配置。memory.md 记录的 uniform PPL=10.53 在服务器上找不到对应 eval 文件，唯一可验证值为 10.38。

---

### MMLU (5-shot, lm-eval-harness v0.4.11)

| Category | Uniform (%) | Adaptive (%) | Δ (pp) |
|----------|-------------|--------------|--------|
| **Overall** | **51.85** ± 0.41 | **53.42** ± 0.41 | **+1.57** |
| Humanities | 46.48 ± 0.69 | 48.88 ± 0.70 | +2.40 |
| Social Sciences | 59.70 ± 0.87 | 61.39 ± 0.86 | +1.69 |
| STEM | 45.73 ± 0.87 | 45.99 ± 0.87 | +0.25 |
| Other | 58.42 ± 0.86 | 59.93 ± 0.85 | +1.51 |

Source: `llama3b_uniform_mmlu` / `llama3b_adaptive_lm_eval` (westd-41312)

---

### HellaSwag (10-shot)

| Model | acc (%) | acc_norm (%) | Source |
|-------|---------|-------------|--------|
| Uniform | 54.08 ± 0.50 | **73.08** ± 0.44 | `llama3b_uniform_hellaswag` |
| Adaptive | 53.63 ± 0.50 | **72.49** ± 0.45 | `llama3b_adaptive_lm_eval` (first run) |
| **Δ** | **-0.45** | **-0.60** | |

---

### 0-shot Downstream (uniform only)

| Benchmark | acc (%) | acc_norm (%) | Source |
|-----------|---------|-------------|--------|
| ARC-Easy | 72.18 ± 0.92 | 68.43 ± 0.95 | `qwen_uniform_downstream` |
| HellaSwag | 52.77 ± 0.50 | 70.46 ± 0.46 | `qwen_uniform_downstream` |
| PIQA | 76.22 ± 0.99 | 76.93 ± 0.98 | `qwen_uniform_downstream` |
| WinoGrande | 68.90 ± 1.30 | — | `qwen_uniform_downstream` |

> **Adaptive 模型缺少 0-shot ARC/PIQA/WinoGrande 评测。**

---

### 总结

| Metric | Uniform | Adaptive | Δ | 方向 |
|--------|---------|----------|---|------|
| PPL | 10.38* | 10.58* | +0.20* | ❌ adaptive worse |
| MMLU (5-shot) | 51.85% | 53.42% | +1.57pp | ✅ adaptive better |
| HellaSwag (10-shot, acc_norm) | 73.08% | 72.49% | -0.60pp | ❌ adaptive worse |

\* PPL eval 配置不一致，需要用相同数据重新评测才能公平比较。

---

### 需要注意的问题

1. **PPL eval 不一致**: uniform 用 2000 docs (1.5M tokens)，adaptive 用 4.0M tokens。需要统一 eval 才能比较。
2. **memory.md PPL=10.53 来源不明**: 服务器上没有对应文件，可能是某次未保存的 eval 或记录错误。
3. **Adaptive 缺少 0-shot downstream**: ARC/PIQA/WinoGrande 只有 uniform 的结果。
4. **Registry 结论**: adaptive 标记为 `negative`，uniform 标记为 `success`。Adaptive 训练过程中 process died 5 次，W&B 缺失。
5. **第三个脚本 `run_llama3b_adaptive_tau09_seed42.sh`**: 使用 τ=0.9, ρ=0.2 的配置（数据为 `scored_data_rho02.jsonl`），但 registry 中没有对应实验记录，可能未运行。

---
