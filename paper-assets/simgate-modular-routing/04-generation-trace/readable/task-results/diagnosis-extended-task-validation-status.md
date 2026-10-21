# diagnosis extended task validation status

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnosis_extended-task-validation-status_20260519T211256_result.json`
- **Structured JSON:** [`f3fac4e9b42651d893ae.json`](../../sessions/f3/f3fac4e9b42651d893ae.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

### GPU 状态
| GPU | 进程 | 显存 | 利用率 | 当前任务 |
|-----|------|------|--------|----------|
| cuda:0 | vLLM (PID 803414) | 28GB/32GB | 91% | `boil` 数据收集 |
| cuda:1 | vLLM (PID 803459) | 28GB/32GB | 0% | `use-thermometer` 数据收集 |

GPU 1 的 0% 利用率是正常的——采集到 snapshot 时刚好在做 ScienceWorld 环境模拟（CPU-bound Java 进程），不在推理。

### 数据收集进度

| Task | GPU | 已完成 | 目标 | 状态 |
|------|-----|--------|------|------|
| **boil** | 0 | 11/20 | 20 | 运行中 |
| melt | 0 | 0/20 | 20 | 排队（boil 之后） |
| find-living-thing | 0 | 0/20 | 20 | 排队（melt 之后） |
| **use-thermometer** | 1 | 10/20 | 20 | 运行中 |
| power-component | 1 | 0/20 | 20 | 排队（use-thermometer 之后） |

### 当前已收集数据快照

**boil** (11 episodes, ep 0-10):
| 指标 | internal | det |
|------|----------|-----|
| Deaths | 6/11 (54.5%) | 2/11 (18.2%) |
| ΔDR | +36.4pp | |
| det-preferred | 4 | |
| no-preference | 7 (5 tied_alive + 2 both_dead) | |

**use-thermometer** (10 episodes, ep 0-9):
| 指标 | internal | det |
|------|----------|-----|
| Deaths | 5/10 (50.0%) | 1/10 (10.0%) |
| ΔDR | +40.0pp | |
| det-preferred | 5 | |
| internal-preferred | 1 | |
| no-preference | 4 (tied_alive) | |

### 与 prescreening (n=5) 方向一致性

| Task | Prescreening ΔDR | 当前 ΔDR (partial) | 方向一致? |
|------|-------------------|---------------------|-----------|
| boil | +30pp | +36.4pp | **一致** |
| use-thermometer | ~+30pp | +40.0pp | **一致** |

### 时间估算

~3.5 min/episode。已运行 ~37 min（04:36 开始）。
- GPU 0 剩余: 9 (boil) + 20 (melt) + 20 (find-living-thing) = 49 episodes ≈ **2.8h**
- GPU 1 剩余: 10 (use-thermometer) + 20 (power-component) = 30 episodes ≈ **1.8h**

### 结论

- **无异常进程**——两张卡上的进程全部属于本实验
- 实验正常运行，约 **3 小时后**全部完成
- Registry 中无此实验条目（count=0），需要在实验完成后注册
- 已收集的 partial 数据与 prescreening 方向一致：internal death rate 显著高于 det，符合预期

---
