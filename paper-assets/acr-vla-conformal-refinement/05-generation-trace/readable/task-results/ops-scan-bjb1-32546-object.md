# ops scan bjb1 32546 object

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_scan-bjb1-32546-object_20260515T113909_result.json`
- **Structured JSON:** [`b83caade122281938773.json`](../../sessions/b8/b83caade122281938773.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

6 个 registry 全部更新完毕。汇总如下：

## Object Eval 进度快照 (2026-05-15 19:45 UTC)

| # | 实验 | GPU | 进度 | Running Avg | 状态 |
|---|------|-----|------|-------------|------|
| 1 | **reconvla** (baseline) | cuda:0 | 6/10 | **6.7%** | alive |
| 2 | **perdof** CRM | cuda:1 | 6/10 (butter 5/10) | **8.3%** | alive |
| 3 | ⭐ **obs_only** CRM (norm=0.1) | cuda:2 | 6/10 | **13.3%** | alive |
| 4 | **scalar** CRM | cuda:3 | 6/10 | **3.3%** | alive |
| 5 | **obs_only** (norm=0.2) | cuda:4 | 5/10 | **18.0%** | alive |
| 6 | **vla_mean** (baseline) | cuda:5 | 6/10 | **10.0%** | alive |

### Per-task 明细

| Task | reconvla | perdof | obs_only⭐ | scalar | obs_only_0.2 | vla_mean |
|------|----------|--------|-----------|--------|-------------|----------|
| alphabet_soup | 0% | 0% | 0% | 0% | 0% | 0% |
| cream_cheese | 0% | 0% | **10%** | 0% | 0% | 0% |
| salad_dressing | 10% | 20% | 20% | 10% | **30%** | 10% |
| bbq_sauce | **30%** | **30%** | **40%** | 10% | **40%** | **30%** |
| ketchup | 0% | 0% | **10%** | 0% | **20%** | 10% |
| tomato_sauce | 0% | 0% | 0% | 0% | — | 10% |

### 关键发现

1. **obs_only norm=0.2 暂时领先** (18.0%)，但只完成 5 个 task，还需观察后续
2. **obs_only norm=0.1** 排第二 (13.3%)，是唯一在 cream_cheese 和 ketchup 上都有成功的方法
3. **scalar CRM 最差** (3.3%)，比两个 baseline 都低
4. **所有方法在 alphabet_soup 上全军覆没**（0%），这是公认最难的 task
5. GPU 利用率 ~20-22%，所有 python 进程 CPU 134-137%，运行正常
6. 估计还需 ~3-4 小时完成剩余 4 个 task

---
