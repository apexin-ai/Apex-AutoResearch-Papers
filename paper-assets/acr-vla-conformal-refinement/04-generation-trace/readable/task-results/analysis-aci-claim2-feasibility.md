# analysis aci claim2 feasibility

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_aci-claim2-feasibility_20260515T024604_result.json`
- **Structured JSON:** [`156e0caeda189321ee43.json`](../../sessions/15/156e0caeda189321ee43.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已获取全部代码。以下是分析结果。

## ACI Claim 2 Feasibility

### 1. ACI 实现状态
- **ACI 类/模块**: 存在，`src/aci.py`，完整实现
- **核心方法**: `__init__`, `update(expert_action, mean_action, cov_matrix, conformal_radius)`, `_compute_coc()`, `reset()`
- **aci.update() 调用点**: **无**。evaluate.py 仅在 L293 创建实例、L311 调用 `aci.reset()`，从未调用 `update()`
- **ACI 对象从未传入任何 action selection 函数**，是一段死代码

### 2. eval loop 结构
- **文件**: evaluate.py
- **evaluate() 函数**: L244-L375
- **task 循环**: L303 `for task_info in task_envs:`
- **rollout 循环**: L315 `for r in range(args.n_rollouts):`
- **step 循环**: L222-L242 `rollout_single()` 内部，`for step in range(max_steps):`
- **当前 step 流程**: `action_fn(obs)` → `env.step(action_7d)` → 检查 done/success → 返回 (success, steps)

### 3. 启用 ACI 所需修改

**核心障碍：`aci.update()` 需要 `expert_action`（ground truth），但 eval 时没有 expert action。**

`update()` 签名:
```python
def update(self, expert_action, mean_action, cov_matrix, conformal_radius)
```
- `expert_action`: eval 时不可用。LIBERO 环境只返回 obs/reward/done，不提供当前 step 的 expert action
- `mean_action`: 可从 CGS 获得
- `cov_matrix`: CGS 内部计算但**不返回**，需修改 CGS 接口
- `conformal_radius`: 同上，CGS 内部计算但不返回

**具体修改点:**

| # | 文件:位置 | 修改内容 | 难度 |
|---|----------|---------|------|
| 1 | **aci.py: update()** | 重新设计 error signal，不依赖 expert_action。可选方案：(a) 用 t+1 步实际 obs 与预测的偏差作为 error；(b) 用 Mahalanobis self-consistency 替代 | 高 |
| 2 | **cgs.py: compute_features()** | 返回 per-step `cov_matrix` 和 `conformal_radius`（当前只返回聚合特征） | 低 |
| 3 | **evaluate.py: rollout_single()** | 重构为暴露 per-step 中间数据（当前是黑盒闭包），或把 ACI 逻辑注入 action_fn 闭包 | 中 |
| 4 | **evaluate.py: select_action_crm()** | 接收 aci 对象，每步调用 aci.update()，用 aci.alpha 动态替换 CGS 的静态 alpha | 中 |
| 5 | **evaluate.py: parse_args()** | 新增 `--aci_gamma`, `--aci_alpha_target` 等 CLI 参数 | 低 |

### 4. 工作量评估

- **如果用 self-consistency 替代 expert_action**（即不需要真正的 ground truth，用预测自身的漂移作为 proxy error signal）:
  - 代码修改: ~60-80 行
  - 难度: **中**
  - 估计时间: **3-5 小时**
  - 风险: proxy error 的有效性未经验证，可能需要调参

- **如果坚持原始 ACI 公式（需要 expert action）**:
  - 需要从 LIBERO demo 数据中按 step 对齐提取 expert action，这在 closed-loop eval 中几乎不可行（轨迹会 diverge）
  - 难度: **高**
  - 估计时间: **1-2 天**
  - 风险: 高——closed-loop eval 中 agent 轨迹与 demo 轨迹偏离后，expert action 对齐失效

- **核心风险**: ACI 的理论保证依赖于 i.i.d. 或 exchangeable 的 calibration error 序列。在 closed-loop robotics 中，连续 step 高度相关，ACI 的覆盖率保证可能不成立。这是一个**理论层面的问题**，不是纯工程问题。

### 总结

ACI 模块代码完整但从未接入 eval loop。主要障碍不是工程量，而是 **eval 时缺少 ground truth action** 这一根本性数据依赖。最务实的方案是重新定义 error signal（例如用 next-step observation prediction error 或 self-consistency），绕开对 expert action 的依赖，但这改变了 ACI 的语义，需要在论文中明确说明。

---
