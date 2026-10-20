# code kv bench 001

**When Does KV Redundancy Predict MLP Sparsity? Architecture Dependence of Cross-Axis Signals in Reasoning Inference** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_kv-bench-001_20260512T015136_result.json`
- **Structured JSON:** [`37ca21f500d0fb6094c6.json`](../../sessions/37/37ca21f500d0fb6094c6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验 kv-bench-001 已提交。tmux session `kv-bench-001` 运行中。

**状态总结：**
- 脚本：`src/kv_eviction/run_kv_benchmark.py` — 自包含，修复了原框架代码的所有问题（DynamicCache API、policy返回值、position_ids）
- 配置：10 段文本 × 512 max tokens，3 budgets (30%/50%/70%) × 3 policies (CARC-KV/H2O/StreamingLLM) + baseline
- 预估耗时：~6-8 分钟
- 结果输出：`results/kv_eviction/kv_bench_001_results.json`
- 日志：`results/kv_eviction/kv_bench_001.log`
- 查看进度：`tmux attach -t kv-bench-001` 或 `tail -f results/kv_eviction/kv_bench_001.log`

---
