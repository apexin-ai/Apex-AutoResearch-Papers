# code olmo1b 10k cuda2

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_olmo1b_10k_cuda2_20260522T200147_result.json`
- **Structured JSON:** [`a155d58d6194b97a5768.json`](../../sessions/a1/a155d58d6194b97a5768.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已启动并注册完毕。

**状态汇总：**
- **exp_id**: `exp_olmo1b_10k`
- **PID**: 66415
- **GPU**: cuda:2（6GB 已占用，66% utilization）
- **Phase 1**: OLMo-1B continuation 生成 depth 1-5（10K docs，batch_size=32，~2.5s/batch）
- **Phase 2**: Qwen2.5-1.5B-Instruct cross-scoring（自动跟在 Phase 1 后执行）
- **日志**: `/tmp/exp_olmo1b_10k.log`
- **数据**: `data/olmo1b_c4_10k/`
- **结果**: `results/olmo1b_c4_10k/`

估计 Phase 1 每个 depth 约 15 分钟（313 batches × ~3s），5 个 depth 共约 75 分钟；Phase 2 feature extraction + analysis 约 30-40 分钟。总计约 2 小时。

---
