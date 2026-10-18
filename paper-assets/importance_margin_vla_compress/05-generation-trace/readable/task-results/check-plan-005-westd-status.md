# check plan 005 westd status

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_plan_005_westd_status_20260516T144751_result.json`
- **Structured JSON:** [`01430e82d3178b91d5bd.json`](../../sessions/01/01430e82d3178b91d5bd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

**plan_005_formal_bound 已失败退出，不在运行。**

### 状态总结

| 项目 | 状态 |
|------|------|
| 进程 | **未运行** — ps 中无 eval_formal_bound 相关进程 |
| GPU | 两块 RTX PRO 6000 Blackwell (98GB each)，**均空闲** (0 MiB / 0% utilization) |
| 日志 | `logs/plan_005_formal_bound.log`，63 行 |
| 结果文件 | 无 formal_bound 相关输出产物 |

### 失败原因

脚本在 `22:32:12` 加载完模型后崩溃：

```
File "eval_formal_bound.py", line 137, in main
    tokenizer = get_tokenizer_from_policy(model)
File "train.py", line 255, in get_tokenizer_from_policy
    model = policy.model
AttributeError: 'IMMSmolVLAWrapper' object has no attribute 'model'
```

`get_tokenizer_from_policy()` 尝试访问 `policy.model`，但 `IMMSmolVLAWrapper` 没有这个属性。需要修正属性访问路径。

### 其他在跑的进程

服务器上有另一个 worker 在跑数据集下载（`lerobot/libero_10` via LeRobotDataset，PID 195322）和 pip install LIBERO（PID 188321），与 plan_005 无关。

---
