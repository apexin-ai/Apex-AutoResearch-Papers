# analysis logprob rho inconsistency

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_logprob_rho_inconsistency_20260514T122249_result.json`
- **Structured JSON:** [`af02718854821be55aa0.json`](../../sessions/af/af02718854821be55aa0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

**NER logprob ρ 差异的根因是温度 (T)**，不是实例子集、N 采样数或归一化方式。

### 因子分解（NER ρ gap = 0.174）

| 因子 | 贡献 | 占比 | 判定 |
|------|------|------|------|
| **(b) 温度 T=0.7 vs T=1.0** | **+0.129** | **74%** | **主因** |
| (a) 实例子集 200 vs 529 | +0.039 | 22% | 次要 |
| (c) N=16 vs N=8 | +0.007 | 4% | 可忽略 |
| (d) 归一化方式 | 0 | 0% | 排除（两者相同） |

### 关键证据

- **同 200 实例**，exp-001 (N=16,T=0.7) ρ=0.314 vs exp-012 (N=8,T=1.0) ρ=0.179，差距 +0.135
- **仅改 N**（exp-001 内从 N=16 子采样到 N=8），ρ 仅从 0.314 降到 0.308，差 +0.007
- 因此 T 效应 ≈ 0.135 - 0.007 = **0.129**

### 机制

T=1.0 使 logprob 分布更宽（range 0.153 vs T=0.7 的 0.098），采样多样性带来的噪声稀释了 logprob 与 F1 的相关性。

### 建议

统一 logprob baseline 比较时，应固定 T。如果要在 T=1.0 数据上报告 logprob baseline，ρ≈0.14 是正确的数字。exp-001 的 ρ=0.314 不可直接对比，因为 T=0.7 的 logprob 信号本身更强。

诊断脚本和完整 JSON 已保存到服务器 `output/logprob_diagnosis/`。

---
