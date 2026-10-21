# diagnose exp022 parallelism bottleneck

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp022-parallelism-bottleneck_20260515T034404_result.json`
- **Structured JSON:** [`87dfc0324b915ee0bb53.json`](../../sessions/87/87dfc0324b915ee0bb53.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完毕。以下是完整报告。

---

## exp022 GRPO 并行度瓶颈分析报告

### 1. 当前训练速度

| Step | timing_s/gen | timing_s/step | response_length/mean | throughput (tok/s) |
|------|-------------|---------------|---------------------|--------------------|
| 1 | 161.2s | 208.4s | 3280.9 | 503.7 |
| 2 | ~501s | 534.7s | — | 216.0 |
| 3 | 329.0s | 362.2s | 3842.6 | 339.5 |

- 进程运行 29 分钟，完成 4/30 steps（13%）
- 按当前速度（~400s/step），剩余 26 steps 需要约 2.9 小时
- step 间速度波动大（208s → 535s → 362s），gen 阶段占每步 77-93%

### 2. GPU 利用率

- 两块 GPU 各占 ~48.5GB/97.9GB（49.6%）
- 查询时 GPU 利用率均为 0% — 说明正处于 env stepping 或 CPU 计算阶段
- vLLM 配置 `gpu_memory_utilization: 0.4`，KV cache 空间偏小

### 3. 并行度瓶颈定位

**根因确认：`envs.yaml` 中 AlfworldSG 的 `parallel_friendly: false` + `max_workers: 1`**

文件：`/root/cost-verify-agent-rl/RAGEN/config/envs.yaml`，AlfworldSG 条目：
```yaml
AlfworldSG:
    parallel_friendly: false
    max_workers: 1
```

**执行路径**（`es_manager.py:265-269`）：
```python
parallel_friendly = sample_entry.get('parallel_friendly', False)
max_workers = sample_entry.get('max_workers', 1)
executor = self._executors.get(tag) if parallel_friendly and max_workers > 1 else None
if executor is None or len(items) == 1:
    for idx, env_input in items:  # ← 64 个 env 串行执行
        results[idx] = _process_env_input(env_input)
```

当 `parallel_friendly=false` 或 `max_workers=1`，64 个 env step 在单线程 for 循环中串行执行。每个 multi-turn rollout step 包含 ~22-28 轮，每轮串行 step 64 个 env。

**为什么 ALFWorld 被标记为不可并行**：`alfworld/env.py` 中使用了全局 `_RAW_ENV_CACHE`：
```python
_RAW_ENV_CACHE = {}  # 按 (config_file, mode) 缓存 AlfredTWEnv
```
所有 ALFWorld env 实例共享同一个 `raw_env` 对象。`reset()` 调用 `self.raw_env.init_env(batch_size=1)` 修改共享状态 — 非线程安全。

但 **`step()` 调用使用的是每个实例独立的 `self.alfred_env`**，可能是线程安全的。

### 4. 建议修改方案

**方案 A（推荐）：修复线程安全 + 开启并行**

1. 修改 `alfworld/env.py`：移除 `_RAW_ENV_CACHE` 或为每个实例创建独立 `raw_env`
2. 修改 `envs.yaml` 中 AlfworldSG：
   ```yaml
   parallel_friendly: true
   max_workers: 8  # 或 16，取决于 CPU 核数
   ```
3. 风险：中等。需要验证 `AlfredTWEnv.init_env()` 在独立实例间无共享状态
4. 预期收益：env step 时间缩减 8-16x

**方案 B（低风险）：仅增加 vLLM 吞吐**

1. `gpu_memory_utilization: 0.4` → `0.6`（当前 49.6% 显存占用有余量）
2. 不需修改代码
3. 风险：低。但需要确认 FSDP 训练和 vLLM 的显存不冲突
4. 预期收益：gen 阶段提速 20-40%（更大 KV cache → 更好 batch 调度）

**方案 C（综合）：A + B 同时实施**

### 5. 是否需要 kill 重启

**必须 kill 重启。** 原因：
- `envs.yaml` 在进程启动时加载，`ThreadPoolExecutor` 在 `__init__` 中创建
- `gpu_memory_utilization` 是 vLLM 引擎初始化参数
- 两项改动都无法热更新

当前进度 4/30 steps（13%），已运行 29 分钟。重启损失不大。

### 附注：val 配置疑似违反 C003

exp022 val 配置：`env_groups: 4, group_size: 1` → 4 episodes。C003 要求 val ≥16 episodes。

---
