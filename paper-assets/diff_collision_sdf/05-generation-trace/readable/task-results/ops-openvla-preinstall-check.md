# ops openvla preinstall check

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_openvla_preinstall_check_20260525T145148_result.json`
- **Structured JSON:** [`284e53da1ae9b72052aa.json`](../../sessions/28/284e53da1ae9b72052aa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 检查结果

### Eval 脚本
**不存在。** `eval_safelibero_openvla.py` 未找到。现有 eval 脚本：
- `eval_safelibero.py`
- `eval_pi05_safelibero.py`

### 核心依赖

| 包 | 状态 | 版本 |
|---|---|---|
| transformers | ✅ 已装 | 4.53.2 |
| timm | ✅ 已装 | 1.0.27 |
| accelerate | ✅ 已装 | 1.13.0 |
| flash_attn | ✅ 已装 | 2.8.3 |
| prismatic | ❌ 未装 | — |

### 模型权重
**下载未完成。** `/root/autodl-tmp/openvla-7b-raw/` 有 3 个 safetensors 文件（共 ~15GB），但均有 `.aria2` 残留控制文件，表明下载中断。HF cache 中仅有 config/tokenizer，无权重。

### 待完成清单
1. **创建** `eval_safelibero_openvla.py` eval 脚本
2. **安装** `prismatic` 包（OpenVLA 核心依赖）
3. **重新下载** openvla-7b 模型权重（清理 `.aria2` 文件后重下，或用 HF hub 下载完整版）

---
