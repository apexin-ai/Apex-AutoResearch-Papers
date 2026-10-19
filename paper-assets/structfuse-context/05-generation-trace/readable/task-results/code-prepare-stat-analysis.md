# code prepare stat analysis

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prepare_stat_analysis_20260514T150704_result.json`
- **Structured JSON:** [`f9fa299341dbfa7ef14a.json`](../../sessions/f9/f9fa299341dbfa7ef14a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本已创建并验证通过。

**结果**：`/root/structfuse/analysis/m2_stat_analysis.py` 已部署到服务器，dry-run 成功。当前 3/18 runs 有数据（qwen/random_s42 完成、qwen/random_s43 和 starcoder/random_s42 进行中），统计检验因 embedding_distance 和 dataflow_aware 数据尚未到位而跳过，符合预期。

脚本功能：
- `--status-only`：仅查看数据可用性
- 默认运行：数据可用时自动执行 paired t-test、bootstrap CI、Cohen's d、encoder×strategy 交互对比，输出格式化表格 + JSON
- 缺失 run 自动跳过，不会报错

---
