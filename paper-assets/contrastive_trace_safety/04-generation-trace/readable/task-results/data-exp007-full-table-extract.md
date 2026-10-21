# data exp007 full table extract

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_exp007_full_table_extract_20260517T012957_result.json`
- **Structured JSON:** [`d3ebdc690e7175f306d9.json`](../../sessions/d3/d3ebdc690e7175f306d9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据提取完成。额外字段：`precp_fpr_step`（step-level FPR）和 `lead_mean`（平均提前量）。

### R1-32B
| W | bal_acc | precision | coverage | precp_fpr_trace | precp_fpr_step | lead_mean |
|---|---------|-----------|----------|-----------------|----------------|-----------|
| 1 | 0.7182 | 0.5490 | 0.8000 | 0.2764 | 0.3203 | 12.88 |
| 3 | 0.7252 | 0.5600 | 0.8000 | 0.2576 | 0.3064 | 11.38 |
| 5 | 0.7309 | 0.5750 | 0.7500 | 0.2393 | 0.2841 | 11.07 |
| 10 | 0.7371 | 0.6093 | 0.7000 | 0.1891 | 0.2340 | 10.79 |
| 15 | 0.7207 | 0.5907 | 0.7000 | 0.2089 | 0.2451 | 10.86 |
| 20 | 0.6961 | 0.5628 | 0.6500 | 0.2193 | 0.2618 | 9.62 |
| 25 | 0.7028 | 0.5662 | 0.7000 | 0.2282 | 0.2646 | 10.71 |

### QwQ-32B
| W | bal_acc | precision | coverage | precp_fpr_trace | precp_fpr_step | lead_mean |
|---|---------|-----------|----------|-----------------|----------------|-----------|
| 1 | 0.7298 | 0.5435 | 0.7895 | 0.1850 | 0.2276 | 19.73 |
| 3 | 0.7452 | 0.5647 | 0.7368 | 0.1750 | 0.2141 | 20.64 |
| 5 | 0.7610 | 0.5733 | 0.7368 | 0.1795 | 0.2168 | 20.07 |
| 10 | 0.7469 | 0.5714 | 0.7368 | 0.1707 | 0.2073 | 18.43 |
| 15 | 0.7412 | 0.5816 | 0.6842 | 0.1605 | 0.1911 | 15.77 |
| 20 | 0.7542 | 0.6024 | 0.6316 | 0.1567 | 0.1789 | 15.75 |
| 25 | 0.7624 | 0.6177 | 0.5789 | 0.1476 | 0.1694 | 14.91 |

### R1-8B (参照)
| W | bal_acc | precision | coverage | precp_fpr_trace | precp_fpr_step | lead_mean |
|---|---------|-----------|----------|-----------------|----------------|-----------|
| 1 | 0.7783 | 0.6926 | 0.7209 | 0.1037 | 0.0965 | 13.84 |
| 3 | 0.7902 | 0.7228 | 0.6977 | 0.0988 | 0.0850 | 12.07 |
| 5 | 0.7810 | 0.7258 | 0.6512 | 0.0913 | 0.0809 | 8.25 |
| 10 | 0.7925 | 0.7431 | 0.5581 | 0.0865 | 0.0761 | 10.04 |
| 15 | 0.8017 | 0.7767 | 0.5116 | 0.0701 | 0.0639 | 7.23 |
| 20 | 0.8072 | 0.7862 | 0.5349 | 0.0661 | 0.0612 | 7.43 |
| 25 | 0.8095 | 0.8216 | 0.4884 | 0.0545 | 0.0483 | 8.14 |

**观察**：R1-8B 在所有 W 上表现最好（高 bal_acc + 低 FPR）。两个 32B 模型表现相近，但 QwQ-32B 的 FPR 显著低于 R1-32B，且 lead_mean 更大（提前检测更早）。三个模型都呈现 W 增大时 coverage 下降、precision 上升的 trade-off。R1-32B 最优 W=10，QwQ-32B 最优 W=5 或 W=25（取决于优化目标）。

---
