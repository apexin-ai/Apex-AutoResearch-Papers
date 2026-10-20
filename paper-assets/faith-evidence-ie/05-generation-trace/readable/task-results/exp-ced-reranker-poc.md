# exp ced reranker poc

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_ced-reranker-poc_20260515T075539_result.json`
- **Structured JSON:** [`ee6e10af2573335a2cc4.json`](../../sessions/ee/ee6e10af2573335a2cc4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全量运行正常启动。首个 doc ~8.4s/it，预计生成阶段 ~2.3h，加上 CED scoring 约 ~3h 总计。

**进度汇报：**
- 脚本 `/root/autodl-tmp/freige/eval/ced_reranker.py` 已写好并部署
- Dry-run (2 docs) 通过，pipeline 正确
- 全量 985 docs 已在后台运行 (PID 178050)
- 生成速度 ~8.4s/doc (N=8, T=0.7, max_new_tokens=2048)
- 预计完成时间约 16:03 + 3h ≈ **19:00 UTC**
- 结果将保存到 `/root/autodl-tmp/eval_results/ced_reranker_poc/results.json`

需要我定期检查进度还是完成后再汇报？

---
