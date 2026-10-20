# check eval final

**rl active probe fl** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_eval-final_20260514T091815_result.json`
- **Structured JSON:** [`b392785e07c7b433adba.json`](../../sessions/b3/b392785e07c7b433adba.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告

### eval-sft-v1 — 已完成 ✓
- 模型: Qwen3-8B + SFT checkpoint
- 样本数: 202
- 退出码: 0

| Metric | Mean | 90% CI Low | 90% CI High |
|--------|------|------------|-------------|
| debug_accuracy | 0.2822 | 0.2277 | 0.3317 |
| probe_executed | 0.0000 | 0.0000 | 0.0000 |
| probe_diagnostic | 0.0050 | 0.0000 | 0.0149 |
| probe_dependent | 0.0594 | 0.0347 | 0.0842 |
| probe_generation_rate | 0.9901 | — | — |

### eval-base-v2 — 已完成 ✓
- 模型: Qwen3-8B (base, no checkpoint)
- 样本数: 202
- 退出码: 0

| Metric | Mean | 90% CI Low | 90% CI High |
|--------|------|------------|-------------|
| debug_accuracy | 0.2871 | 0.2376 | 0.3366 |
| probe_executed | 0.0050 | 0.0000 | 0.0149 |
| probe_diagnostic | 0.0099 | 0.0000 | 0.0198 |
| probe_dependent | 0.0545 | 0.0297 | 0.0842 |
| probe_generation_rate | 1.0000 | — | — |

### 对比小结

SFT 在所有 probe 质量指标上均未超过 base，CI 完全重叠。SFT 的 probe_executed 甚至降到 0.0（base 0.5%），probe_generation_rate 也略低（99.0% vs 100%）。debug_accuracy 两者无显著差异（28.2% vs 28.7%）。

### Qwen3-30B-A3B 下载 — 进行中
- 已下载: 15GB，当前下载第 10/16 个 shard（84%, 3.11G/3.73G）
- 速度: ~434 kB/s，预计当前 shard 还需 ~25 分钟
- modelscope 进程仍在运行

---
