# code d098 fsdp2 full audit

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d098_fsdp2_full_audit_20260519T185853_result.json`
- **Structured JSON:** [`edf8131bc5526cc6dd62.json`](../../sessions/ed/edf8131bc5526cc6dd62.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## FSDP1→FSDP1/2 双兼容 全量审计修复报告

### 修改清单

| 文件 | 行号 | FSDP1 模式 | 修复方式 | 在执行路径上? |
|------|------|-----------|---------|-------------|
| `ragen/workers/actor/dp_actor.py` | 224 | `self.actor_module._fsdp_wrapped_module` | `getattr(self.actor_module, "_fsdp_wrapped_module", self.actor_module)` | **YES — v9b 崩溃点** |
| `ragen/workers/actor/dp_actor.py` | 227, 248 | `FSDP.summon_full_params(self.actor_module)` | `... if isinstance(self.actor_module, FSDP) else nullcontext()` | **YES** |
| `ragen/workers/critic/dp_critic.py` | 157 | `self.critic_module._fsdp_wrapped_module` | `getattr(self.critic_module, "_fsdp_wrapped_module", self.critic_module)` | **YES** |
| `ragen/workers/critic/dp_critic.py` | 160, 175 | `FSDP.summon_full_params(self.critic_module)` | `... if isinstance(self.critic_module, FSDP) else nullcontext()` | **YES** |
| `ragen/workers/sharding_manager/fsdp_vllm.py` | 70, 120 | `self.module._fsdp_wrapped_module` isinstance | `getattr(self.module, "_fsdp_wrapped_module", self.module)` | **YES** |
| `ragen/workers/sharding_manager/fsdp_vllm.py` | 75 | `self.module._fsdp_wrapped_module.base_model.model` | `getattr(self.module, ...).base_model.model` | **YES** |
| `ragen/workers/sharding_manager/fsdp_vllm.py` | 73, 121 | `FSDP.summon_full_params(self.module)` | `... if isinstance(self.module, FSDP) else nullcontext()` | **YES** |
| `verl/verl/utils/fsdp_utils.py` | 597 | `FSDP.summon_full_params(submodule)` | `... if isinstance(submodule, FSDP) else nullcontext()` | YES (LoRA 路径) |
| `verl/verl/utils/fsdp_utils.py` | 629 | `FSDP.summon_full_params(module)` | `... if isinstance(module, FSDP) else nullcontext()` | YES (LoRA 路径) |
| `verl/verl/workers/sharding_manager/fsdp_vllm.py` | 148 | `FSDP.summon_full_params(self.module)` | `... if isinstance(self.module, FSDP) else nullcontext()` | YES (verl base `__enter__`) |

### 已确认无需修改的文件

| 文件 | 原因 |
|------|------|
| `verl/verl/utils/checkpoint/fsdp_checkpoint_manager.py:261` | 已有 `if fsdp_version(self.model) == 1:` 守卫 |
| `verl/verl/utils/activation_offload.py:531,557` | 已有 `if isinstance(child, FSDP):` 守卫 |
| `verl/verl/workers/fsdp_workers.py:795` | 已有 `if fsdp_version(...) == 1:` 守卫 |
| `verl/verl/workers/fsdp_workers.py:661,675,690` | 已用 `getattr(..., "_fsdp_wrapped_module", ...)` |
| `verl/verl/workers/engine/fsdp/transformer_impl.py:633,646` | 已用 `getattr` 模式 |
| `verl/verl/workers/sharding_manager/fsdp_sglang.py:143` | 已用 `getattr` 模式 |
| `verl/verl/utils/fsdp_utils.py:590,619` | 已用 `getattr` 模式 |
| `verl/verl/utils/fsdp_utils.py:580-583,645,663` | 字符串替换操作，FSDP2 名称中不含 `_fsdp_wrapped_module` 时自动无效 |
| `verl/tests/*`, `verl/recipe/*`, `patches/*` | 不在 GRPO 执行路径 |

### 兼容策略

两种修复模式：

1. **`_fsdp_wrapped_module` 属性访问** → `getattr(model, "_fsdp_wrapped_module", model)`
   - FSDP1: 返回 unwrapped 原始模型
   - FSDP2: model 自身（composable API 无 wrapper）

2. **`FSDP.summon_full_params(model)`** → `FSDP.summon_full_params(model) if isinstance(model, FSDP) else nullcontext()`
   - FSDP1: 正常收集完整参数
   - FSDP2: 跳过（参数是 DTensor，可直接操作）

所有修改保留 FSDP1 完整兼容，5 个文件全部通过 `ast.parse` 语法验证。

---
