# diagnose mvp v4 r2 batch

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_mvp_v4_r2_batch_20260513T234444_result.json`
- **Structured JSON:** [`0e2779b2553499e4bdac.json`](../../sessions/0e/0e2779b2553499e4bdac.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

## 根因分析

**GPU 0-2 上存在更早的僵尸实验，r2 实验因 GPU 内存竞争被静默杀死。**

时间线：
| 时间 | 事件 |
|------|------|
| 07:00 | 旧 v4a/v4b/v4c 输出目录创建 |
| 07:22 | 旧实验进程启动 (PID 27689/28083/28452)，**至今仍在运行** |
| 07:27-28 | r2 实验在同一 GPU 上叠加启动 (PID 31119/31481/31839) |
| 07:31-33 | r2 实验在处理第 3-4 题时静默死亡，无 traceback |

**证据：**

1. GPU 0-2 当前进程是**旧实验**（非 r2），cmdline 确认：
   - PID 27689 → `profiling_output_v4a --sparsity_levels 0.1`（单一稀疏度，无 `--masking_method`）
   - PID 28083 → `profiling_output_v4b --sparsity_levels 0.2`
   - PID 28452 → `profiling_output_v4c --sparsity_levels 0.3`
   - 这些旧实验的输出目录**全部为空**，说明它们本身也有问题

2. r2 实验叠加后，每 GPU 两个进程各需 ~30-33GB（当前单进程占用），总计 ~60-66GB。在长序列生成（1000-1700 tokens）+ importance masking 的注意力计算峰值下，97GB GPU 内存被耗尽。

3. 无 Python traceback 的静默死亡 = CUDA OOM 发生在 C++ 扩展层（model forward / attention kernel），触发 SIGKILL 或段错误，Python 来不及捕获异常。

4. `random_r2` (cuda:3) 正常运行（已到 13/50），因为 GPU 3 只有它一个进程，且 random masking 不需要额外的 importance score 计算，内存占用更低（19GB vs 32GB）。

```json
{"root_cause":"GPU 0-2 上旧实验 v4a/v4b/v4c (PID 27689/28083/28452, 启动于 07:22) 未被终止，r2 实验叠加到同一 GPU 导致显存耗尽，进程被 SIGKILL 静默杀死。旧实验输出目录为空且参数不同（单一 sparsity, 无 masking_method flag），属于僵尸进程。","error_type":"resource","fix_steps":["kill 27689 28083 28452  # 终止旧的僵尸实验","确认 GPU 0-2 显存释放: nvidia-smi","重新启动 r2 实验: mvp_v4a_r2, mvp_v4b_r2, mvp_v4c_r2"],"can_auto_fix":true,"random_r2_alive":true}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "root_cause": "GPU 0-2 上旧实验 v4a/v4b/v4c (PID 27689/28083/28452, 启动于 07:22) 未被终止，r2 实验叠加到同一 GPU 导致显存耗尽，进程被 SIGKILL 静默杀死。旧实验输出目录为空且参数不同（单一 sparsity, 无 masking_method flag），属于僵尸进程。",
    "error_type": "resource",
    "fix_steps": [
      "kill 27689 28083 28452  # 终止旧的僵尸实验",
      "确认 GPU 0-2 显存释放: nvidia-smi",
      "重新启动 r2 实验: mvp_v4a_r2, mvp_v4b_r2, mvp_v4c_r2"
    ],
    "can_auto_fix": true,
    "random_r2_alive": true
  }
}
```

</details>

---
