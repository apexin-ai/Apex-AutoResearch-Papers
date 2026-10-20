# exp deberta c4 westd

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_deberta-c4-westd_20260519T192827_result.json`
- **Structured JSON:** [`cf52fd3b1dbe80ed9584.json`](../../sessions/cf/cf52fd3b1dbe80ed9584.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练已提交并确认 RUNNING。

**报告：**

| 项目 | 详情 |
|------|------|
| exp_id | `exp_deberta_c4` |
| 服务器 | westd-42896, cuda:0 |
| PID | 130789 |
| C4 configs | `exp_14b_c4` (depth 0-5, 30000 样本, 5000 docs), `exp_32b_c4` (depth 0-4, 25000 样本, 5000 docs) |
| 总数据量 | 55,000 样本 |
| 模型 | DeBERTa-v3-base (184.4M params) |
| 训练设置 | 5-fold GroupKFold, 3 epochs, lr=2e-5, batch=16, max_len=512, AMP |
| 输出 | `results/exp_deberta_c4/` (per-config JSON + OOF .npz + summary) |
| 预估时间 | ~60-90 分钟（2 configs × 5 folds × 3 epochs） |
| 日志 | `results/exp_deberta_c4/train.log` |

注意：服务器上只有 `exp_14b_c4` 和 `exp_32b_c4` 两个 C4 数据目录，未发现任务中提到的 mvp_pilot / exp_002_pythia / exp_017_qwen_cont 等目录。

---
