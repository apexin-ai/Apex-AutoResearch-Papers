# code eval improvements

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_eval_improvements_20260520T021106_result.json`
- **Structured JSON:** [`af0b9fe9af28a191916b.json`](../../sessions/af/af0b9fe9af28a191916b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

编译通过，--help 输出正确。三个 fix 全部完成：

---

**Fix 1: `--no_refine` 参数** ✅
- `--model_type a3`（默认）：训练 + inference refinement
- `--model_type a3 --no_refine`：仅训练效果，跳过 `_refine_action_a3`，但仍记录 SDF 值（走 A1 的 SDF logging 路径）
- 输出 JSON 中记录 `refine_enabled: true/false`

**Fix 2: `--collision_threshold` 参数** ✅
- 默认值 0.001m（与原有行为一致），可通过命令行调整
- SafeLIBERO/VLSA 原始 eval 不检测碰撞（只测 success rate），displacement-based 碰撞检测是我们自己的方法，无参考阈值可对齐。建议跑实验时对比 0.001/0.005/0.01 看效果
- 输出 JSON 中记录 `collision_threshold` 值

**Fix 3: `OBSTACLE_NAMES` 覆盖** ✅
- 从 BDDL 文件确认：`safelibero_spatial/object/goal` 用 6 个标准尺寸障碍物（与原列表一致）
- `safelibero_long` 用 3 个 **small 变体**：`moka_pot_small_obstacle_1`, `milk_small_obstacle_1`, `wine_bottle_small_obstacle_1` — 原脚本会漏检这 3 个
- 新增 `SUITE_OBSTACLE_NAMES` 映射，evaluate_task 自动选择正确的列表
- `--verify_obstacles` 模式可加载 MuJoCo 环境实际验证 body names（需要 GPU）

---
