# debug s0 50r collision anomaly

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_debug_s0-50r-collision-anomaly_20260521T155224_result.json`
- **Structured JSON:** [`93411ddcf302bc03a24c.json`](../../sessions/93/93411ddcf302bc03a24c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**确认根因。** s0 50r 结果中所有 episode 的 `max_disp` 全是 `0.0`——碰撞检测完全失效。

## 诊断结论

### 1. 根因：`eval_safelibero.py` 的 ObstacleTracker 有 stale sim 引用 bug

`eval_safelibero.py`（s0 50r 用的）第 131 行：
```python
self.sim = env.env.sim  # 构造时缓存 sim 引用
```

`evaluate_safelibero.py`（s2 50r 用的）第 147 行：
```python
self.env = env  # 存 env 引用，每次动态解析 sim
```

执行流程：
1. `tracker = ObstacleTracker(env, ...)` → `self.sim = env.env.sim`（sim A）
2. `run_episode()` → `env.reset()` → robosuite 创建新 sim（sim B），`env.env.sim` 指向 sim B
3. `tracker.record_initial()` → 从 sim A（旧、冻结的）读位置
4. `tracker.step(t)` → 从 sim A 读位置 → **永远和 initial 一样** → displacement = 0.0 → 永远不触发碰撞

### 2. s0 和 s2 eval 的配置差异

| | s0 50r | s2 50r |
|---|---|---|
| 脚本 | `/root/occsafe_vla/eval/eval_safelibero.py` | `/root/occsafe_vla/openvla-oft/vla-scripts/evaluate_safelibero.py` |
| ObstacleTracker | `self.sim = env.env.sim`（stale 引用） | `self.env = env`（动态解析） |
| 碰撞数据 | 全部 `max_disp: 0.0` | 有真实位移值（如 0.002597） |
| episode 字段 | 无 `trajectory_length` | 有 `trajectory_length` |

### 3. eval_safelibero.py vs evaluate_safelibero.py 差异

除了上述 ObstacleTracker bug 外：
- `eval_safelibero.py` 的 `except Exception: pass` 静默吞掉所有异常，不打 WARNING
- `evaluate_safelibero.py` 打 WARNING 日志帮助调试
- `evaluate_safelibero.py` 记录 `trajectory_length` 和 `per_episode` 汇总统计

### 4. 修复方案

**最简方案：** 用 `evaluate_safelibero.py` 重跑 s0 50r eval。这是已验证正确的脚本。

**代码修复：** 如果还需要保留 `eval_safelibero.py`，改 ObstacleTracker 的 `__init__`：
```python
# 修改前
self.sim = env.env.sim

# 修改后
self.env = env
```
并将 `record_initial()` 和 `step()` 中所有 `self.sim.data` 改为 `self.env.env.sim.data`。

---
