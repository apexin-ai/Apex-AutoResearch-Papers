# code fix biavr apre wiring

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-biavr-apre-wiring_20260514T044447_result.json`
- **Structured JSON:** [`b57531a2b618acc967eb.json`](../../sessions/b5/b57531a2b618acc967eb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 修复完成

### 改了什么

**文件**: `/root/cost-verify-agent-rl/RAGEN/ragen/llm_agent/agent_proxy.py`

**Bug 1 修复** — 在 rollout 循环中调用 `_build_a_pre_inputs()` (第 303-309 行):

在 B-IAVR tracking block 之后、`es_manager.step()` 之前，增加了 a_pre 计算逻辑。当 `biavr.enable_a_pre=True` 时，对选择了 `&lt;VERIFY>` 的 env 执行:
1. `_build_a_pre_inputs()` 构建无 self-guidance 的 counterfactual prompt
2. `_generate_a_pre_greedy()` 用 temperature=0 greedy decode 生成 a_pre
3. `compare_actions(a_pre, a_post)` 比较前后 action
4. 更新 `biavr_changed[eid][-1]`

**Bug 2 修复** — `biavr_changed` 不再永远是 False:

通过上述 wiring，当 a_pre != a_post 时，`biavr_changed` 会被设为 True，`action_changed_t` 传入 reward 计算后可以拿到 `+alpha` 奖励。

**新增方法**:
- `_compute_and_update_a_pre()` — 协调 a_pre prompt 构建、生成、比较的完整流程
- `_generate_a_pre_greedy()` — 支持 VllmWrapperWg（直接调 vLLM engine）和 RayWorkerGroup（构建 DataProto + `do_sample=False`）两种后端

### 为什么这样改

原代码中所有组件都已实现（`_build_a_pre_inputs`、`compare_actions`、`extract_action_from_response`），但没有在 rollout 循环中调用。这导致 `action_changed` 永远为 False → verify 只有 `-lambda_cost` 惩罚没有 `+alpha` 奖励 → agent 学到永远不 verify → B-IAVR 机制完全失效。

修复仅在 `_biavr_enable_a_pre=True` 时激活，不影响非 B-IAVR 路径。

### 测试结果

68/68 pass（61 existing + 7 new wiring tests），无 GPU 操作。

---
