# analysis 14b max length truncation

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_14b_max_length_truncation_20260518T171951_result.json`
- **Structured JSON:** [`032a4d2c4d602e59c6be.json`](../../sessions/03/032a4d2c4d602e59c6be.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
=== Token 长度分布 ===
样本数: 3027
mean: 864, median: 813, p90: 1243, p95: 1419, p99: 1814, max: 2977

=== 截断比例 ===
max_length=2048: 0.5% 截断 (14/3027 样本)
max_length=3072: 0.0% 截断 (0/3027 样本)
max_length=4096: 0.0% 截断 (0/3027 样本)

=== 决策 ===
最终 max_length: 2048
gradient_checkpointing: 否（不需要）
理由: 截断比例仅 0.5%，远低于 15% 阈值。被截断的 14 个样本均为高关系数文档（平均 48 relations vs 正常 12.4），是极端尾部。2048 对 14B 完全安全。

=== 脚本修改 ===
修改了: /root/autodl-tmp/freige/scripts/seed_expansion/sft_14b.sh
变更: 仅在头部注释中添加了截断分析数据（max_length 和其他训练参数不变）
eval_14b.sh: 无需修改（max_new_tokens=1024 仅控制生成长度，与 max_length 无关）
```

---
