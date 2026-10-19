## FSDP1→FSDP1/2 双兼容 全量审计修复报告

### 修改清单（10 处，5 个文件）

| 文件 | 行号 | FSDP1 模式 | 修复方式 |
|------|------|-----------|---------|
| ragen/workers/actor/dp_actor.py | 224 | `_fsdp_wrapped_module` | `getattr(..., "_fsdp_wrapped_module", model)` |
| ragen/workers/actor/dp_actor.py | 227, 248 | `FSDP.summon_full_params` | `isinstance(model, FSDP)` guard |
| ragen/workers/critic/dp_critic.py | 157 | `_fsdp_wrapped_module` | `getattr` |
| ragen/workers/critic/dp_critic.py | 160, 175 | `FSDP.summon_full_params` | `isinstance` guard |
| ragen/workers/sharding_manager/fsdp_vllm.py | 70, 120 | `_fsdp_wrapped_module` | `getattr` |
| ragen/workers/sharding_manager/fsdp_vllm.py | 73, 75, 121 | `summon_full_params` + nested access | `isinstance` guard + `getattr` chain |
| verl/verl/utils/fsdp_utils.py | 597, 629 | `FSDP.summon_full_params` | `isinstance` guard |
| verl/verl/workers/sharding_manager/fsdp_vllm.py | 148 | `FSDP.summon_full_params` | `isinstance` guard |

### 兼容策略

1. `_fsdp_wrapped_module` → `getattr(model, "_fsdp_wrapped_module", model)`
2. `FSDP.summon_full_params(model)` → `FSDP.summon_full_params(model) if isinstance(model, FSDP) else nullcontext()`

全部通过 ast.parse 语法验证。