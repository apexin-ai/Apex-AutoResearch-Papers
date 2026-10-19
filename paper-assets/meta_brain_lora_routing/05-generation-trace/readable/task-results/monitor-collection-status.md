# monitor collection status

**Meta-Brain: Perturbation-Diagnostic Routing of LoRA Experts for Parameter-E cient VLA Robustness** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_collection-status_20260515T134313_result.json`
- **Structured JSON:** [`806120b3db7b706b25b6.json`](../../sessions/80/806120b3db7b706b25b6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 数据收集状态汇总

### GPU 状态
| GPU | 利用率 | 显存 |
|-----|--------|------|
| 0 | 0% | 1 MiB (空闲) |
| 1 | 0% | 8386 MiB (已加载) |
| 2 | 35% | 8386 MiB (活跃) |
| 3 | 0% | 1 MiB (空闲) |

### 数据文件状态
| 条件 | 文件 | 大小 | 状态 |
|------|------|------|------|
| camera_viewpoints | 存在 | 17M | 可能完成 (80 ep) |
| background_textures | 存在 | 40M | 可能完成 (80 ep) |
| objects_layout | 存在 | 17M | 可能完成 (80 ep) |
| nominal | 存在 | 21M | 可能完成 (100 ep) |
| light_conditions | 存在 | **1.3K** | **FAILED — 0 episodes** |
| sensor_noise | 不存在 | — | 正在重试中 |
| robot_initial_states | 不存在 | — | 正在运行中 |

### 问题详情

**1. light_conditions — 完全失败**
- 错误：`FileNotFoundError: /root/LIBERO-plus/libero/libero/assets/scenes/lights/tabletop_light_sync_modified_130.xml`
- 缺少场景 XML 文件，0 episodes 写入

**2. sensor_noise — 卡死/循环崩溃**
- 错误：`AttributeError: np.float_ was removed in the NumPy 2.0 release. Use np.float64 instead.`
- Episode 17/80 时崩溃，日志显示在反复重载 tasks（21:43:57 又一次 task matching），但会再次撞同一个 bug
- 根因：LIBERO-plus 的 `env_wrapper.py:105` 用了 `np.float_`，与 NumPy 2.0 不兼容

**3. robot_initial_states — 正在运行**
- 日志 `collect_robot_initial_states_2.log` 显示 21:44:12 完成 task matching（350/2402 tasks），应该在正常收集中
- 使用 GPU 1 或 GPU 2

### 需要修复才能继续

1. **light_conditions**: 缺少 `tabletop_light_sync_modified_130.xml`，需确认场景文件是否生成/拷贝到位
2. **sensor_noise**: 需在 `/root/LIBERO-plus/libero/libero/envs/env_wrapper.py:105` 将 `np.float_` 改为 `np.float64`，然后重跑

---
