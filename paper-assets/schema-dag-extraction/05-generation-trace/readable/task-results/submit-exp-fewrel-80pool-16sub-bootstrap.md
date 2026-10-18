# submit exp fewrel 80pool 16sub bootstrap

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_submit_exp_fewrel_80pool_16sub_bootstrap_20260516T015642_result.json`
- **Structured JSON:** [`105913cd0e9e67f95f1d.json`](../../sessions/10/105913cd0e9e67f95f1d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已成功提交并正常运行。汇报如下：

**实验状态**
- **PID**: 347426 (nohup 后台进程)
- **日志**: `/tmp/exp_80pool_16sub.log`
- **Registry**: `exp_fewrel_80pool_16sub_bootstrap` → RUNNING

**进展**
- vLLM Qwen3-32B-FP8 加载完成 (32.04 GiB, 30.6s)
- 推理已启动，前 3 个 batch 正常（~4-8s/batch）
- **BCS 范围**: [0.4578, 0.6836], mean=0.5570, n=100

**脚本改动**
- 在 `run_analysis` 中增加了 `scipy.stats.linregress(bcs, accs)` 线性回归
- 1000 次 bootstrap 重采样斜率 95% CI
- 输出到 `bootstrap_ci.json` 的 `regression_slope` 字段

**预计完成时间**
- 100 batches × ~5s/batch ≈ 8-10 分钟（约 10:10 UTC）
- extract 结束后自动运行 analyze 阶段

---
