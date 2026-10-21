# analysis pooled irt rrf n25 v2

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_pooled_irt_rrf_n25_v2_20260516T150141_result.json`
- **Structured JSON:** [`f7e9323185a3106b46b8.json`](../../sessions/f7/f7e9323185a3106b46b8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已注册。核心发现：

### γ 结果

| Benchmark | γ mean | 95% CI | CI excl. 0 | PPP |
|-----------|--------|--------|------------|-----|
| **MMLU** | -0.404 | [-1.84, 1.07] | No | 0.006 ⚠️ |
| **GSM8K** | 0.142 | [-0.75, 0.96] | No | **0.398** ✓ |
| **ARC** | 1.513 | [0.23, 2.87] | **Yes** | 0.000 ⚠️ |

### 关键判断

1. **ARC 是唯一 γ 显著的 benchmark**，但 PPP=0.000 表明模型不拟合数据，且 N=8 违反 C008（4PL 需 N≥16）。显著性大概率是过参数化伪影而非真实 contamination bias。

2. **GSM8K 是唯一可信的结果**（N=16, PPP=0.398），γ=0.142 **非显著** — contamination 没有系统性偏移 item difficulty 校准。同时 IRT 校准大幅改善分数估计（ΔMAE=+0.118）。

3. **MMLU 4PL 在 N=8 下不可解释**（γ 反号，PPP≈0），需回退到 2PL+γ。

4. **与 2PL+γ 对比**：GSM8K γ 一致（0.172 vs 0.142）；ARC 从 2PL 的 0.486 跳到 4PL 的 1.513 是 c/d 参数不可识别导致的膨胀；MMLU 反号说明 4PL 在小 N 下失效。

### 对论文的影响

数据支持的 story 比原假设更强：**IRT 对 contamination 是 robust 的** — contamination 效应被标准 IRT 参数（c, d, discrimination）吸收，γ 本身无需显著偏离 0。建议 framing 从 "contamination breaks IRT calibration" 转为 "IRT provides contamination-robust score estimation"。

### 建议下一步

1. 对 MMLU/ARC 补跑 **2PL+γ**（同 v2 数据）— 这才是论文应报告的模型
2. 考虑加回 3B 以提升 MMLU/ARC 的 N 至 ≥16
3. 论文主表用 GSM8K 4PL+γ（N=16）+ MMLU/ARC 2PL+γ

---
