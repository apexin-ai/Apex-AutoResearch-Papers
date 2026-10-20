# exp plan008 multi domain seeds

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_plan008-multi-domain-seeds_20260515T181516_result.json`
- **Structured JSON:** [`4adf2dbffd34c781d813.json`](../../sessions/4a/4adf2dbffd34c781d813.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已启动，总结如下：

**Plan 008 Multi-Domain Seeds 实验状态**

| 阶段 | 状态 | 详情 |
|------|------|------|
| Phase 1: Seeds | ✅ 完成 | news 500, scientific 500, creative 500 |
| Phase 2: Generation | 🔄 运行中 | Pythia-2.8B on cuda:0, PID 234061 |
| Phase 3: Features | ⏳ 待执行 | 生成完成后自动开始 |
| Phase 4: Evaluation | ⏳ 待执行 | 特征提取后自动开始 |

**数据源**:
- news: CNN/DailyMail (`abisee/cnn_dailymail`)
- scientific: arXiv abstracts (`ccdv/arxiv-summarization`)
- creative: WritingPrompts (`euclaise/writingprompts`)

**预计总时长**: ~6.5 小时（generation ~5.5h + features/eval ~1h）

**监控命令**:
```bash
# 查看各域生成进度 (目标每域 2500 records)
wc -l /root/gen-depth-fingerprint/data/pythia-2.8b-{news,scientific,creative}/generations_shard0.jsonl

# 查看日志
tail -20 /tmp/plan008_full.log

# 检查进程
ps -p 234061 -o pid=
```

脚本支持断点续传，即使中断也可重新运行 `python multi_domain_seeds.py --phase all` 从断点继续。最终结果输出到 `/root/gen-depth-fingerprint/results/multi_domain_results.json`。

---
