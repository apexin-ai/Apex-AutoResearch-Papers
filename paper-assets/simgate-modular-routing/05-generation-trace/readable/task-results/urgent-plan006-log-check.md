# urgent plan006 log check

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_urgent_plan006-log-check_20260515T161020_result.json`
- **Structured JSON:** [`27eedd84e6a14bd0e958.json`](../../sessions/27/27eedd84e6a14bd0e958.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 判定结果：部分成功

### 1. 日志关键内容

| 日志 | 最后状态 |
|------|---------|
| GPU1 (`plan006_deep_internal.log`) | `EngineCore Shutdown complete` @ 00:10:38 — 正常关闭（被 kill） |
| GPU0 (`plan006_gpu0.log`) | `ERROR: Engine core proc EngineCore died unexpectedly` @ 00:10:48 — **非预期崩溃** |

GPU1 被 kill 时连带触发了 GPU0 的 vLLM EngineCore 崩溃（两个进程共享同一台机器的 GPU 驱动层，kill GPU1 的 vLLM 实例影响了 GPU0）。

### 2. Episode 数量

| Task | Episodes | 状态 |
|------|----------|------|
| identify-life-stages-1 | **20/20** | ✓ |
| lifespan-longest-lived | **20/20** | ✓ |
| find-non-living-thing | **20/20** | ✓ |
| inclined-plane-determine-angle | **20/20** | ✓ |
| lifespan-longest-lived-then-shortest-lived | **18/20** | ✗ 缺 2 |
| chemistry-mix | **13/20** | ✗ 缺 7 |
| **Total** | **111/120** | **92.5%** |

### 3. 数据质量

结构正确，两个 task 抽样验证通过：
- 字段完整：`episode_idx`, `variation_idx`, `always_deep_internal` (含 `mode`, `task_name`, `final_score`, `num_steps`, `total_time_s`, `action_history`, `steps`)
- 每个 step 含：`step`, `action`, `modality="deep-internal"`, `score_before`, `score_after`, `score_delta`, `observation`, `is_dead`
- `modality: "deep-internal"` 标记正确

### 4. GPU 状态

| GPU | 显存占用 | 利用率 |
|-----|---------|--------|
| GPU0 | 0 MiB | 0% |
| GPU1 | 15397 MiB | 0% |

PID 499313 仍存活但 EngineCore 已死，是僵尸进程。GPU1 上残留显存（被 kill 的进程的 vLLM 模型权重未释放）。

### 5. 需要补收

| Task | 缺失 | 起始 episode_idx |
|------|------|-----------------|
| lifespan-longest-lived-then-shortest-lived | 2 episodes | idx 18 |
| chemistry-mix | 7 episodes | idx 13 |

**建议下一步**：kill 僵尸进程 499313，释放 GPU1 显存，然后在单卡上补收这 9 个 episodes。

---
