# code cross scale convergence

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_cross_scale_convergence_20260519T045618_result.json`
- **Structured JSON:** [`253fc2b184586e9bbb1f.json`](../../sessions/25/253fc2b184586e9bbb1f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有输出已生成。以下是完整结果总结：

**输出文件**（均在 `/root/entrainment_gated_ft/analysis/`）：
- `cross_scale_convergence.py` (9.9K) - 分析脚本
- `cross_scale_convergence.pdf` (34K) - 2×3 subplot 图表
- `cross_scale_convergence.png` (299K) - 同上 PNG 版
- `cross_scale_summary.csv` (6.1K) - 完整数据表

---

**Spearman 相关性 (arch_std vs attn_layers)**：

| Scale | Benchmark | rho | p-value |
|-------|-----------|-----|---------|
| 1.3B | lambada_acc | **-1.000** | 1.4e-24 |
| 1.3B | arc_easy_norm | -0.700 | 0.188 |
| 1.3B | mmlu_acc | -0.700 | 0.188 |
| 1.3B | hellaswag_norm | 0.300 | 0.624 |
| 1.3B | arc_challenge_norm | 0.600 | 0.285 |
| 1.3B | winogrande_acc | 0.100 | 0.873 |
| 340M | arc_challenge_norm | **-0.900** | **0.037** |
| 340M | lambada_acc | -0.500 | 0.391 |
| 340M | arc_easy_norm | -0.500 | 0.391 |
| 340M | mmlu_acc | -0.300 | 0.624 |
| 340M | hellaswag_norm | 0.400 | 0.505 |
| 340M | winogrande_acc | 0.800 | 0.104 |

---

**关键发现**：

| Scale | Benchmark | Std: 0→8 attn | 趋势 | 变化幅度 |
|-------|-----------|---------------|------|----------|
| 1.3B | lambada_acc | 0.0240→0.0049 | CONVERGE | -79.4% |
| 1.3B | arc_easy_norm | 0.0100→0.0013 | CONVERGE | -87.0% |
| 1.3B | mmlu_acc | 0.0092→0.0040 | CONVERGE | -56.0% |
| 340M | mmlu_acc | 0.0071→0.0025 | CONVERGE | -64.5% |
| 340M | lambada_acc | 0.0246→0.0151 | CONVERGE | -38.7% |
| 340M | arc_challenge_norm | 0.0137→0.0088 | CONVERGE | -35.6% |
| 340M | winogrande_acc | 0.0043→0.0131 | DIVERGE | +206.4% |
| 1.3B | arc_challenge_norm | 0.0096→0.0132 | DIVERGE | +38.3% |

**核心观察**：
1. **LAMBADA 在 1.3B 上展现完美的单调收敛**（rho=-1.0），3 种架构随 attention 增多趋于一致
2. **收敛效应在 1.3B 比 340M 更强**（lambada 79% vs 39%），符合 scale-dependent convergence 假设
3. 部分 benchmark（winogrande, arc_challenge）呈 diverge 模式，可能因为任务特性不同
4. 340M MMLU 接近随机（~0.25），收敛数据噪声大

---
