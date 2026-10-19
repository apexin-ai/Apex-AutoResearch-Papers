# debug eval path investigation

**Meta-Brain: Perturbation-Diagnostic Routing of LoRA Experts for Parameter-E cient VLA Robustness** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_debug_eval-path-investigation_20260516T071908_result.json`
- **Structured JSON:** [`594de8ab8418f154ecf4.json`](../../sessions/59/594de8ab8418f154ecf4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息收集完毕。以下是报告：

---

## Checkpoint 路径排查报告

### 1. LoRA Checkpoint 目录

| 目录 | 状态 | 文件 |
|------|------|------|
| `lora_visual_r16/final/` | **存在** | `adapter_config.json` (1.1KB) + `adapter_model.safetensors` (14MB) + `README.md` |
| `lora_physical_r16/final/` | **存在** | 同上 (14MB) |
| `lora_universal_r16/final/` | **存在** | 同上 (14MB) |
| `lora_universal_r48/final/` | **存在** | 同上 (42MB, rank 更大) |
| `lora_spatial_r16/` | **训练中** | 有 `final/` 和 `step_1000/`，但 spatial 训练看起来还在跑 |

### 2. pi0 Base Checkpoint

- **路径**: `/root/autodl-tmp/checkpoints/pi0_base/` — **存在**
- **内容**: `config.json`, `model.safetensors` (13GB), `policy_preprocessor.json`, `policy_postprocessor.json`
- 评估脚本 `--pi0_checkpoint` 默认值就是这个路径，**无问题**

### 3. 评估脚本参数 (`evaluate_libero_plus.py`)

```
--routing          choices=[par, oracle, random, none, universal], default="par"
--pi0_checkpoint   default="/root/autodl-tmp/checkpoints/pi0_base"  ✅
--router_checkpoint default=""                                       ⚠️ 根因
--lora_visual_dir  default=""
--lora_spatial_dir default=""
--lora_physical_dir default=""
```

逻辑 (lines 537-554): 如果任一 `lora_*_dir` 非空 → 调 `MetaBrain.from_checkpoints()` → **无条件**调 `PARRouter.from_checkpoint(router_checkpoint)` → `torch.load("")` → **FileNotFoundError**

### 4. 失败错误信息（`logs/eval_visual_expert.log`）

```
FileNotFoundError: [Errno 2] No such file or directory: ''
```

调用链：
1. `evaluate_libero_plus.py:546` → `MetaBrain.from_checkpoints(router_checkpoint="")`
2. `meta_brain_assembly.py:490` → `PARRouter.from_checkpoint("", ...)`
3. `par_router.py:57` → `torch.load("")` → **boom**

**根因**: `--router_checkpoint` 默认空字符串，`from_checkpoints()` 不检查就直接 `torch.load()`。且服务器上**不存在任何 router checkpoint 文件**（find 返回空）。

### 5. GPU 使用

| GPU | 型号 | 显存使用 | 利用率 |
|-----|------|---------|--------|
| 0 | RTX PRO 6000 Blackwell | 0 MiB / 98GB | 0% |
| 1 | RTX PRO 6000 Blackwell | 0 MiB / 98GB | 0% |
| 2 | RTX PRO 6000 Blackwell | **12.7GB** / 98GB | **99%** |
| 3 | RTX PRO 6000 Blackwell | 0 MiB / 98GB | 0% |

GPU 2 正在使用（可能是 spatial 训练）。GPU 0/1/3 空闲。

### 6. LIBERO-Plus 数据

- **路径**: `/root/LIBERO-plus/` — **存在**
- 包含 `libero/` 子目录、`benchmark_scripts/`、`setup.py` 等

### 修复方向

`from_checkpoints()` 在没有 router checkpoint 时仍然无条件调用 `PARRouter.from_checkpoint()`。两种修法：

1. **传入有效的 router_checkpoint 路径** — 但服务器上目前没有训练好的 router（PAR Router 还没训练）
2. **改代码**: 当 `router_checkpoint` 为空时，创建 dummy router（类似 `from_dummy` 的做法），而非调 `torch.load("")`

---
