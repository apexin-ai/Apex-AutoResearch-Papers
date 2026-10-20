# code plan a bugfix

**collapse aware mixing** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan_a_bugfix_20260514T033515_result.json`
- **Structured JSON:** [`1ed6ad13e1636fa3e5a4.json`](../../sessions/1e/1ed6ad13e1636fa3e5a4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 报告

### 1. 修改清单

| # | 文件 | 改动 | 行号 |
|---|------|------|------|
| 1 | `controlled_pipeline.py:27` | 添加 `import random` | 新增 |
| 1 | `controlled_pipeline.py:29` | 添加 `import numpy as np` | 新增 |
| 1 | `controlled_pipeline.py:337-342` | `run_controlled_pipeline()` 函数开头添加 seed 设置：`torch.manual_seed`, `torch.cuda.manual_seed_all`, `np.random.seed`, `random.seed`, `cudnn.deterministic=True` | 新增 |
| 2 | `controlled_pipeline.py:199` | DataLoader `num_workers=2` → `num_workers=0`（方案 A，单进程确定性） | 修改 |
| 3a | `main_experiment.py:1-5` | docstring 标记 `[DEPRECATED]`，添加 `DeprecationWarning` | 修改 |
| 3b | `config.py:1-5` | docstring 从 "spectral effective rank" 更新为 "n-gram entropy + PI controller" | 修改 |

### 2. 集成测试结果：**通过**

- 模型：EleutherAI/pythia-1b（离线缓存）
- 参数：`seed=99, num_generations=1, tokens=50K, mode=pi_controller`
- G0 训练 12 步，checkpoint-6 和 checkpoint-12 正常保存
- G0 baseline entropy 测量：`unigram_entropy=6.7401 → setpoint=6.0661`
- `control_log.jsonl` 正确写入（含 generation/event/entropy/setpoint/mode）
- PI controller `set_baseline` 正常工作
- 无报错退出，`CONTROLLED PIPELINE COMPLETE`

### 3. 清理

`/tmp/plan_a_integration_test` 和测试日志已删除。

---
