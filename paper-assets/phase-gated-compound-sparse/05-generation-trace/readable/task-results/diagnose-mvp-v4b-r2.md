# diagnose mvp v4b r2

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_mvp_v4b_r2_20260513T234352_result.json`
- **Structured JSON:** [`493fc41135b4b1631d08.json`](../../sessions/49/493fc41135b4b1631d08.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结论

**根因：GPU 资源竞争——两个 importance profiling 进程共享同一 GPU 导致 CUDA OOM 静默崩溃。**

### 事件链

1. **07:20** — 旧 v4a/v4b/v4c 进程启动在 GPU 0/1/2，各占 ~33 GB（importance 模式，`output_attentions=True`）
2. **07:27** — 代码同步到服务器（添加 `--masking_method` 参数）
3. **07:27-28** — r2 进程在**相同的 GPU 0/1/2** 上启动，各加载第二份 7B 模型（~14 GB）
4. **07:31-33** — r2 进程处理到 problem 3-4 时，调用 `compute_dense_forward_with_importance`（`output_attentions=True`），产生 ~12-20 GB 注意力张量
5. 两个进程同时处于 attention forward 峰值时，GPU 内存需求：
   - 旧进程：33 GB 基础 + ~15 GB attention 峰值 ≈ 48 GB
   - r2 进程：14 GB 模型 + ~15 GB attention = 29 GB  
   - **合计 ~77+ GB / 95 GB GPU** → 加上碎片化和 CUDA 运行时开销，超出容量
6. CUDA 驱动级 OOM → 进程被 SIGABRT/SIGKILL → 无 Python traceback，无 dmesg 记录

### 为什么其他实验正常

| 实验 | GPU 共享？ | 代码路径 | 结果 |
|------|-----------|---------|------|
| 旧 v4a/b/c | 独占 | importance + output_attentions | ✅ 正常运行 |
| random r2 (GPU 3) | 独占 | `compute_dense_ce_losses`（无 output_attentions） | ✅ 正常运行 |
| 我的 stress test | 独占（旧进程已退出） | importance | ✅ 通过 5 个问题 |
| **r2 importance** | **共享（与旧 v4）** | **importance + output_attentions** | ❌ 崩溃 |

### 关键证据

- r2 实验 problem 1 耗时 **175 秒**（GPU 竞争），独占时同样的 problem 只需 **49 秒** — 3.5x 减速
- `output_attentions=True` 对 2048-token 序列产生 **~12 GB** 注意力张量（28层 × 28头 × seq² × 4B）
- 两进程共享 95 GB GPU 时，并发峰值内存超过可用容量

```json
{"root_cause":"GPU 0/1/2 上同时运行两个 importance profiling 进程（旧 v4 + r2），compute_dense_forward_with_importance(output_attentions=True) 产生 ~12-20GB 注意力张量，并发峰值超出 95GB GPU 容量导致 CUDA 驱动级 OOM，进程被静默终止","error_type":"resource","fix_steps":["先 kill 残留的旧进程再启动新实验：kill 27689 28083 28452（已自行退出）","重新启动 r2 实验，确保每个 GPU 只有一个 profiling 进程","可选：在启动脚本中加入 GPU 占用检查：nvidia-smi --query-compute-apps=pid --format=csv,noheader | grep -q . && echo 'GPU busy'"],"can_auto_fix":true}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "root_cause": "GPU 0/1/2 上同时运行两个 importance profiling 进程（旧 v4 + r2），compute_dense_forward_with_importance(output_attentions=True) 产生 ~12-20GB 注意力张量，并发峰值超出 95GB GPU 容量导致 CUDA 驱动级 OOM，进程被静默终止",
    "error_type": "resource",
    "fix_steps": [
      "先 kill 残留的旧进程再启动新实验：kill 27689 28083 28452（已自行退出）",
      "重新启动 r2 实验，确保每个 GPU 只有一个 profiling 进程",
      "可选：在启动脚本中加入 GPU 占用检查：nvidia-smi --query-compute-apps=pid --format=csv,noheader | grep -q . && echo 'GPU busy'"
    ],
    "can_auto_fix": true
  }
}
```

</details>

---
