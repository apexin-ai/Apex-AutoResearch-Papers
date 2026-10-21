# diagnosis ext val urgent check

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnosis_ext-val-urgent-check_20260519T215927_result.json`
- **Structured JSON:** [`3e5b26675b1d1e5b7fc4.json`](../../sessions/3e/3e5b26675b1d1e5b7fc4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态

**实验仍在运行，不是挂掉。** GPU 利用率 0% 是瞬时快照，两个 tmux session 都在活跃推理。

### 当前进度

| Task | 完成/目标 | 状态 |
|------|----------|------|
| boil | 20/20 | ✅ 完成 |
| melt | 0/20 | ❌ VLLM EngineDeadError 崩溃，需重跑 |
| find-living-thing | 4/20 | 🔄 GPU 0 运行中 |
| use-thermometer | 20/20 | ✅ 完成 |
| power-component | 4/20 | 🔄 GPU 1 运行中 |

### 已完成 task 的关键结果

| Task | internal DR | det DR | **ΔDR** | D/I/N | Prescreening ΔDR | 一致？ |
|------|------------|--------|---------|-------|-------------------|--------|
| boil (n=20) | 55% | 25% | **+30pp** | 6/0/14 | +30pp | ✅ exact |
| use-thermometer (n=20) | 50% | 20% | **+30pp** | 7/1/12 | ~+30pp | ✅ exact |

### melt 失败原因
VLLM EngineCore 进程在 `run_episode_deterministic` 推理过程中意外死亡。脚本 catch 了错误继续跑 find-living-thing。melt 需要在当前 task 完成后单独重跑。

### 预计完成时间
GPU 0/1 各还剩 ~16 episodes，按当前速率约 1-1.5 小时完成 find-living-thing 和 power-component。melt 需额外重跑。

报告已写入 artifacts，registry 已更新 metrics。

---
