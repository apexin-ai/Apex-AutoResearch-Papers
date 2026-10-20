# fix d080 17855 qwen35 restart

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_d080_17855_qwen35_restart_20260519T002604_result.json`
- **Structured JSON:** [`be22c93c5006c06e3be7.json`](../../sessions/be/be22c93c5006c06e3be7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两台服务器都已 patch。

---

## D080 汇报

### 1. Qwen3.5 dtype 测试结果
| 参数 | 实际加载 dtype |
|---|---|
| `torch_dtype=None` | **bfloat16** |
| `torch_dtype=torch.float32` | **bfloat16**（已弃用，被忽略） |
| `dtype=torch.float32` | **bfloat16**（transformers 5.8.1 对 Qwen3.5 无效） |
| `.to(dtype=torch.float32)` | **float32**（有效） |

**根因**：Qwen3.5 的 safetensors 以 bfloat16 存储权重，transformers 5.8.1 的 `from_pretrained` 对 `dtype`/`torch_dtype` 参数均不生效。必须显式 `.to(dtype=...)` 转换。

### 2. Kill 验证
- 旧 PID 55423 已 kill，`ps` 确认无进程
- cuda:1 显存 26831 MiB → 0 MiB（已释放）
- 旧 tmux session `qwen35_08b_fp32` 已销毁
- 旧数据 `results/generalize/qwen35_08b_wiki_a100_s42_fp32/` 已清除

### 3. 新实验
- **exp_id**: `qwen35_08b_wiki_a100_s42_v2`
- **PID**: 74455
- **tmux session**: `qwen35_08b_wiki_a100_s42_v2`
- **output_dir**: `results/generalize/qwen35_08b_wiki_a100_s42_fp32_v2`

### 4. 训练状态
- `Casting model from torch.bfloat16 to torch.float32` 已确认生效
- 进入 Generation 0 synthetic 数据生成阶段，无 NaN/Error
- cuda:1 占用 4435 MiB（fp32 0.8B 模型合理）
- fp32 推理速度比 bfloat16 慢，generation 阶段耗时较长属正常

### 5. 额外修复
- `iterative_train.py` 已在 westd-17855 和 westd-19828 同步 patch（`model.to(dtype=target_dtype)` 强制转换）
- 新 md5: `5b37837e7a6378f42bcb740f8f5e4773`（westd-17855）

---
