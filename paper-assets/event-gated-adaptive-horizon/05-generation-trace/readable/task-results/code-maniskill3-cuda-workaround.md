# code maniskill3 cuda workaround

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_maniskill3_cuda_workaround_20260515T142722_result.json`
- **Structured JSON:** [`4b4b2f0e1a57b5ca5888.json`](../../sessions/4b/4b4b2f0e1a57b5ca5888.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**修改内容** (`envs/maniskill.py`):

1. **`__init__` 中移除 CUDA_VISIBLE_DEVICES** — 在 `gymnasium.make()` 前 `os.environ.pop("CUDA_VISIBLE_DEVICES")`，原始值存入 `_cvd_stash`。SAPIEN 看到所有物理 GPU，避免 segfault。
2. **State-based env 使用 CPU render backend** — `render_backend="cpu"` 跳过 CUDA 渲染设备分配。
3. **`maniskill_target_device()` 函数** — 将原始 CVD 值转换为物理 GPU device string（如 `"cuda:2"`），供训练代码使用。
4. **补充 `act_space` / `obs_space` 属性** — 验证测试需要。

**验证结果**:
- `CUDA_VISIBLE_DEVICES=2`（不存在的 GPU）：通过（原来 segfault）
- 无 CVD / CVD=0：通过（无回归）
- GPU 显存：仅 GPU 0 增加 ~118 MiB（SAPIEN CUDA context），GPU 1 不受影响

**注意事项**: CVD 移除后 PyTorch 看到所有物理 GPU，训练代码需用物理 GPU index（`maniskill_target_device()` 或 `--device cuda:N`），不能假设 `cuda:0`。

报告已写入 `artifacts/maniskill3_cuda_workaround.md`。

---
