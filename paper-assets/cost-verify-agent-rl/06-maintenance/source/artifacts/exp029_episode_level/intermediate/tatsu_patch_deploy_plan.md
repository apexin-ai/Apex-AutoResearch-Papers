# Tatsu Parallel Patch 部署方案

## 概述

启用 `patches/tatsu_parallel_fix.py` 使 ALFWorld env.step() 可并行执行，val 评估从 ~10min 降至 ~2.5min (4x speedup)。

---

## 部署步骤

### Step 1: 创建 `patches/__init__.py`

```bash
touch /root/cost-verify-agent-rl/RAGEN/patches/__init__.py
```

当前 `patches/` 目录没有 `__init__.py`，需要创建才能作为 Python package 被 import。

### Step 2: 在 `train.py` 顶部添加 patch import

文件: `/root/cost-verify-agent-rl/RAGEN/train.py`

在第 1 行 `import tempfile` 之后（第 2 行之后）插入:

```python
import patches.tatsu_parallel_fix  # noqa: F401 - thread-safe tatsu parsers
```

完整效果:
```python
import tempfile
tempfile.tempdir = "/root/autodl-tmp/tmp"

import patches.tatsu_parallel_fix  # noqa: F401 - thread-safe tatsu parsers

"""
Borrowed from verl.trainer.main_ppo.py
...
```

关键: 必须在任何 `textworld` import 之前执行。`train.py` 是入口点，放在最前面即可保证。

### Step 3: 修改 `config/envs.yaml` 中 `AlfworldSG` 的并行参数

文件: `/root/cost-verify-agent-rl/RAGEN/config/envs.yaml`

第 375-379 行，修改:
```yaml
  AlfworldSG:
    env_type: alfworld
    max_actions_per_traj: 50
    parallel_friendly: true    # false → true
    max_workers: 4             # 1 → 4
```

说明:
- `parallel_friendly: true` 触发 `es_manager.py` 为该 tag 创建 `ThreadPoolExecutor`
- `max_workers: 4` 在 2 GPU 环境下合理（不超过 CPU 核心数，避免 GIL 瓶颈）
- 如果 `AlfworldSG_Dense` 或 `AlfworldSG_SuccessGated` 也在使用，同样修改

### Step 4: 验证 (dry-run)

部署后、正式训练前，运行短测试确认 patch 生效:

```bash
cd /root/cost-verify-agent-rl/RAGEN
python -c "
import patches.tatsu_parallel_fix
print('Patch applied successfully')

# 验证 thread-local 生效
import threading
import textworld.envs.pddl.textgen as m
assert m._PARSER is None, 'Singleton should be nulled'
print('Singleton correctly disabled')
"
```

然后运行已有的并行测试:
```bash
cd /root/cost-verify-agent-rl/RAGEN
python patches/test_tatsu_parallel.py
```

预期输出: 8/8 passed。

### Step 5: 短 val 测试 (可选但推荐)

用 `val_before_train: True` 启动训练，观察第一轮 val:
- 确认无 `FailedToken` 或 `IndexError` 崩溃
- 确认 val 耗时 ~2.5min 而非 ~10min
- 确认 val 结果与串行一致（32 episodes, 分数应在同一范围）

---

## 不需要改动的部分

| 项目 | 原因 |
|------|------|
| 启动命令 | 不变，仍为 `python train.py --config-name=_alfworld_exp029_episode_level` |
| exp029 config yaml | 不需要改（并行参数在 `envs.yaml` 的 custom_envs 中） |
| `ragen/env/alfworld/env.py` | 不需要改（`_TW_LOAD_LOCK` 已处理 env 创建串行化） |
| `ragen/llm_agent/es_manager.py` | 不需要改（已有 `parallel_friendly` + `ThreadPoolExecutor` 逻辑） |

---

## 风险评估

| 风险 | 影响 | 缓解 |
|------|------|------|
| 内存增加 | 每线程 ~4KB × 4 parsers × 4 workers = ~64KB，可忽略 | 无需处理 |
| env 创建仍串行 | `_TW_LOAD_LOCK` 限制了初始化并行度 | 预期行为，仅 step() 并行 |
| 未知 textworld 状态共享 | 如果除 parser 外还有其他全局状态 | patch 已覆盖所有 4 个 singleton，test_tatsu_parallel.py 8/8 通过 |
| val 结果不可复现 | 并行执行顺序不确定 | ALFWorld 本身确定性不依赖执行顺序，各 env 独立 |

---

## 回滚方案

如果部署后出现问题:

1. **快速回滚**: 改回 `envs.yaml` 中 `parallel_friendly: false`，无需删除 patch import（patch 加载但不触发并行）
2. **完全回滚**: 同时删除 `train.py` 中的 `import patches.tatsu_parallel_fix` 行

---

## 执行命令汇总 (copy-paste ready)

```bash
# Step 1
touch /root/cost-verify-agent-rl/RAGEN/patches/__init__.py

# Step 2
sed -i '3a import patches.tatsu_parallel_fix  # noqa: F401' /root/cost-verify-agent-rl/RAGEN/train.py

# Step 3
sed -i 's/\(  AlfworldSG:\)/\1/' /root/cost-verify-agent-rl/RAGEN/config/envs.yaml
sed -i '/^  AlfworldSG:$/,/^  [A-Z]/{s/parallel_friendly: false/parallel_friendly: true/;s/max_workers: 1/max_workers: 4/}' /root/cost-verify-agent-rl/RAGEN/config/envs.yaml

# Step 4: 验证
cd /root/cost-verify-agent-rl/RAGEN && python patches/test_tatsu_parallel.py
```
