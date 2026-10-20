# analysis d073 s2b twv 6lf rerun

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_d073-s2b-twv-6lf-rerun_20260516T031738_result.json`
- **Structured JSON:** [`3781c1cdbca39b700f64.json`](../../sessions/37/3781c1cdbca39b700f64.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成，artifact 已注册，registry 已更新。以下是完整结果。

---

## 6-LF TLM vs MV 对比表

| Method | Gold F1 | Gold Acc | Conf≥2 F1 | Conf≥2 Agr | Conf≥3 F1 | Conf≥3 Agr |
|---|---|---|---|---|---|---|
| **6-LF MV** | 0.7192 | 0.7530 | (base) | 1.000 | (base) | 1.000 |
| 6-LF TWV σ=1 | 0.7188 | 0.7517 | 0.9109 | 0.9215 | 0.9716 | 0.9743 |
| 6-LF TWV σ=2 | 0.7342 | 0.7683 | 0.9151 | 0.9257 | 0.9711 | 0.9737 |
| 6-LF TWV σ=3 | 0.7389 | 0.7733 | 0.9030 | 0.9155 | 0.9647 | 0.9679 |
| 6-LF TWV σ=5 | 0.7435 | 0.7783 | 0.8799 | 0.8963 | 0.9500 | 0.9543 |
| **6-LF HMM** | **0.7838** | **0.8217** | 0.8248 | 0.8531 | 0.9119 | 0.9206 |
| 6-LF lag-HMM | 0.7643 | 0.8017 | 0.8402 | 0.8637 | 0.9276 | 0.9351 |

## Delta vs 6-LF MV (Gold F1)

| Method | Δ Gold F1 |
|---|---|
| TWV σ=1 | -0.04pp |
| TWV σ=2 | +1.50pp |
| TWV σ=3 | +1.97pp |
| TWV σ=5 | +2.43pp |
| **HMM** | **+6.46pp** |
| lag-HMM | +4.51pp |

## C3 Claim 结论

**C3 需要重大修改。** 原始 C3 claim（"TWV/HMM/lag-HMM 不比 MV 好"）是 3-LF 低冲突（15%）条件下的局部结论，不是通用结论。

修改后的 C3：**TLM 价值取决于 LF 多样性。** 3 LF + 15% 冲突 → MV 足够；6 LF + 42% 冲突 → HMM-TLM 比 MV 提升 +6.46pp gold F1。这说明 TLM 的优势在于利用 LF 间的分歧信号——当 LF 高度一致时，temporal smoothing 无额外信息可用；当 LF 冲突显著时，HMM 的状态转移模型能有效消歧。

注意事项：3-LF conf≥2 数字来自 probe cross-eval（训练在 TLM 标签上，测试 MV conf≥2），而 6-LF conf≥2 是直接标签对齐，方法学不完全可比。Gold F1 对比是同口径的。

---
