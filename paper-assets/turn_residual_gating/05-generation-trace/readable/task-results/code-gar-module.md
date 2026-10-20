# code gar module

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_gar_module_20260518T044654_result.json`
- **Structured JSON:** [`7b77d15124a41b41298f.json`](../../sessions/7b/7b77d15124a41b41298f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个文件全部通过语法检查。

**已创建的文件：**

- **`config.py`** — 项目超参常量（模型名、LoRA rank、GAR 参数、训练配置等）
- **`turn_utils.py`** — 基于 `<|im_start|>`/`<|im_end|>` 的 turn 边界检测，提供 `detect_turn_boundaries`（完整 turn 结构解析、goal token 定位、assistant 末尾 token、turn distance/index map）和 `build_turn_features`（ThreadGate 所需的 turn distance / turn index / boundary mask）
- **`gar.py`** — `GARMeasurer` 通过 forward pre-hook 捕获 Q/K states 手动计算 attention weights（绕过 SDPA 不暴露 attention 的问题），支持 `measure_only=True`（detach，诊断用）和 `measure_only=False`（保留梯度，训练用）两种模式；`compute_gar_loss` 实现 L_GAR = Σ max(0, GAR(τ-1) - GAR(τ) - ε) 的 margin 惩罚

系统环境无 torch，语法检查已通过。实际 import 验证需在有 torch 的训练环境中执行。

---
