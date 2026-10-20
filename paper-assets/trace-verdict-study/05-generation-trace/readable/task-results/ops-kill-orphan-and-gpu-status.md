# ops kill orphan and gpu status

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_kill-orphan-and-gpu-status_20260521T151558_result.json`
- **Structured JSON:** [`0ffdf96509b52aa989bf.json`](../../sessions/0f/0ffdf96509b52aa989bf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

没有任何进程持有 GPU 设备文件。GPU 0 的 ~49GB 占用是驱动/系统层面的残留，应该会在短时间内自动释放，或者下次有进程申请 CUDA context 时被回收。

---

**汇报：**

| 项目 | 状态 |
|------|------|
| PID 706059 (qwen1.5b_no_trace_seed42) | 已死，确认不存在 |
| PID 706833 (codellama_exception_only_seed42) | 已杀掉 |
| GPU 0 | 49175 MiB used / 48077 MiB free（残留显存，无活跃进程） |
| GPU 1 | 0 MiB used / 97252 MiB free（完全空闲） |
| 其他 GPU 进程 | 无（`nvidia-smi` compute apps 为空，`fuser /dev/nvidia*` 无结果） |

GPU 1 完全可用。GPU 0 的残留显存无进程关联，可以直接使用——新进程启动 CUDA context 时会正常分配。

---
