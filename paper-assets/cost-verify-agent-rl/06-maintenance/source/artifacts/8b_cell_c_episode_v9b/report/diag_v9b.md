# 诊断报告：8b_cell_c_episode_v9b 失败分析

## 失败直接原因

```
AttributeError: 'FSDPQwen3ForCausalLM' object has no attribute '_fsdp_wrapped_module'
```

**完整调用链：**
```
fsdp_workers.py:978  compute_log_prob
  → dp_actor.py:223  compute_log_prob
    → self.actor_module._fsdp_wrapped_module  # AttributeError
```

出错代码（`ragen/workers/actor/dp_actor.py:223`）：
```python
is_peft_model = not no_lora and isinstance(self.actor_module._fsdp_wrapped_module, PeftModel)
```

## 根因分析

**代码 bug — FSDP1/FSDP2 API 不兼容。**

- `_fsdp_wrapped_module` 是 FSDP1（`torch.distributed.fsdp.FullyShardedDataParallel`）的内部属性，用于访问被包装的原始模块。
- v9b 使用 FSDP2（composable API，`fully_shard`），模型被就地修改为 `FSDPQwen3ForCausalLM`，**没有 `_fsdp_wrapped_module` 属性**。
- FSDP2 的模块可以直接访问原始属性，不需要 unwrap。

**不是 OOM。** GPU 内存空闲（4×RTX PRO 6000 96GB 全部 0MiB 占用），进程已退出。

### 为何 val_before_train 通过但训练崩溃

- `val_before_train` 只做 generation（推理），不调用 `compute_log_prob`。
- 训练第一步需要计算 log prob 做 policy gradient，此时触发 `compute_log_prob` → 访问 `_fsdp_wrapped_module` → 崩溃。

### 同一方法中的其他 FSDP1 遗留问题

`dp_actor.py` 中 `compute_log_prob` 还有两处 FSDP1 API 调用（`FSDP.summon_full_params`），如果 `is_peft_model=True` 会触发，但本实验不用 LoRA，修复 line 223 后暂不会遇到。仍建议一并处理。

## 建议修复方案

**方案 A（最小改动，推荐）：** 用 `hasattr` 兼容 FSDP1/FSDP2：

```python
# dp_actor.py line 223
if hasattr(self.actor_module, '_fsdp_wrapped_module'):
    # FSDP1
    is_peft_model = not no_lora and isinstance(self.actor_module._fsdp_wrapped_module, PeftModel)
else:
    # FSDP2 or unwrapped
    is_peft_model = not no_lora and isinstance(self.actor_module, PeftModel)
```

**方案 B（更彻底）：** 同时修复 `FSDP.summon_full_params` 调用：

```python
# 替换 FSDP.summon_full_params 为兼容写法
if isinstance(self.actor_module, FSDPModule):
    # FSDP2: no summon needed, params are accessible
    self.actor_module.merge_adapter()
else:
    with FSDP.summon_full_params(self.actor_module):
        self.actor_module.merge_adapter()
```

## 关键事实

| 项目 | 值 |
|------|-----|
| 失败类型 | 代码 bug（非 OOM） |
| 失败时机 | 训练第一步 compute_log_prob |
| 出错文件 | `ragen/workers/actor/dp_actor.py:223` |
| GPU 峰值内存 | 未达到 OOM，无峰值数据 |
| W&B run 7xfef8p6 | 未记录到训练 step 数据（崩溃在第一步） |
| GPU 状态 | 4×RTX PRO 6000 96GB 全部空闲 |

## 修复后重试 checklist

1. 修改 `dp_actor.py:223` 兼容 FSDP2
2. 审查同文件中所有 `FSDP.summon_full_params` 和 `_fsdp_wrapped_module` 引用
3. 同步代码到服务器
4. dry-run 验证（至少跑完第一个 training step）
