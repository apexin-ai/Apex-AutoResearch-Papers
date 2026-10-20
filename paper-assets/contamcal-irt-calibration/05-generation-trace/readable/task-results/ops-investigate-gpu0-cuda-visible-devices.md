# ops investigate gpu0 cuda visible devices

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_investigate-gpu0-cuda-visible-devices_20260515T055037_result.json`
- **Structured JSON:** [`56164a3a292a76e0099a.json`](../../sessions/56/56164a3a292a76e0099a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

排查完成。以下是根因分析。

---

## 根因分析

### 问题链

**v2 实验跑在 GPU 0 而非 GPU 3 的原因是 `--gpu` 参数与 `CUDA_VISIBLE_DEVICES` 的双轨冲突。**

`submit_training_job` MCP 工具（tmux 后端）在 tmux session 中**正确设置了** `export CUDA_VISIBLE_DEVICES=3`（代码位于 `/home/ubuntu/agent-ml-research/core/tools/execution_backends/tmux_backend.py:52`）。

但旧版 `exp001/train_sft.py`（未纳入 git 跟踪）有一个 `--gpu` 参数，它在 Python 内部**覆写了** `CUDA_VISIBLE_DEVICES`。如果训练命令未传 `--gpu 3`（或 `--gpu` 默认值为 `0`），就会把 tmux 已设好的 `CUDA_VISIBLE_DEVICES=3` 覆写为 `0`，导致 PyTorch 跑在物理 GPU 0。

git 提交 `dd81ae2`（今天 13:00:46）的 commit message 直接确认了这一点：

> *"The --gpu argument was silently overwriting CUDA_VISIBLE_DEVICES, causing experiments to run on wrong GPUs. GPU selection now relies solely on CUDA_VISIBLE_DEVICES set by the caller."*

### --gpu 参数实际行为

ROADMAP 说"args.gpu 解析但未用"——这描述的是**对 GPU 选择无正面作用**。旧代码确实解析了 `--gpu`，但用法有误（覆写环境变量而非配合它），等效于"死代码"，因为它的存在只制造 bug、不解决问题。

**当前版本**（`dd81ae2` 之后）：`--gpu` 已被完全移除。`train_sft.py` 不再处理 GPU 选择，完全依赖调用方设置 `CUDA_VISIBLE_DEVICES`。

### 修复状态

`dd81ae2` 修复了 `train_sft.py`，但**两个 shell 脚本仍有残留问题**：

1. **`exp001/train_and_eval.sh:89`** — 训练调用仍传 `--gpu "$GPU"` 且不设 `CUDA_VISIBLE_DEVICES`：
   ```bash
   python3 "$SCRIPT_DIR/train_sft.py" \
       --gpu "$GPU" \    # 新版 train_sft.py 不接受此参数，会报错
   ```
   eval 调用（第 103 行）正确使用了 `CUDA_VISIBLE_DEVICES="$GPU"`。

2. **`exp001/run_exp001.sh` Phase 3（训练）** — 同样传 `--gpu "$gpu_id"` 但不设 `CUDA_VISIBLE_DEVICES`。Phase 4（eval）正确。

### 修复建议（不改代码）

1. **`train_and_eval.sh`**：训练调用删掉 `--gpu "$GPU"`，加上 `CUDA_VISIBLE_DEVICES="$GPU"` 前缀，与 eval 调用保持一致。
2. **`run_exp001.sh` Phase 3**：同上。
3. **今后所有训练调用**：统一用 `CUDA_VISIBLE_DEVICES` 环境变量控制 GPU，不通过 `--gpu` 参数。通过 `submit_training_job` 提交的任务不受影响（tmux 后端已正确设置环境变量）。

---
