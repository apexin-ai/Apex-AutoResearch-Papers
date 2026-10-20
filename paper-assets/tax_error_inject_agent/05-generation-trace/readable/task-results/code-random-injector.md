# code random injector

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_random-injector_20260514T103705_result.json`
- **Structured JSON:** [`78239085b903104734ca.json`](../../sessions/78/78239085b903104734ca.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

注入位置分布完全一致（同 seed 下 `plan_injections` 用相同的 `select_injection_point` 函数）。

---

**总结**

RandomInjector 已完整实现并通过验证：

**代码位置**: `injection/random_injector.py`

**实现方式**: 继承 `InjectionOperator`，每次 `inject()` 从 6 种 perturbation 中均匀随机选一种：
- `swap_adjacent` — 交换相邻步骤（对应 P1）
- `delete_step` — 删除随机步骤（对应 P2）
- `truncate_prefix` — 截断前缀历史（对应 C1）
- `mask_observation` — 遮蔽观测（对应 C4）
- `replace_action_target` — 替换动作目标物体（额外 perturbation）
- `shuffle_segment` — 打乱连续片段（额外 perturbation）

**公平性保证**:
- **数量一致**: 同一 `plan_injections()` 逻辑，`num_variants` 参数控制总量
- **位置分布一致**: 同一 `select_injection_point()` 函数，同 seed 下分布完全相同（已验证）
- **同一 recovery teacher**: pipeline 用相同的 GPT-5.2 API 调用
- **唯一区别**: TaxEI 按 taxonomy 类别选算子，Random 均匀随机选 perturbation

**与 TaxEI 的区别**: TaxEI 模式有 4 个专用算子（P1/P2/C1/C4），每个针对特定错误类别设计；Random 模式用 1 个 `RandomInjector`，不区分错误类别，从通用 perturbation 池中随机采样。

**测试结果**: 100/100 inject+validate 通过，formatter 兼容，pipeline 集成通过，dry-run 48/50 成功。

---
