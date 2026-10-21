# code plan009 llama prep

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan009_llama_prep_20260520T054548_result.json`
- **Structured JSON:** [`d5e7ff7f4882b09ad1f9.json`](../../sessions/d5/d5e7ff7f4882b09ad1f9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### Step 1: 模型状态
**已存在**，路径 `/root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-8B-Instruct/`
- 4 个 safetensors 分片 (4.7G + 4.7G + 4.6G + 1.1G ≈ 15G)
- tokenizer、config 等配置文件完整，无需下载

### Step 2: 代码适配
**已完全通用化，无需任何代码修改：**

| 组件 | 适配方式 |
|------|---------|
| `turn_utils.py` | `get_turn_markers()` 自动检测 `llama3` / `chatml` 格式，`_parse_turns_llama3()` 已实现 |
| `threadgate.py` | `ThreadGatedModel(model_name=...)` 动态读取 `hidden_size`(4096) / `num_hidden_layers`(32)，无硬编码 |
| `train_phase2.py` | `--model` 参数覆盖 `MODEL_NAME`，直接传 Llama 路径即可 |
| `config_llama.py` | 已存在，继承 `config.py` 并覆盖 `MODEL_NAME` 为 Llama 路径 |
| `run_phase1_gar_llama.py` | Phase 1 GAR 诊断脚本已存在 |
| `verify_llama_compat.py` | 兼容性验证脚本已存在（含 tokenizer/turn detection/gate hook/LoRA/GAR 7 项测试） |

### Step 3: 脚本列表

| 脚本 | Plan | 用途 |
|------|------|------|
| `scripts/launch_llama_phase1_gar_diag.sh` | 009 | Phase 1 GAR baseline 测量（eval only，~0.5h） |
| `scripts/launch_llama_tg.sh` | 010 | ThreadGate 训练，超参与 Qwen v7 一致 |
| `scripts/launch_llama_lora.sh` | 011 | LoRA-only baseline 训练 |

所有脚本 seed=42，输出至 `runs/phase2_llama_*` 目录。未启动任何训练。

---
