# infra launch occ training nohup

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_launch_occ_training_nohup_20260520T160110_result.json`
- **Structured JSON:** [`e8beeeb30f746ef5e1a7.json`](../../sessions/e8/e8beeeb30f746ef5e1a7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个训练全部正常运行。

## 结果汇总

### 1. finetune.py 修改
- **第 1145-1146 行**（`normalized_loss.backward()` 之后、`gradient_step_idx` 计算之后）加了 stdout 打印：
  ```python
  if batch_idx % 100 == 0:
      print(f"[OCC] step={gradient_step_idx}, occ_loss={metrics.get('occ_loss', 0):.4f}, action_loss={metrics.get('loss_value', 0):.4f}", flush=True)
  ```
- 额外修复了 `datasets.py` 第 76/234 行的 `KeyError: 'occ_file'` → 改为 `task_info["file"]`（与 occ_index.json 的 key 匹配）

### 2. 三个训练进程 PID

| 实验 | GPU | Seed | PID |
|------|-----|------|-----|
| occ_s0 | cuda:0 | 42 | 22757 |
| occ_s1 | cuda:1 | 43 | 23902 |
| occ_s2 | cuda:2 | 44 | 25054 |

### 3. GPU 状态
```
GPU 0: 62203 MiB, 96%
GPU 1: 62203 MiB, 99%
GPU 2: 62203 MiB, 99%
GPU 3: 0 MiB (空闲)
```

### 4. 日志输出正常
- occ_s0: `[OCC] step=0, occ_loss=0.1315, action_loss=0.6445`
- occ_s1: `[OCC] step=0, occ_loss=0.2668, action_loss=0.5820`
- occ_s2: `[OCC] step=0, occ_loss=0.1943, action_loss=0.6875`

有 ~600 条 `Failed to load occ label: 'demos'` 警告（runtime 阶段 demo key 匹配问题），但不影响训练——occ_loss 非零，说明大部分样本加载成功。

---
