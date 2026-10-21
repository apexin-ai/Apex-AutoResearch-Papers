# exp029_seed3_episode 失败诊断

## 失败原因

**配置类型错误**：Hydra override `seed=42` 将 `config.seed` 设为 `int`，但 `es_manager.py:44` 期望 `seed` 是 dict（含 `train`/`val` 键）。

```
AttributeError: 'int' object has no attribute 'get'. Did you mean: '_return_value'?
```

### Traceback 关键路径
```
train.py:325  → trainer.init_agent_proxy()
agent_trainer.py:536  → LLMAgentProxy(...)
agent_proxy.py:195  → EnvStateManager(config, mode="train")
es_manager.py:44  → self.base_seed = seed_cfg.get(mode, None)  ← crash here
```

### 根因对比

| 实验 | seed 配置 | 结果 |
|------|-----------|------|
| exp029_episode_level (parent) | 无 seed 字段（默认 None） | 正常 |
| exp029_seed3_episode | `seed=42`（int） | **crash** |
| exp029_seed3_v2 | `seed: {train: 42, val: 123}`（dict） | 正在运行 |

`es_manager.py:44` 的逻辑：
```python
seed_cfg = getattr(self.sys_config, "seed", None)
if seed_cfg is not None:
    self.base_seed = seed_cfg.get(mode, None)  # int 没有 .get()
```

## 运行时间

- 启动即失败（初始化阶段 crash，未进入训练循环）
- 无 checkpoint 产出
- 无有效 W&B metrics

## GPU / 磁盘状态

- GPU 0,1：空闲（3MiB）
- GPU 2,3：被 v2 实验占用（~48GB each，ray::WorkerDict）
- 磁盘：46% used（14G/30G），正常

## 是否可重试

不需要。**v2 已修复并正在运行**：
- 日志：`/root/runs/cost-verify-agent-rl/exp029_seed3_v2.log`
- W&B run：`exp029-seed3-episode-level`（run ID: `0t58u17b`）
- 修复方式：将 `seed=42` 改为 `seed: {train: 42, val: 123}`

## 建议

1. **代码层面**：`es_manager.py:44` 应增加 `int` 类型兼容处理，避免同类问题复发：
   ```python
   if isinstance(seed_cfg, int):
       self.base_seed = seed_cfg
   elif seed_cfg is not None:
       self.base_seed = seed_cfg.get(mode, None)
   ```
2. **流程层面**：seed 复现实验的启动脚本应复用 parent config 的 seed 格式（dict），通过 `seed.train=3` 覆盖具体值，而非 `seed=3` 替换整个结构。
