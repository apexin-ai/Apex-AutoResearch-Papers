# analysis exp 025 n ablation

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_025_n_ablation_20260516T121619_result.json`
- **Structured JSON:** [`1e59e3fde9b4e9ced515.json`](../../sessions/1e/1e59e3fde9b4e9ced515.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果汇总：

**Rank32 (ft_002_v2, N=16 source)**:
| N | Degen% | Oracle_gap | Best signal | Best_Δ vs greedy |
|---|--------|------------|-------------|------------------|
| 2 | 53.0 | +4.0pp | LP | -1.67pp |
| 4 | 30.7 | +9.7pp | LP | -0.30pp |
| 8 | 18.7 | +13.9pp | LP | +0.15pp |
| 16 | 11.5 | +17.5pp | FK | +0.27pp |

**Rank8 (exp-023, N=8 source)**:
| N | Degen% | Oracle_gap | Best signal | Best_Δ vs greedy |
|---|--------|------------|-------------|------------------|
| 2 | 38.2 | +2.2pp | LP | -4.48pp |
| 4 | 15.7 | +10.3pp | LP | -2.22pp |
| 8 | 7.2 | +16.0pp | LP | -0.47pp |

关键发现：
- LP 在所有 N 值下最鲁棒，是最先转正的信号
- N=2 时 SJ=FK=EM（仅1对比较，退化为 binary）
- rank32 需要 N≥8 才能 selection > greedy；rank8 在 N=8 时仍为负
- 输出路径：`/root/autodl-tmp/struct_self_consist_ie/output/exp_025_n_ablation/`

---
