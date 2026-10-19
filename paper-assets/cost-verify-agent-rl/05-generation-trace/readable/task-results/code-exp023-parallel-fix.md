# code exp023 parallel fix

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp023-parallel-fix_20260515T035034_result.json`
- **Structured JSON:** [`b9afa45d823a87d72a9d.json`](../../sessions/b9/b9afa45d823a87d72a9d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 3 个测试通过 (6.2s)。汇总产出：

---

## 产出汇总

### 1. env.py 修改 (`RAGEN/ragen/env/alfworld/env.py`)
**改了什么：**
- 添加 `import threading`
- 添加 `_RAW_ENV_LOCK = threading.Lock()` 保护 `_RAW_ENV_CACHE`
- `_get_cached_raw_env()` 内用 `with _RAW_ENV_LOCK:` 包裹缓存读写，消除竞态条件
- `reset()` 中移除 `np.random.seed(seed)` / `random.seed(seed)` 全局状态修改（不再污染全局随机数）
- 原文件已备份为 `env.py.bak`

**为什么：** 原实现中多 worker 并发调用 `_get_cached_raw_env()` 时，check-then-write 不是原子操作，可能导致重复创建或部分初始化的 env 被另一线程读取。

### 2. Smoke test 结果：PASS
- Test 1: 4 线程并发 `__init__`，确认只创建 1 个 `AlfredTWEnv`（缓存命中），每个实例的 `game_files` 是独立副本
- Test 2: 2 个 env 独立 reset + step
- Test 3: 交替操作两个 env，验证无状态泄漏

### 3. envs.yaml 修改 (`RAGEN/config/envs.yaml`)
- 行 378: `AlfworldSG.parallel_friendly: false` → `true`
- 行 379: `AlfworldSG.max_workers: 1` → `4`

### 4. vLLM 配置修改
- `_alfworld_exp023_grpo_parallel.yaml` 行 50: `gpu_memory_utilization: 0.4` → `0.6`

### 5. exp023 配置
- 路径: `/root/cost-verify-agent-rl/RAGEN/config/_alfworld_exp023_grpo_parallel.yaml`
- 改动: experiment_name → `exp023-alfworld-grpo-parallel`，log/ckpt 目录 → `exp023/`，gpu_memory_utilization → 0.6
- 其他参数与 exp022 一致（exp021 checkpoint, LR=5e-7, kl_loss_coef=0.5, 30 steps）

### 6. 所有修改的文件
| 文件 | 操作 |
|------|------|
| `RAGEN/ragen/env/alfworld/env.py` | 线程安全修复 |
| `RAGEN/ragen/env/alfworld/env.py.bak` | 原文件备份 |
| `RAGEN/config/envs.yaml` | AlfworldSG 并行配置 |
| `RAGEN/config/_alfworld_exp023_grpo_parallel.yaml` | 新建 exp023 配置 |
| `tests/test_env_thread_safety.py` | 新建 smoke test |

---
