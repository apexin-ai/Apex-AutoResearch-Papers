# infra v4 corrected submit

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_v4-corrected-submit_20260513T225733_result.json`
- **Structured JSON:** [`689b9be4f865422feb2a.json`](../../sessions/68/689b9be4f865422feb2a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 4 个实验正常运行。

**产出报告：**

| # | exp_id | PID | GPU | Sparsity | Output Dir |
|---|--------|-----|-----|----------|------------|
| 1 | mvp_ii_profiling_v4a | 27684 | cuda:0 | 0.1 | profiling_output_v4a |
| 2 | mvp_ii_profiling_v4b | 28078 | cuda:1 | 0.2 | profiling_output_v4b |
| 3 | mvp_ii_profiling_v4c | 28447 | cuda:2 | 0.3 | profiling_output_v4c |
| 4 | mvp_ii_profiling_v4d | 28834 | cuda:3 | 0.4 | profiling_output_v4d |

**执行摘要：**

1. **旧进程清理**：发现并 kill 了旧 Worker 提交的 3 个错误实验（GPU 0/1/2 上运行多 sparsity levels：0.1,0.2 / 0.3,0.4,0.5 / 0.15,0.25）
2. **代码同步**：服务器代码是旧版本（无 `--sparsity_levels` CLI 参数），已上传本地最新版本（支持 `--sparsity_levels` 参数 + `DEFAULT_SPARSITY_LEVELS`）
3. **Bug 修复**：发现并修复 `interaction_index.py:330-331` 的 device mismatch（`kv_importance`/`head_importance` 在 CPU，attention 输出在 CUDA），添加 `.cpu()` 调用
4. **nvidia-smi 确认**：4 卡均有 ~25GB 显存占用，GPU 利用率 76-99%，v4a 已处理到 [6/50] 问题

---
