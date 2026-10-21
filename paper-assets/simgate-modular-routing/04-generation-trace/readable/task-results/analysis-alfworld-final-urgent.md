# analysis alfworld final urgent

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_alfworld-final-urgent_20260520T110454_result.json`
- **Structured JSON:** [`381c4c8b416031d6b46a.json`](../../sessions/38/381c4c8b416031d6b46a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据已收集完毕，汇报如下：

---

## ALFWorld Llama 结果

**状态：已完成** — 135 episodes，进程已结束（GPU 0 残留模型在显存但 0% 利用率）。

**日志最后输出：**
```
Total: 67 games
  det-preferred: 2 (3.0%)
  internal-preferred: 0 (0.0%)
  no-preference: 65 (97.0%)
  Internal success: 0/67 (0.0%)
  Deterministic success: 2/67 (3.0%)
Output: results/alfworld_llama_counterfactual/episodes.jsonl
```
（这是运行脚本的实时统计，分析脚本的完整统计见下）

**分析脚本 stdout：**

| 指标 | 值 |
|------|-----|
| 总 episodes | 135 |
| det-preferred | 16 (11.9%) |
| int-preferred | 0 (0.0%) |
| no-preference | 119 (88.1%) |
| det-leaning (non-tie) | 100.0% |
| DAF | 0% (无死亡机制) |
| det-preferred 95% CI | [6.7%, 17.8%] |
| Δ_full 95% CI | [0.0667, 0.1778] |

**Per-task breakdown：**

| task_type | n | det | int | tie | det% |
|-----------|---|-----|-----|-----|------|
| look_at_obj_in_light | 13 | 1 | 0 | 12 | 7.7% |
| pick_and_place | 32 | 12 | 0 | 20 | 37.5% |
| pick_clean_then_place | 27 | 2 | 0 | 25 | 7.4% |
| pick_cool_then_place | 24 | 1 | 0 | 23 | 4.2% |
| pick_heat_then_place | 16 | 0 | 0 | 16 | 0.0% |
| pick_two_obj_and_place | 23 | 0 | 0 | 23 | 0.0% |

**Llama vs Qwen 对比：**

| Model | Det-Pref | Int-Pref | Tie | Det-Leaning | DAF |
|-------|----------|----------|-----|-------------|-----|
| Llama | 11.9% | 0.0% | 88.1% | 100.0% | 0% |
| Qwen | 25.9% | 0.0% | 72.6% | 100.0% | 0% |

**latex_table.tex：**
```latex
% ALFWorld counterfactual comparison: Llama vs Qwen
% Columns: Model & Det-Pref & Int-Pref & Tie & Det-Leaning & DAF
Llama & 11.9\% & 0.0\% & 88.1\% & 100.0\% & 0\% \\
Qwen  & 25.9\% & 0.0\% & 72.6\% & 100.0\% & 0\% \\
```

**analysis.json** 已保存，完整内容含 per_task 数组和 bootstrap CI（如上所述）。

---

## Gemma ScienceWorld 进度

| task | episodes |
|------|----------|
| boil | 20 |
| melt | 2 |
| identify-life-stages-1 | 20 |
| freeze | 14 |

GPU 1 上 VLLM 引擎运行中（27970MiB），Gemma 实验仍在进行。

---
