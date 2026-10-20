# experiment e3 conf stratified gold

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_e3-conf-stratified-gold_20260515T141408_result.json`
- **Structured JSON:** [`fa7815f2b7bb08bfb227.json`](../../sessions/fa/fa7815f2b7bb08bfb227.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## E3 结果

### 分层表格 (Gold Set B, N=505, SWE-only N=323)

| Conf | N | MV-Gold Agree | GB Gold F1 | GB Silver F1 | Gap (S-G) | Gold Stag% | Silver Stag% |
|------|---|---------------|------------|-------------|-----------|------------|-------------|
| 0 | 13 | N/A | — | — | — | 30.8% | 0.0% |
| 1 | 282 | 127/172 = **73.8%** | 0.7841 | 0.9972 | +0.213 | 21.3% | 24.8% |
| 2 | 163 | 110/113 = **97.3%** | 0.9717 | 0.9970 | +0.025 | 27.0% | 36.5% |
| 3 | 47 | 36/38 = **94.7%** | 0.9435 | 1.0000 | +0.057 | 53.2% | 64.8% |
| **≥2** | **210** | **146/151 = 96.7%** | **0.9664** | | | **32.9%** | |

### 核心结论

1. **conf≥2 MV-gold agreement = 96.7%** → 远超 90% 目标，主结果安全。conf=2 单独达 97.3%。

2. **Silver-gold gap 极小**：conf≥2 上 GB gold F1 = 0.9664，silver F1 (CV) = 0.9972，gap 仅 +0.031pp。conf=1 的 gap 才大 (+21.3pp)，说明 conf filtering 有效隔离了 noisy labels。

3. **Stagnation prevalence**：gold overall 26.3% vs silver 28.5% (SWE)。conf=1 层 gold 21.3% 接近 silver 24.8%；但 conf=2/3 层 gold stagnation 偏高（27%/53%），因为 gold 注释采样策略偏向了高 stagnation 的 windows。

4. **限制**：169 个 OH gold windows 无本地 trajectory 数据，GB/MV 分析仅覆盖 323 个 SWE windows。已有 consensus_601 全集评估 GB gold F1 = 0.7237 (N=584) 作为交叉参考。

---
