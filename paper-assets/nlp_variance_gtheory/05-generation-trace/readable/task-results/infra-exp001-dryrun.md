# infra exp001 dryrun

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_exp001_dryrun_20260520T215419_result.json`
- **Structured JSON:** [`f200b45d0d5a6829b23b.json`](../../sessions/f2/f200b45d0d5a6829b23b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有验证完成。汇总结果：

```
代码部署：成功
设计矩阵：5184 行（Llama 条件 1296 行）
数据生成：200 items, 10 subjects, 4 orderings
Dry-run：50 records (10 conditions × 5 items), 所有字段 ✓
enforce_eager：confirmed（vLLM 日志明确显示 enforce_eager=True）
性能：avg 59.2ms/condition, VRAM 14.99/94.97 GB（模型权重），gpu_memory_utilization=0.90
准确率：13/50 (26.0%)
问题：
  - Llama-3.1-8B-Instruct 是 gated model，HF 直接下载需要 token。已通过 ModelScope 下载到本地路径 /root/autodl-tmp/.hf_cache/LLM-Research/Meta-Llama-3___1-8B-Instruct
  - 设计矩阵中 model 列需要使用本地路径而非 HF repo ID（已创建 design_matrix_exp001_llama_local.csv）
  - 正式实验需要：(1) 配置 HF token 或 (2) 所有 gated 模型都用 ModelScope 下载后使用本地路径
  - 准确率偏低（26%），可能因为 dry-run 只取了前 5 个 items（都来自 abstract_algebra，较难的 subject）
```

---
