# analysis collect all eval results

**Meta-Brain: Perturbation-Diagnostic Routing of LoRA Experts for Parameter-E cient VLA Robustness** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_collect_all_eval_results_20260517T010713_result.json`
- **Structured JSON:** [`40758efd8794397d8cf0.json`](../../sessions/40/40758efd8794397d8cf0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完毕。以下是完整汇总：

---

## GPU 状态

| GPU | 显存使用 | 总显存 | 利用率 | 占用进程 |
|-----|---------|--------|--------|---------|
| 0 | 8,752 MiB | 97,887 MiB | 0% | Visual expert eval (PID 499143) |
| 1 | 8,780 MiB | 97,887 MiB | 0% | r48 eval (PID 493569) |
| 2 | 9,430 MiB | 97,887 MiB | 88% | train_strong.py (PID 695712) |
| 3 | 1 MiB | 97,887 MiB | 0% | **空闲** |

注：GPU 0/1 利用率显示 0% 但有进程占用显存，可能是 eval 在 episode 间隙的空闲态。

---

## 正在运行的进程

| PID | 实验 | GPU | 当前进度 |
|-----|------|-----|---------|
| 493569 | Universal r48 (全8类) | cuda:1 | sensor_noise seed=42 ep=9/20 (第7/8类) |
| 499143 | Visual expert 5pt | cuda:0 | sensor_noise seed=123 ep=14/20 (第4/5类) |
| 695712 | train_strong.py | cuda:2 | 运行中 |

---

## 已完成 Eval 结果汇总

### 完整数据（3 seeds × 20 episodes = 60 episodes/perturbation）

| Perturbation | Baseline (none) | Universal r16 | Visual Expert | Physical Expert | r48 |
|---|---|---|---|---|---|
| nominal | 60.0% (36/60) | **65.0%** (39/60) | N/A (运行中) | 58.3% (35/60) | N/A (运行中) |
| background_textures | 78.3% (47/60) | 78.3% (47/60) | 78.3%† (47/60) | — | N/A (运行中) |
| objects_layout | 58.8% (20/34) | **67.6%** (23/34) | — | — | N/A (运行中) |
| robot_initial_states | 22.6% (12/53) | 20.8% (11/53) | — | **26.4%** (14/53) | N/A (运行中) |
| camera_viewpoints | 68.4% (39/57) | **70.2%** (40/57) | N/A (运行中) | — | N/A (运行中) |
| light_conditions | 56.7% (34/60) | **71.7%** (43/60) | 63.3%† (38/60) | — | N/A (运行中) |
| sensor_noise | 65.5% (36/55) | 65.5% (36/55) | N/A (运行中) | — | N/A (运行中) |
| language | 0/0 | 0/0 | — | — | N/A |

†Visual expert 部分结果来自早期单类测试（visual_expert_eval.log），完整 5pt 结果（含 nominal/camera_viewpoints/sensor_noise）仍在运行。

---

## 关键发现

1. **Universal r16 vs Baseline**：在 light_conditions (+15.0pp)、objects_layout (+8.8pp)、nominal (+5.0pp) 上明显提升；robot_initial_states 略降 (-1.8pp)
2. **Physical expert**：robot_initial_states 比 baseline 高 3.8pp (26.4% vs 22.6%)，但 nominal 反而低于 baseline (-1.7pp)
3. **Visual expert 初步结果**：light_conditions (63.3%) 低于 universal r16 (71.7%)，background_textures 持平。需等待完整 5pt 跑完再确认

---

## 数据缺失清单

| 条件 | 缺失内容 | 预计完成 |
|------|---------|---------|
| Universal r48 | 全部 8 类 | 仍在运行，~30-40min 完成 |
| Visual expert (完整) | nominal, camera_viewpoints, sensor_noise | 仍在运行，~20-30min 完成 |
| Physical expert | 仅测了 robot_initial_states + nominal，其他 6 类无数据 | 需单独安排 |

---
