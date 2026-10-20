# exp medium random50 seed42 check

**The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_medium_random50_seed42_check_20260514T015023_result.json`
- **Structured JSON:** [`5cd65f40285aeced6948.json`](../../sessions/5c/5cd65f40285aeced6948.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

## 实验结果报告

**状态**: 成功完成，8 代全部跑完。

### Gen 0-7 完整指标

| Gen | PPL | RankMe | kNN | Rare | Corr |
|-----|-----|--------|-----|------|------|
| 0 | 26.12 | 361.63 | 0.988 | 0.0346 | 0.0101 |
| 1 | 32.57 | 387.80 | 0.988 | 0.0277 | 0.0331 |
| 2 | 41.58 | 410.08 | 0.988 | 0.0214 | 0.0088 |
| 3 | 49.87 | 421.67 | 0.988 | 0.0182 | -0.0018 |
| 4 | 59.83 | 427.23 | 0.988 | 0.0161 | -0.0014 |
| 5 | 60.62 | 426.16 | 0.988 | 0.0144 | -0.0004 |
| 6 | 68.34 | 427.19 | 0.988 | 0.0134 | -0.0071 |
| 7 | **70.25** | 426.50 | 0.988 | 0.0128 | -0.0034 |

### 关键对比（Gen7 PPL）

| 方法 | Gen7 PPL | vs Random 50% |
|------|----------|---------------|
| **RGDS** | **82.84** | — |
| **Random 50%** | **70.25** | baseline |
| **Uncurated** | **91.66** | — |

Random 50% (70.25) < RGDS (82.84) < Uncurated (91.66)。随机丢弃 50% 数据反而比 RGDS 筛选和全量无筛选都好，PPL 更低。这说明 RGDS 的筛选策略在 Medium 规模上不如随机选择，且单纯减少数据量（50%）本身就能减缓 model collapse。

### Registry & Cron 更新
- Registry: metrics / conclusion=success / checkpoint_path / log_path / status=DONE 全部已更新
- Cron: medium_random50_seed42 监控已删除

---
