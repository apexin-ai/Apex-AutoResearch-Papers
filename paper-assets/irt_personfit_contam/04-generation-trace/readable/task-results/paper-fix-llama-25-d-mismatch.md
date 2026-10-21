# paper fix llama 25 d mismatch

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_fix-llama-25-d-mismatch_20260524T101634_result.json`
- **Structured JSON:** [`7f18c4cf04089fe8e248.json`](../../sessions/7f/7f18c4cf04089fe8e248.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Push 成功。总结：

---

### 1. d=-1.99 来源追溯
d=-1.99 是 **Llama 50% contamination 的 seed 3**（appendix.tex:441），被错误地 copy-paste 到 Table 1 的 25% 列。

### 2. 正确值
从 appendix tab:llama_multiseed，25% 三个种子为 -3.16, -2.28, -2.24。  
**multi-seed mean = -2.56, SD = 0.52**。  
同时 15% 和 50% 也有 multi-seed 数据，全部切换为 mean±SD 格式以与 Qwen 一致。

### 3. 所有改动

| 文件 | 行号 | 旧值 | 新值 |
|------|------|------|------|
| results.tex:10 | range下界 | \|d\|=1.99 (Llama 25%) | \|d\|=2.30 (Llama 50%) |
| results.tex:10 | Llama序列 | 2.11/1.99/2.33 | 2.80/2.56/2.30 |
| results.tex:15 | range | 1.99--7.44 | 2.30--7.44 |
| results.tex:19 | caption | Qwen-only multi-seed | both Qwen+Llama multi-seed |
| results.tex:29 | Table 1 Llama行 | -2.11 [CI] / -1.99 [CI] / -2.33 [CI] | -2.80 (±0.60) / -2.56 (±0.52) / -2.30 (±0.30) |
| results.tex:33 | footnote | Qwen only | Qwen and Llama |
| results.tex:40 | heatmap caption | single-seed values | multi-seed means where available |
| results.tex:100 | Table 2 footnote | "4--7 not retained" | "4 vectors from seeds 4--7 not retained" |
| results.tex:165 | dose-response | 2.11→1.99→2.33 | 2.80→2.56→2.30 |
| introduction.tex:39 | PSN-IRT引用 | "with pre-calibrated 4PL...from PSN-IRT \citep{}" | "with PSN-IRT parameters" |
| limitations.tex:4 | multi-seed | "(available for Qwen)" | "(available for Qwen and Llama)" |
| gen_fig_heatmap.py:35 | Llama data | [nan,2.11,1.99,2.33,...] | [nan,2.80,2.56,2.30,...] |
| gen_fig_theta_scatter.py | Llama 15%/25%/50% | single-seed with bootstrap CI | multi-seed mean with ±SD bars |

### 4. 编译确认
16 页 PDF，主文（含 limitations）结束在第 8 页。

### 5. 匿名 repo push
`57ac2ce..892deca main -> main` ✓  
https://github.com/anonymous-nlp-2026-2/irt_personfit_contam

---
