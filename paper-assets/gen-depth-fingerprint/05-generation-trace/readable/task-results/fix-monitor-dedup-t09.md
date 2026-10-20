# fix monitor dedup t09

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_monitor-dedup-t09_20260518T170204_result.json`
- **Structured JSON:** [`641240a045708ac2701b.json`](../../sessions/64/641240a045708ac2701b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部就位。汇报：

## 结果

### 1. 原脚本中是否存在 t=0.9 自动启动逻辑

**存在，在 tmux shell 脚本中。** `run_temp_olmo.sh` 和 `run_temp_qwen06.sh` 是串行脚本（`[1/2]` t=0.5 → `[2/2]` t=0.9 → feature extraction），t=0.5 完成后会自动在 GPU 0/1 上启动 t=0.9 generation，和 GPU 2/3 上已有的 `temp_olmo_t09`/`temp_qwen06_t09` 写同一输出文件。

**Monitor 脚本本身不启动 generation**，只做 feature extraction + LOGO classification。但 GPU 分配有误（olmo→GPU 2, qwen→GPU 3），会和 t=0.9 generation 抢 GPU。

### 2. 做了什么修改

| 文件 | 修改 |
|------|------|
| `run_temp_olmo.sh` | 删除 t=0.9 generation 和 feature extraction 部分，只保留 t=0.5 generation |
| `run_temp_qwen06.sh` | 同上 |
| `monitor_temp_pipeline.py` | GPU 分配改为 olmo→0, qwen→1（两个温度共享），更新 docstring |
| 运行中的 bash 进程 | `kill -STOP 27209/27221` 暂停 bash 脚本，python generation 不受影响 |

### 3. Monitor 重启状态

正常运行，正在监控 4 个 target 的 seed 数量（olmo_t05: 957, qwen06_t05: 643, olmo_t09: 83, qwen06_t09: 64）。

### 4. 确认不会重复启动 t=0.9

- Bash 脚本已 STOP（`T+` 状态），t=0.5 完成后不会继续执行 t=0.9
- Shell 脚本已改写，即使重新运行也不含 t=0.9
- Monitor 不含 generation 逻辑，只在数据就绪后触发 feature extraction
- t=0.9 generation 仅在 `temp_olmo_t09`（GPU 2）和 `temp_qwen06_t09`（GPU 3）上运行

---
