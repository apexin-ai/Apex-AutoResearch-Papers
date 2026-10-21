# debug check t1 final results

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_debug_check_t1_final_results_20260518T051044_result.json`
- **Structured JSON:** [`99d37afd4355bb5328dd.json`](../../sessions/99/99d37afd4355bb5328dd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

**进程状态**：卡死。PID 657872 仍在运行但挂起（sleeping on futex, GPU 0%, log 自 13:10 无更新，已 1.5+ 小时无进展）。

**完成了 10/20 seeds，无 JSON/PDF 输出**（Phase 3 统计和保存未执行）。

### 已获取的数据

| 指标 | 值 |
|---|---|
| **Baseline R2** | 0.5169 |
| **Dominant-24 R2** | 0.5592 |
| **Dominant-24 R2 increase** | 0.0423 |

**10 个 random-24 seeds**：

| seed | R2 | R2 increase |
|---|---|---|
| 0 | 0.5896 | 0.0727 |
| 1 | 0.5845 | 0.0676 |
| 2 | 0.5811 | 0.0642 |
| 3 | 0.5893 | 0.0724 |
| 4 | 0.6040 | 0.0871 |
| 5 | 0.6021 | 0.0852 |
| 6 | 0.6028 | 0.0859 |
| 7 | 0.5748 | 0.0579 |
| 8 | 0.5897 | 0.0728 |
| 9 | 0.6185 | 0.1016 |

**10-seed 统计（手算）**：
- Random mean increase: **0.0767**
- Random SD: ~0.0126
- Dominant-24 increase (0.0423) **低于所有 10 个 random subsets**
- z-score ≈ (0.0423 − 0.0767) / 0.0126 ≈ **−2.73**
- Percentile: **0%**（dominant-24 是最低的）

### 关键发现

Dominant-24 ablation 的 R2 increase（0.0423）**显著低于** random-24 subsets（均值 0.0767）。方向与预期相反：dominant heads ablation 后 action prediction 改善幅度比随机 subset 更小，不是更大。

### 建议

进程需要 kill 并处理。已有 10 个 seeds 的数据已经足够得出结论（z = −2.73），是否需要我：
1. Kill 卡死进程，用已有 10-seed 数据手动生成 JSON + 图？
2. Kill 后重跑完整 20 seeds？

---
