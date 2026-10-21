# diagnose cwm8b v5 gpu2 check

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_cwm8b-v5-gpu2-check_20260515T175703_result.json`
- **Structured JSON:** [`0c099b8aac273f661d56.json`](../../sessions/0c/0c099b8aac273f661d56.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### 任务 1：GPU 2 状态

| GPU | 显存 | 利用率 |
|-----|------|--------|
| 0 | 18,477 MiB | 78% |
| 1 | 27,313 MiB | 88% |
| **2** | **0 MiB** | **0%** |
| 3 | 22,527 MiB | 88% |

**PID 400279/400280 存活**（运行 6 分钟），CPU 104%，RSS 4.6GB——正在加载 Qwen3-8B 模型到内存，尚未上 GPU。日志最后一条停在 `01:56:53`（数据 truncation 报告），之后进入模型加载阶段，无新输出是正常的。

**判断：进程正常，处于模型加载中间阶段，预计几分钟内 GPU 2 会出现显存占用。不需要 kill/重启。**

注意一点：当前运行的脚本是 `train_repo_cwm.py`，而非你重启命令中指定的 `train_repo_cwm_8b.py`。

### 任务 2：checkpoint-400

**checkpoint-400 存在**，内容完整：
- `adapter_model.safetensors` (61MB)
- `optimizer.pt` (123MB)
- `trainer_state.json`, `scheduler.pt`, `rng_state.pth` 等
- 创建时间：May 14 16:32

**全部现存 checkpoint（5 个）：**
- checkpoint-400
- checkpoint-4900
- checkpoint-5000
- checkpoint-5100
- checkpoint-5200

---
