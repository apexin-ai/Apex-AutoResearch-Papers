# analysis olmo instruct results

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_olmo-instruct-results_20260515T165350_result.json`
- **Structured JSON:** [`4e8c35350659f82b1310.json`](../../sessions/4e/4e8c35350659f82b1310.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有信息已收集。汇总报告如下：

---

## 实验状态报告

### review-p1c-olmo-instruct (cuda:0, PID 218484)

**Step 1 Generation — 仍在运行，~86% 完成**

| 指标 | 值 |
|------|-----|
| Seeds 完成 | 857 / 995 (86.1%) |
| 剩余 | 138 seeds |
| 总 records | 3,830 |
| 预计 ETA | ~15 min（约 01:10 UTC） |

Depth 分布：

| Depth | Records | 占 seed 比 |
|-------|---------|-----------|
| 0 | 857 | 100% |
| 1 | 834 | 97.3% |
| 2 | 768 | 89.6% |
| 3 | 706 | 82.4% |
| 4 | 665 | 77.6% |
| 5-6 | 0 | — |

instruct 链在 depth 4 后逐渐截断（chain 产生空输出时提前停止）。

**Step 2 (feature extraction)** — 未开始，等 Step 1 完成  
**Step 3 (LOGO analysis)** — 未开始

pipeline 是 `set -e` 串行执行，Step 1 完成后会自动执行 Step 2 和 3。**整个 pipeline 预计还需 ~30-40 min**（Step 1 ~15min + Step 2 ~10min + Step 3 ~5min）。

---

### GPU 占用状态

| GPU | VRAM 使用 | 利用率 | 任务 | 进度 |
|-----|----------|--------|------|------|
| cuda:0 | 3,647 / 32,607 MiB | 50% | p1c_olmo: OLMo-instruct generation | 857/995 seeds (86%), ETA ~15min |
| cuda:1 | 4,031 / 32,607 MiB | 42% | plan-010: human_edit_robustness (PID 223500) | Rephrase 12,800/21,557 (59%), ETA ~35min |
| cuda:2 | 3,977 / 32,607 MiB | 41% | high_temp: run_high_only.py | 刚启动 ~8min |
| cuda:3 | 3,979 / 32,607 MiB | 43% | sampling_ablation (low_t05_p08) | 237/996 (24%), ETA ~2.9h |

**4 张 5090 全部在用，无空闲 GPU。**

---

### 下一步

p1c_olmo pipeline 预计 ~01:45 UTC 左右全部完成。完成后可收集 LOGO F1、特征 Spearman ρ、length-matched 分析等指标，与 base OLMo-2-1B (LOGO F1=0.7635) 对比。需要我稍后再检查一次吗？

---
