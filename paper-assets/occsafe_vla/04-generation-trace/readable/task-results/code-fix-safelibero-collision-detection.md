# code fix safelibero collision detection

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix_safelibero_collision_detection_20260520T171638_result.json`
- **Structured JSON:** [`a90f2dde1a98c6ce4e23.json`](../../sessions/a9/a90f2dde1a98c6ce4e23.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证完成，结果完美证明了 bug 和修复：

**关键发现：**

1. **`sim identity changed after reset: True`** — `env.reset()` 确实会创建新 sim 对象（id 不同），确认 Bug 1 的前提成立。

2. **`buggy.sim is current sim: False`** — 所有 5 个 episode 中，buggy tracker 的 `self.sim` 都指向旧对象。

3. **对比结果：**

| | Buggy (原代码) | Fixed (修复后) |
|---|---|---|
| tracked | **0** | **3** |
| max_disp | 0.000000 | 0.000000~0.000517 |

- **Buggy**: tracked=0，`record_initial()` 在 stale sim 上读 body 全部抛异常被 `except: pass` 吞掉，`_initial_pos` 为空 → `step()` 什么都不检查 → max_disp 永远 0 → **CAR 永远 100%**
- **Fixed**: tracked=3，3 个 obstacle 全部正确追踪，Ep 2 检测到 0.000517 位移

**修改汇总：**
- L152: `self.sim = env.env.sim` → `self.env = env`（动态访问 sim）
- L172, L182: `self.sim.data.body(...)` → `self.env.env.sim.data.body(...)`
- L173: `except Exception: pass` → `except Exception as e: print(WARNING)`
- L175-176: 新增 `_initial_pos` 空检查警告
- L189: `except Exception: pass` → `except Exception as e: print(WARNING)`

备份文件在 `evaluate_safelibero.py.bak`。

---
