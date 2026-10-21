# diagnose exp013d

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp013d_20260514T083812_result.json`
- **Structured JSON:** [`709f0672ce7e59f9cbc3.json`](../../sessions/70/709f0672ce7e59f9cbc3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

---

## exp013d 失败诊断结果

### 根因
**`RAY_object_store_memory=30GB` 修复从未生效。** Ray object_store 实际分配 70.36GB（默认值），与 exp013b 完全相同。

### 错误类型
**config_error** — 配置意图未落实到代码/启动参数中。

### 证据

1. **ray.init 实际参数**（日志第 19 行）：
   ```
   ray init kwargs: {'num_cpus': None, 'runtime_env': {'env_vars': {
     'TOKENIZERS_PARALLELISM': 'true', 'NCCL_DEBUG': 'WARN',
     'VLLM_LOGGING_LEVEL': 'WARN', 'RAY_DEBUG': 'legacy'}}}
   ```
   — 没有 `object_store_memory` 参数，env_vars 里也没有 `RAY_object_store_memory`

2. **Raylet 日志确认**：`Object store current usage 8e-09 / 70.3625 GB` — 70.36GB，不是 30GB

3. **Raylet 被 SIGKILL**（cgroup OOM killer），模型刚加载完（Rank 1 loaded actor model at 16:36:10）就崩了

4. `env_groups: 4` 确实生效了，但不够 — object_store 本身就多占了 40GB

### Traceback
```
ray.exceptions.ActorUnavailableError: The actor cbc9d79ed0b94caab056a5b801000000
is unavailable: The actor is temporarily unavailable: RpcError: RPC error:
Socket closed rpc_code: 14.
```
（Raylet 被杀后 actor 连接断开的间接错误）

### Checkpoint / Metrics
**无。** `/root/autodl-tmp/checkpoints/exp013d_grpo/` 不存在，训练在第一个 step 之前就崩溃了。

### 修复方案

两种方式（任选其一）：

**方式 A — Hydra config override**（推荐）：
启动命令加 `ray_kwargs.ray_init.object_store_memory=32212254720`（30GB in bytes），这会直接传给 `ray.init()`。

**方式 B — 启动脚本 export 环境变量**：
在 `python train.py` 之前加 `export RAY_object_store_memory=32212254720`。

方式 A 更可靠，因为它通过 `ray.init()` 参数显式设置，不依赖环境变量被 Ray 正确读取。

---
