# infra session handover check

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_session-handover-check_20260513T183443_result.json`
- **Structured JSON:** [`6e59972f2e490553c5bd.json`](../../sessions/6e/6e59972f2e490553c5bd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 服务器状态报告

### 1. GPU 状态
| GPU | 显存占用 | 利用率 | 进程 PID | 运行时长 |
|-----|---------|--------|----------|---------|
| GPU 0 | 28013 / 32607 MiB | 0% (采样瞬时) | 62662 (VLLM::EngineCore) | 14 min |
| GPU 1 | 28013 / 32607 MiB | 0% (采样瞬时) | 651246 (VLLM::EngineCore) | 2h 13m |

两张卡均在活跃推理中。

---

### 2. Boil v3 (GPU1) — 进行中
- **进程**: PID 650426, `phase1_signal.py --task_types boil --episodes 20`
- **进度**: **16/20 episodes** 完成，还差 4 个
- **无 summary.json**（未完成不会生成）

#### 当前结果 (n=16)
| Mode | Mean | Std | Scores |
|------|------|-----|--------|
| always_internal | **-43.38** | 51.59 | 6 个 -100, 2 个 +3, 其余 0 |
| always_deterministic | **-11.81** | 34.46 | 2 个 -100, 2 个 +3, 1 个 +5, 其余 0 |
| oracle_routing | **+4.75** | 17.43 | **1 个 +70**, 2 个 +3, 其余 0 |

#### 对比 MVP (old code, n=20)
| Mode | MVP Mean | v3 Mean | 变化 |
|------|---------|---------|------|
| always_internal | -49.75 | -43.38 | +6.37 |
| always_deterministic | -19.70 | -11.81 | +7.89 |
| oracle_routing | **-29.70** | **+4.75** | **+34.45** |

oracle_routing 改善巨大：v3 完全消除了 -100 致命惩罚，且出现了 70 分高分 episode。

---

### 3. 预筛 (GPU0) — 进行中
- **进程**: PID 61945, `signal_prescreening.py --task_type freeze --episodes 5`
- **模式**: 仅测 always_internal 和 always_deterministic（无 oracle_routing）

| Task | Episodes | Internal | Deterministic |
|------|----------|----------|---------------|
| chemistry-mix | 5/5 | -55.8 | **+4.2** |
| chemistry-mix-paint-tertiary-color | 5/5 | -37.4 | -17.4 |
| find-animal | 5/5 | -58.4 | **+8.2** |
| find-living-thing | 5/5 | -58.4 | -16.6 |
| find-non-living-thing | 5/5 | **+31.6** | **+24.8** |
| find-plant | 5/5 | -58.4 | **+3.2** |
| freeze | **3/5** | -33.3 | 0.0 |

freeze 还在跑（3/5 episodes）。find-non-living-thing 两种模式均为正分，表现最好。

---

### 4. 脚本就绪情况
| 脚本 | 状态 | 大小 | 最后修改 |
|------|------|------|---------|
| `src/router_sft_train.py` | 存在 | 12.7 KB | May 14 02:33 |
| `src/rule_based_routing.py` | 存在 | 11.6 KB | May 14 02:33 |
| `src/episode_level_collection.py` | 存在 | 13.9 KB | May 14 01:40 |
| `src/counterfactual_labeling.py` | 存在 | 12.3 KB | May 14 01:13 |

四个关键脚本均已就绪。

---

### 总结
- **两张 GPU 均在工作**：GPU0 跑预筛（freeze 3/5），GPU1 跑 boil v3（16/20）
- **Boil v3 相比 MVP 显著改善**，尤其 oracle_routing 从 -29.70 提升到 +4.75
- **预筛已完成 6 个 task，第 7 个 freeze 进行中**
- 预计 boil v3 约 30-40 分钟内完成剩余 4 个 episode，freeze 约 10 分钟内完成

---
