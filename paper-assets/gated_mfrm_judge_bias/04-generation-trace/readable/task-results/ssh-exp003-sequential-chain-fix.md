# ssh exp003 sequential chain fix

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_exp003_sequential_chain_fix_20260522T142817_result.json`
- **Structured JSON:** [`3800eae80d736055d39b.json`](../../sessions/38/3800eae80d736055d39b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已稳定运行：

| 指标 | 结果 |
|------|------|
| **PID** | 143769 |
| **GPU 0** | 62% utilization, 667 MiB（vs 之前 73.5GB×4） |
| **GPU 1-3** | 空闲，符合 `CUDA_VISIBLE_DEVICES=0` |
| **MCMC 速度** | ~85-93 it/s（sequential chain on single GPU） |
| **进度** | mfrm_only chain 1 已跑到 45%，无 error |
| **数据加载** | 5661 条观测，9 个 judge，正常 |

chain 1 的 warmup 2000 + sample 4000 = 6000 步，当前 ~87 it/s ≈ 69s/chain，4 chains ≈ 4.6min per method。3 个 MCMC method 总计约 15min 完成。无 OOM 风险。

---
