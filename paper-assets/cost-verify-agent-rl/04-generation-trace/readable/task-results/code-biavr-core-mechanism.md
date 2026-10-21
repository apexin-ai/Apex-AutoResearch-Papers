# code biavr core mechanism

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_biavr_core_mechanism_20260515T120804_result.json`
- **Structured JSON:** [`e7e9236fc5e1ca6d0945.json`](../../sessions/e7/e7e9236fc5e1ca6d0945.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

B-IAVR 核心模块已完整实现且全部测试通过。以下是现有实现与任务规格的映射：

### 现有模块（68/68 测试通过）

| 任务要求 | 现有实现 | 状态 |
|---------|---------|------|
| `action_change_detector.py` | `action_canonicalize.py` + `pre_action.py` | ✅ 完成 |
| `verification_reward.py` | `reward.py` (BIAVRTracker + Lagrangian dual) | ✅ 完成 |
| `selective_gate.py` | `verify_mechanism.py` (`&lt;VERIFY>` token解析 + prompt) | ✅ 完成 |
| `__init__.py` | 已导出所有公开接口 | ✅ 完成 |
| `tests/test_biavr.py` | 68 个测试全部通过 | ✅ 完成 |

### 框架集成已就绪

- `ctx_manager.py`: biavr_enabled 属性、`&lt;VERIFY>` token 解析、format prompt 适配、无强制 prefix
- `agent_trainer.py`: biavr metrics 记录 + lambda 自动更新

### 设计决策（比任务规格更成熟）

现有实现采用了**Lagrangian 对偶**方案而非固定 bonus/penalty：
- `r_step(t) = -λ·1[verify] + α·1[verify ∧ action_changed]`
- λ 通过 `λ_{t+1} = max(0, λ_t + η·(verify_rate - β))` 自适应
- β=0.3 目标验证率，η=0.01 学习率

Gate 机制选用 **Option A（token-based）**：模型在输出最前面决定是否输出 `&lt;VERIFY>`，端到端通过 GRPO 训练。

### 缺失项：`DESIGN_DECISIONS.md`

需要创建吗？待确认的关键决策点：
1. ~~Gate 机制~~ → 已选 token-based `&lt;VERIFY>` prefix
2. 验证触发条件 → 当前每步均可触发
3. ~~reward 系数~~ → Lagrangian 自适应（λ₀=0.1, α=1.0, β=0.3, η=0.01）
4. 与 GRPO advantage 的集成 → biavr reward 叠加到 step reward，通过 BIAVRTracker 在每个 training iteration 结束时更新 λ
5. **a_pre 计算的 inference cost** → 需要额外一次 greedy forward pass（当前 `pre_action.py` 定义了 prompt 但未在 rollout 循环中调用）

a_pre 的 rollout 集成（实际调用 counterfactual inference）是目前唯一还没 wire up 的部分，需要等 exp026 baseline 确认后再接入。

---
