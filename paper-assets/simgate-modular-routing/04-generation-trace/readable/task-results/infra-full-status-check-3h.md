# infra full status check 3h

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_full-status-check-3h_20260513T184049_result.json`
- **Structured JSON:** [`92718a2155a27ad36af4.json`](../../sessions/92/92718a2155a27ad36af4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据全部到手，汇总如下。

---

## 状态报告 (2026-05-14 ~02:40 UTC, 运行 ~2h18m)

### 1. GPU 状态

| GPU | 利用率 | 显存 | 进程 |
|-----|--------|------|------|
| GPU0 | 0% | 28013/32607 MiB | PID 62662 (预筛) |
| GPU1 | 0% | 28013/32607 MiB | PID 651246 (Boil v3) |

两颗 GPU 显存满载，利用率快照为 0%（两进程均在推理间歇）。

### 2. Boil v3 (GPU1) — 仍在运行

- PID 650421，已跑 2h17m
- **16/20 episodes 完成**，日志仍在输出推理进度
- 无 summary.json（未完成时不生成）

**Boil v3 分数 (16 eps)：**

| Mode | Mean | 致命(-100)次数 |
|------|------|----------------|
| always_internal | **-49.6** | 8/16 |
| always_deterministic | **-11.8** | 2/16 |
| oracle_routing | **+4.75** | 0/16 |

**MVP Boil 对比 (20 eps)：**

| Mode | v3 (16ep) | MVP (20ep) | 变化 |
|------|-----------|------------|------|
| always_internal | -49.6 | -39.8 | ↓ (更多致命) |
| always_deterministic | -11.8 | -19.7 | ↑ (+7.9) |
| **oracle_routing** | **+4.75** | **-29.7** | **↑↑ (+34.5)** |

关键发现：**v3 oracle_routing 大幅改善**（+4.75 vs -29.7），16 个 episode 中 0 次致命。Det 也改善了。Oracle 与 det 的差距 = +16.55，说明路由空间存在且可学习。

### 3. 预筛 (GPU0) — 7/25 tasks 完成，正在跑第 8 个

PID 649681，已跑 2h18m。

| Task | I_mean | D_mean | **Δ(D-I)** | 趋势 |
|------|--------|--------|------------|------|
| chemistry-mix | -55.8 | 4.2 | **+60.0** | D 远优于 I |
| find-animal | -58.4 | 8.2 | **+66.6** | D 远优于 I |
| find-plant | -58.4 | 3.2 | **+61.6** | D 远优于 I |
| freeze | -60.0 | 2.0 | **+62.0** | D 远优于 I |
| find-living-thing | -58.4 | -16.6 | **+41.8** | D 优于 I |
| chem-mix-paint-tertiary | -37.4 | -17.4 | **+20.0** | D 优于 I |
| find-non-living-thing | 31.6 | 24.8 | **-6.8** | I 略优于 D |

7 个 task 中 6 个 Δ(D-I) 为正，说明 deterministic 模式普遍优于 internal。`find-non-living-thing` 是唯一例外（internal 反而更好，且两者均为正分）。

### 4. 脚本就绪确认

5 个脚本全部存在且最近更新（2026-05-14）：
- `src/episode_level_collection.py`
- `src/router_sft_train.py`
- `src/rule_based_routing.py`
- `src/counterfactual_labeling.py`
- `src/collect_trajectories.py`

### 5. 预估剩余时间

- **Boil v3**: 还剩 4/20 episodes，按当前速率约 30-40 分钟完成
- **预筛**: 7/25 完成（2h18m），每 task 约 20 分钟，剩余 18 个 task 约需 6 小时

---
