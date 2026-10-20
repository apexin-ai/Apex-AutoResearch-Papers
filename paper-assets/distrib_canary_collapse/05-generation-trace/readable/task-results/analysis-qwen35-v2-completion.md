# analysis qwen35 v2 completion

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_qwen35_v2_completion_20260519T131813_result.json`
- **Structured JSON:** [`fa0e7447214521d485d5.json`](../../sessions/fa/fa0e7447214521d485d5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部任务已由先前 session 完成。以下是完整状态报告：

---

## qwen35_08b_wiki_a100_s42_v2 — 完成报告

### 状态
| 项目 | 状态 |
|------|------|
| PID 74455 | 已终止 |
| GPU cuda:1 | 已释放 (0 MiB) |
| EXIT_CODE | 0 |
| Registry | **DONE**, conclusion=**success** |
| 结果目录 | `results/generalize/qwen35_08b_wiki_a100_s42_fp32_v2/` (gen_0 ~ gen_10 + all_metrics.json + analysis_results.json) |

### 5-Method Lead-Lag 分析

| 方法 | 结果 |
|------|------|
| **PermG fwd** | **8/8** (全部 FDR 显著) |
| **PermG rev** | **0/8** (正确方向性) |
| **K≥4 consensus** | **8/8** |
| **MMCT detection** | **1.0** (100%) |
| TY Granger | 6/8 |

### Consensus Detail (8/8 pairs, 全部 ≥4 votes)

| Pair | Votes | Methods |
|------|-------|---------|
| token_entropy → distinct_1 | 4 | naive, diff, thresh, pg_fwd |
| token_entropy → distinct_2 | 5 | naive, diff, thresh, pg_fwd, ty |
| token_entropy → distinct_3 | 4 | naive, diff, thresh, pg_fwd |
| token_entropy → mauve | 5 | naive, diff, thresh, pg_fwd, ty |
| ece → distinct_1 | 5 | naive, diff, thresh, pg_fwd, ty |
| ece → distinct_2 | 5 | naive, diff, thresh, pg_fwd, ty |
| ece → distinct_3 | 5 | naive, diff, thresh, pg_fwd, ty |
| ece → mauve | 5 | naive, diff, thresh, pg_fwd, ty |

### Drift (gen 0 → gen 10)

| Metric | Gen 0 | Gen 10 | Drift % |
|--------|-------|--------|---------|
| token_entropy | 2.978 | 1.369 | **-54.03%** |
| ece | 0.007 | 0.423 | **+5643.53%** |
| perplexity | 20.55 | 1247.19 | **+5968.54%** |
| distinct_1 | 0.094 | 0.063 | -32.50% |
| distinct_2 | 0.459 | 0.248 | -45.99% |
| distinct_3 | 0.741 | 0.391 | -47.21% |
| effective_rank | 43.60 | 103.27 | +136.87% |
| mauve | 0.029 | 0.022 | -22.89% |

### Conclusion 判断

**Success** — Qwen3.5-0.8B（第 7 个架构族）完美确认跨架构泛化：
- K≥4 = 8/8（满分），所有 canary-downstream pair 均显示 lead-lag 因果结构
- PermG 方向性完美：fwd 8/8, rev 0/8，排除反向因果
- MMCT 检测率 100%
- Collapse 信号极强：entropy 在 gen 1 即剧烈下降（2.978→1.505，-49.5%），downstream diversity 在 gen 2 开始追随下降，onset lead time = 1 gen（所有 8 pairs 一致）
- fp32 精度下 collapse magnitude 极大（ppl +5969%），与其他 α=1.0 fp32 实验一致

**无需进一步操作**——进程、GPU、registry 均已处理完毕。

---
