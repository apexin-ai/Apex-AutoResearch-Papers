# code exp002 pilot

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp002_pilot_20260521T084707_result.json`
- **Structured JSON:** [`951c2659ea434a353945.json`](../../sessions/95/951c2659ea434a353945.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全量 exp-002 已成功启动并稳定运行中。

## 总结

**Phase 1: Pilot 验证 — 通过**

| Benchmark | Records | Accuracy | Extraction | 状态 |
|-----------|---------|----------|------------|------|
| MMLU | 2,000 | 70.6% | 100% | ✓ |
| GSM8K | 600 (v2) | 64.5% | 100% | ✓ (修复后) |
| ARC | 2,000 | 81.5% | 98% | ✓ |
| HellaSwag | 2,000 | 68.5% | 100% | ✓ |

**关键修复**：GSM8K 添加了 stop sequences（`\nQ:`, `\nQuestion:`, `\nProblem:`, `\n\n## `），防止模型在回答后继续生成新题目导致答案提取错误。准确率从 30% → 64.5%。

**Phase 2: 全量启动 — 运行中**

- 4 GPU 并行，按模型分 shard：
  - GPU 0: Qwen3-8B (14/288 MMLU done)
  - GPU 1: Llama-3.1-8B (15/288 MMLU done)
  - GPU 2: Gemma-2-9B (12/288 MMLU done)
  - GPU 3: Mistral-7B (13/288 MMLU done)
- 每 GPU 跑 4 benchmarks 串行（mmlu → arc → hellaswag → gsm8k）
- **PID**: 133392
- **ETA**: ~2.7 小时（约 19:45 CST）
- 每 GPU 产出：288 conditions × 200 items × 4 benchmarks = 230,400 records
- 总产出：921,600 records

**监控命令**：
```bash
grep -c "Condition" results/exp002/gpu*_*.log   # 各GPU进度
grep "===" results/exp002/gpu*_*.log             # benchmark切换时间
```

---
