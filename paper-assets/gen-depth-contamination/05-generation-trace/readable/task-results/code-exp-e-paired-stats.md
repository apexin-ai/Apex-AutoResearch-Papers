# code exp E paired stats

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_E_paired_stats_20260515T104232_result.json`
- **Structured JSON:** [`768df5e61f80f9c753d0.json`](../../sessions/76/768df5e61f80f9c753d0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

JSON 输出格式正确。结果汇总：

**MMLU（6 main strategies, 15 pairs, Holm-Bonferroni）：**
- 11/15 pairs 显著 (p_corr < 0.05)
- binary-ours 显著优于所有其他策略
- binary-drayson 显著优于 dsir、no-filter
- 最大 effect size: binary-ours vs dsir (d=11.0)

**HellaSwag（同上）：**
- 9/15 pairs 显著
- binary-ours 和 graduated_a0.9 并列最高 (0.6701)，两者无显著差异 (p=1.0)
- binary-ours/graduated_a0.9 显著优于 surprisal、dsir、no-filter
- 最大 effect size: graduated_a0.9 vs dsir (d=8.98)

**策略均值排序：**
| Strategy | MMLU | HellaSwag |
|---|---|---|
| binary-ours | 0.5941 | 0.6701 |
| binary-drayson | 0.5913 | 0.6691 |
| surprisal | 0.5894 | 0.6641 |
| graduated_a0.9 | 0.5892 | 0.6701 |
| graduated_a0.7 | 0.5892 | 0.6695 |
| graduated_a0.5 | 0.5880 | 0.6687 |
| graduated_a0.3 | 0.5877 | 0.6669 |
| graduated_a0.1 | 0.5873 | 0.6640 |
| dsir | 0.5869 | 0.6631 |
| no-filter | 0.5865 | 0.6638 |

脚本和 JSON 都已就位：
- 脚本: `scripts/exp_E_paired_stats.py`
- 输出: `artifacts/exp_E_paired_stats.json`（含 per-seed 数据、6-strategy 主比较、graduated alpha sweep 比较、key_findings）

---
