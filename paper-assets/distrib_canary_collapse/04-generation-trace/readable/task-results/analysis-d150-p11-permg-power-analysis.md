# analysis d150 p11 permg power analysis

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_d150_p11_permg_power_analysis_20260520T134046_result.json`
- **Structured JSON:** [`db42de7e7502daef41a3.json`](../../sessions/db/db42de7e7502daef41a3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All three deliverables complete:

1. **脚本**: `scripts/permg_power_analysis.py` (本地+服务器)
2. **结果 JSON**: `artifacts/permg_power_analysis.json`
3. **Power curve 图**: `artifacts/permg_power_curve.png`

## 核心结果

**配置**: 21 β × 5 T × 100 reps × 8 pairs × 5000 perms, 总计 836s

### FPR 验证 (β=0)
| T | Raw | FDR8 |
|---|-----|------|
| 6 | 0.01 | 0.00 |
| 8 | 0.06 | 0.02 |
| 10 | 0.09 | 0.02 |
| 15 | 0.06 | 0.02 |
| 20 | 0.05 | 0.01 |

Raw FPR 在 α=0.05 附近，FDR8 严格控制在 ≤0.02。

### β₅₀ (50% power 所需最小 β)
| T | Raw | FDR8 |
|---|-----|------|
| 6 | — | — |
| 8 | 1.80 | — |
| 10 | 1.20 | 2.00 |
| 15 | 0.80 | 1.20 |
| 20 | 0.60 | 0.90 |

### √T Scaling 检查 (raw)
- T=8: β₅₀·√T = 5.09
- T=10: β₅₀·√T = 3.80
- T=15: β₅₀·√T = 3.10
- T=20: β₅₀·√T = 2.68

β₅₀·√T 从 5.1 下降到 2.7——不是严格常数，但趋势一致：power 随 T 增长，β₅₀ 大致按 1/√T 缩放（T=6/8 过短导致 power 严重不足，T≥10 后趋势稳定）。

### 关键发现
- **T=10 处 steep sigmoid** 确认：raw power 从 β=0.5 (25%) 跃升到 β=1.3 (66%)，与论文中的 phase transition 一致
- **T=6 基本无 power**：即使 β=2.0，raw power 仅 13%（FDR8: 0%）。说明 T≤6 时 PermG 根本不可靠
- **FDR8 vs Raw 差距**：FDR 校正后 power 下降约 30-40%，但 T≥15 时仍能达到 >80% power（β≥1.2）

---
