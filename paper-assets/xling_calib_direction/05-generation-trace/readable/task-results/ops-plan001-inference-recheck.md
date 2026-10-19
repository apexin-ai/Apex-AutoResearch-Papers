# ops plan001 inference recheck

**Shifting the Cross-Lingual Calibration Pareto Frontier: Probe-Based Calibration Transfer via CaCLR** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_plan001_inference_recheck_20260521T140414_result.json`
- **Structured JSON:** [`d51a03aafa74ede90e10.json`](../../sessions/d5/d51a03aafa74ede90e10.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**plan_001 失败。**

- **GPU**: 4 卡全部 0% 利用率，0 MiB 显存
- **Activation 文件**: 空目录，无产出
- **错误原因**: MarlinLinear `post_init()` 调用 `marlin_make_workspace_new(device)` 时，device 为 `meta` 而非 CUDA 设备。这是 GPTQ 量化模型 + `device_map="auto"` 在 `post_init` 阶段的已知冲突——权重还在 meta device 上时就尝试创建 Marlin workspace。

**根因**: `from_pretrained` 用 `device_map="auto"` 加载 GPTQ 量化的 Qwen3-235B 时，transformers 的 post-quantization 处理在模型 dispatch 到真实 GPU 之前就执行了 Marlin 后处理，导致 device 仍为 `meta`。

**修复方向**:
1. 显式设 `device_map` 为具体 GPU 映射（而非 `"auto"`），或
2. 升级 `gptqmodel` / `optimum` 到修复此 bug 的版本，或
3. 换用非 Marlin 后端（`disable_exllama=True` 或用 `auto-gptq` 的 cuda 后端）

需要我排查修复吗？

---
