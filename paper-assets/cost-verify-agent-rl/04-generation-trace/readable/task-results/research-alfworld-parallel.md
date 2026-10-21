# research alfworld parallel

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_alfworld_parallel_20260513T230241_result.json`
- **Structured JSON:** [`5813091e6c9febdfd9df.json`](../../sessions/58/5813091e6c9febdfd9df.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调研完成。以下是报告。

---

## ALFWorld 并行采集限制调研报告

### 1. `parallel_friendly: False` 是技术限制还是保守默认？

**是真实的技术限制**，不仅是保守默认。存在三个具体的线程安全问题：

---

### 2. 具体限制代码和机制

#### 问题 A：`textworld.gym.utils.registry` 全局字典竞态

**文件**：`/root/miniconda3/lib/python3.12/site-packages/textworld/gym/utils.py`

```python
registry: dict[str, dict] = {}  # 模块级全局变量，无锁

def register_games(...) -> str:
    env_id = "tw-{}-v0".format(name) if name else "tw-v0"
    if env_id in registry:  # <-- 读
        base, _ = env_id.rsplit("-v", 1)
        versions = [int(...) for env_id in registry if ...]
        env_id = "{}-v{}".format(base, max(versions) + 1)  # <-- 非原子递增
    registry[env_id] = dict(...)  # <-- 写
    return env_id
```

`AlfredTXTEnv.reset()` 每次调用都走 `textworld.gym.register_game()` → `register_games()`（`ragen/env/alfworld/env.py:141`）。多线程并发 reset 时，版本号递增逻辑产生竞态：两个线程可能读到相同的 max version，写入同一个 env_id，后者覆盖前者。

#### 问题 B：`np.random.seed()` / `random.seed()` 全局随机状态

**文件**：`/root/cost-verify-agent-rl/RAGEN/ragen/env/alfworld/env.py:126-127`

```python
def reset(self, seed=None, mode=None):
    ...
    if seed is not None:
        np.random.seed(seed)   # <-- 设置全局随机状态
        random.seed(seed)      # <-- 设置全局随机状态
```

两个线程同时 reset 不同 seed，会互相覆盖全局随机状态，导致 game 选择不可复现，可能选到相同的 game file。

#### 问题 C：`_RAW_ENV_CACHE` 全局缓存竞态

**文件**：`/root/cost-verify-agent-rl/RAGEN/ragen/env/alfworld/env.py:12,67-71`

```python
_RAW_ENV_CACHE = {}  # 模块级全局变量，无锁

def _get_cached_raw_env(self, alfworld_mode: str) -> AlfredTWEnv:
    cache_key = (os.path.abspath(self.config.config_file), alfworld_mode)
    raw_env = _RAW_ENV_CACHE.get(cache_key)       # <-- 读
    if raw_env is None:
        raw_env = AlfredTWEnv(...)                 # <-- 慢操作：扫描文件系统
        _RAW_ENV_CACHE[cache_key] = raw_env        # <-- 写
    return raw_env
```

`AlfredTWEnv.__init__` 调 `collect_game_files()` 遍历整个数据目录（`os.walk` + 读每个 `traj_data.json`），两个线程可能同时创建重复实例。

---

### 3. 如何改成并行，需要改哪些代码

**方案 A：加锁（最小改动）**

| 文件 | 改动 |
|------|------|
| `ragen/env/alfworld/env.py` | 1) `_RAW_ENV_CACHE` 加 `threading.Lock`；2) `reset()` 中将 `np.random.seed(seed)` 改为 `np.random.RandomState(seed)` 局部 RNG；3) 将 `textworld.gym.register_game` + `make` 调用包在一个锁里 |
| `config/envs.yaml` | 改 `parallel_friendly: true, max_workers: 4-8` |

**风险**：
- register_game 的锁会序列化所有 reset，并行度取决于 reset vs step 的时间比
- textworld 内部可能还有未发现的全局状态

**方案 B：预创建环境池（推荐）**

在 `_init_env_instances` 时就为每个 env 实例预先 register_game + make 好，而不是在每次 reset 时重新创建。reset 时只调 `self.alfred_env.reset()` 而非重建整个环境。

| 文件 | 改动 |
|------|------|
| `ragen/env/alfworld/env.py` | 重构 `reset()`：不再每次 register_game + make，而是维护一个 game-file → env 的映射池，reset 时选 game 后直接 load |

**风险**：需理解 textworld 环境是否支持反复 load 不同 game file（需验证）

**方案 C：多进程替代多线程**

将 `es_manager.py:108` 的 `ThreadPoolExecutor` 改为 `ProcessPoolExecutor`。每个进程有独立的 `registry` 和全局随机状态。

**风险**：
- 环境状态需要跨进程序列化（textworld env 可能不 picklable）
- 进程间通信开销大
- 改动侵入性高

---

### 4. 预估工作量

| 方案 | 工作量 | 风险 |
|------|--------|------|
| A：加锁 | 2-4 小时 | 低，但并行增益可能有限（reset 仍串行） |
| B：环境池 | 4-8 小时 | 中，需验证 textworld 环境复用机制 |
| C：多进程 | 1-2 天 | 高，序列化问题可能无解 |

---

### 5. 更简单的加速方案

**RAGEN 的 rollout 瓶颈不在环境 step，在 LLM inference。** 每条 trajectory 50 步，每步调一次 LLM 生成。环境 step 本身是纯 CPU 文本操作，亚毫秒级。

更高效的加速路径：

1. **增大 vLLM batch size**：RAGEN 已经用 vLLM 做 batched inference，确保所有环境的 LLM 请求在同一 batch 里处理，而不是串行生成。这是最大的加速杠杆。
2. **增大 `group_size`**：增加每组的环境数量，让 vLLM 一次处理更多 prompt，提升 GPU 利用率。
3. **方案 A（加锁）+ 中等 max_workers（4）**：step 阶段可以真正并行（环境各自独立），只有 reset 阶段串行。由于 reset 只在 trajectory 开始时调一次，整体 rollout 速度受影响小。

**建议**：先验证当前 rollout 的时间分布（LLM inference vs env step），如果 env step 占比 <10%，并行环境收益有限。如果确认要做，方案 A 最稳妥。

---
