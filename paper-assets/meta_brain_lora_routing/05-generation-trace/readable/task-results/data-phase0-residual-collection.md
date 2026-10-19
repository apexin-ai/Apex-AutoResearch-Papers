# data phase0 residual collection

**Meta-Brain: Perturbation-Diagnostic Routing of LoRA Experts for Parameter-E cient VLA Robustness** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_phase0_residual_collection_20260515T160605_result.json`
- **Structured JSON:** [`63aa0c59d56c5a138fb6.json`](../../sessions/63/63aa0c59d56c5a138fb6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Per-step 激活数据状态汇总

| 扰动类型 | 文件名 | Episodes | 大小 | 状态 |
|---|---|---|---|---|
| camera_pose | `camera_viewpoints.pt` | 30 | 276MB | ✅ 完整 |
| lighting | `light_conditions.pt` | 30 | 276MB | ✅ 完整 |
| objects_layout | `objects_layout.pt` | 32 | 294MB | ✅ 已重收集完成 |
| robot_initial_states | `robot_initial_states.pt` | 30 | 276MB | ✅ 已重收集完成 |
| sensor_noise | `sensor_noise.pt` | 10/80 | 1.3KB | 🔄 收集中 (PID 182966, GPU 0) |
| background_textures | `background_textures.pt` | 29 | 267MB | ✅ 完整 (额外) |

**Episode-level 数据** (`activations/`):
- camera_viewpoints, light_conditions, objects_layout, robot_initial_states, background_textures, nominal — 全部存在
- sensor_noise episode-level — 缺失，正在收集 (PID 148761, GPU 1, 37/80 episodes)

**结论：**
- objects_layout 和 robot_initial_states 的 per_step 数据已在今天 23:45-23:46 重收集完毕，数据结构完整（含 `label_3class`）
- 唯一缺失项是 **sensor_noise**（per_step + episode-level），两个进程都在跑，无需新启动任务
- sensor_noise per_step 当前速度约 1 ep/min，预计还需 ~70 分钟完成
- **GPU 2 和 GPU 3 空闲，无需启动新任务**——所有缺失数据已有进程在收集

---
