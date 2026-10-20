# ops check gpt2m null logs

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_gpt2m_null_logs_20260524T082139_result.json`
- **Structured JSON:** [`466c5fe3bdc872aa0b3e.json`](../../sessions/46/466c5fe3bdc872aa0b3e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验均已完整完成。结论如下：

---

## 结果

| 实验 | Generation 数 | EXIT_CODE | 状态 |
|------|--------------|-----------|------|
| `a000_gpt2m_s42_fp32` | 11 (gen_0→gen_10) | 0 | **SUCCESS** |
| `a000_gpt2m_s43_fp32` | 11 (gen_0→gen_10) | 0 | **SUCCESS** |

### 最终 metrics (gen_10)

| 指标 | s42 | s43 |
|------|-----|-----|
| token_entropy | 2.839 | 2.839 |
| perplexity | 17.27 | 17.26 |
| self_bleu | 0.022 | 0.026 |
| distinct_1 | 0.079 | 0.078 |
| distinct_2 | 0.359 | 0.350 |
| distinct_3 | 0.550 | 0.531 |
| mauve | 0.014 | 0.013 |
| effective_rank | 24.0 | 25.2 |
| ece | 0.011 | 0.011 |
| effective_alpha | 0.0 | 0.0 |

### 结论

两个实验都**真正完成**（10 个 training generation + gen_0 baseline，EXIT_CODE=0，all_metrics.json 完整）。Cron 监控误判——进程正常退出但缺少 sentinel 文件导致被标记为 "process dead"。

完整路径：
- `/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a000_gpt2m_s42_fp32/`
- `/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a000_gpt2m_s43_fp32/`

---
