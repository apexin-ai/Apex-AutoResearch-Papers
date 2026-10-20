# diagnose exit129 batch

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exit129_batch_20260518T205926_result.json`
- **Structured JSON:** [`050ab7522d11ddf6bdd0.json`](../../sessions/05/050ab7522d11ddf6bdd0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 个实验全部有完整的 11 条记录（generation 0-10，即 10 轮训练 + 初始 baseline）。

---

### interv_react_s43_bf16
- **状态: FALSE ALARM (实际完成)**
- **证据**: log 尾部 "All metrics saved to results/intervention/reactive_d1_s43_bf16/all_metrics.json"；all_metrics.json 包含 11 条记录 (gen 0-10)
- **关键 metrics**:

| Gen | ppl | entropy | d1 | eff_rank | mauve | intervention |
|-----|---------|--------|--------|----------|--------|-------------|
| 0 | 27.68 | 3.2574 | 0.0917 | 48.3 | 0.0297 | No |
| 1 | 24.63 | 2.5202 | 0.0897 | 55.9 | 0.0301 | No |
| 2 | 38.71 | 2.3497 | 0.0750 | 64.7 | 0.0261 | **Yes (trigger)** |
| 3 | 17.38 | 2.8868 | 0.0697 | 53.9 | 0.0187 | Yes (α→0.0) |
| 4 | 17.00 | 2.8636 | 0.0873 | 54.4 | 0.0320 | Yes (α=0.0) |
| 5 | 16.72 | 2.8433 | 0.0876 | 55.1 | 0.0347 | Yes (α=0.0) |
| 6 | 16.74 | 2.8452 | 0.0874 | 56.0 | 0.0342 | Yes (α=0.0) |
| 7 | 16.62 | 2.8402 | 0.0882 | 57.6 | 0.0317 | Yes (α=0.0) |
| 8 | 16.56 | 2.8235 | 0.0889 | 58.5 | 0.0309 | Yes (α=0.0) |
| 9 | 16.51 | 2.8230 | 0.0892 | 59.6 | 0.0308 | Yes (α=0.0) |
| 10 | 16.51 | 2.8169 | 0.0887 | 59.9 | 0.0336 | Yes (α=0.0) |

Intervention 在 gen 2 触发（d1=0.075 < threshold 0.10），之后 α 降至 0.0，collapse 趋势被遏制。

---

### gen_gpt2m_a100_s43_bf16
- **状态: FALSE ALARM (实际完成)**
- **证据**: log 尾部 "All metrics saved to results/generalize/gpt2m_wiki_a100_s43_bf16/all_metrics.json"；all_metrics.json 包含 11 条记录 (gen 0-10)
- **关键 metrics**:

| Gen | ppl | entropy | d1 | eff_rank | mauve |
|-----|---------|--------|--------|----------|--------|
| 0 | 32.91 | 3.6021 | 0.1092 | 2.4 | 0.0318 |
| 1 | 25.14 | 3.0176 | 0.1101 | 2.5 | 0.0354 |
| 2 | 26.78 | 2.9256 | 0.0989 | 2.6 | 0.0354 |
| 3 | 32.26 | 2.9862 | 0.0920 | 2.7 | 0.0339 |
| 4 | 37.81 | 3.0175 | 0.0842 | 2.8 | 0.0256 |
| 5 | 42.11 | 3.0221 | 0.0813 | 2.9 | 0.0266 |
| 6 | 45.61 | 3.0180 | 0.0789 | 3.0 | 0.0250 |
| 7 | 48.73 | 3.0139 | 0.0764 | 3.1 | 0.0273 |
| 8 | 51.33 | 3.0132 | 0.0753 | 3.1 | 0.0210 |
| 9 | 53.63 | 3.0098 | 0.0739 | 3.2 | 0.0193 |
| 10 | 55.49 | 3.0035 | 0.0724 | 3.2 | 0.0227 |

GPT-2 medium 在 α=1.0 下展现明显 collapse：ppl 从 32.9→55.5，d1 从 0.109→0.072，eff_rank 始终极低（~2-3）。

---

### alpha_sweep_a060_s42_bf16
- **状态: FALSE ALARM (实际完成)**
- **证据**: log 尾部 "All metrics saved to results/alpha_sweep/a060_s42_bf16/all_metrics.json"；all_metrics.json 包含 11 条记录 (gen 0-10)
- **关键 metrics**:

| Gen | ppl | entropy | d1 | eff_rank | mauve |
|-----|---------|--------|--------|----------|--------|
| 0 | 27.68 | 3.2574 | 0.0914 | 48.3 | 0.0288 |
| 1 | 18.44 | 2.6459 | 0.0911 | 51.4 | 0.0291 |
| 2 | 19.05 | 2.5937 | 0.0755 | 55.8 | 0.0250 |
| 3 | 19.39 | 2.5895 | 0.0703 | 58.4 | 0.0223 |
| 4 | 19.64 | 2.5824 | 0.0680 | 59.6 | 0.0176 |
| 5 | 19.71 | 2.5896 | 0.0678 | 60.8 | 0.0170 |
| 6 | 19.82 | 2.6019 | 0.0674 | 62.9 | 0.0159 |
| 7 | 20.03 | 2.6059 | 0.0673 | 63.7 | 0.0141 |
| 8 | 20.13 | 2.6149 | 0.0670 | 64.7 | 0.0144 |
| 9 | 20.27 | 2.6245 | 0.0667 | 65.9 | 0.0133 |
| 10 | 20.27 | 2.6404 | 0.0663 | 65.9 | 0.0146 |

α=0.60 下 collapse 较 α=1.0 缓和，ppl 稳定在 ~20，但 d1 和 mauve 仍持续下降。

---

## 汇总

**3 个实验全部为 FALSE ALARM。** 每个都完成了完整的 10 generations 训练并成功写出 all_metrics.json。EXIT_CODE=129 均为 tmux session 清理导致的 SIGHUP，与此前 alpha_sweep_c4_a050_s42_bf16 的情况一致。

---
