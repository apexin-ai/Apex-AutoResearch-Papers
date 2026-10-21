# exp qwen3 model fix

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_qwen3-model-fix_20260524T113009_result.json`
- **Structured JSON:** [`b20d4c580ff336a1fc93.json`](../../sessions/b2/b20d4c580ff336a1fc93.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报：

### 1. PID 49372
已终止。Qwen2.5-7B-Instruct 只下载了 1.7MB 元数据（无权重文件），残留已清理。

### 2. Qwen3-8B 模型状态
**服务器上不存在。** `/root/models/` 和 `/root/autodl-tmp/models/` 均无 Qwen3-8B。

### 3. collect_activations.py 默认模型路径
Line 104 默认值为 `Qwen/Qwen3-8B-Instruct`。

**问题：`Qwen/Qwen3-8B-Instruct` 不存在。** Qwen3 系列采用统一模型架构（thinking/non-thinking 模式合一），没有单独的 Instruct 变体。正确 ID：
- **`Qwen/Qwen3-8B`** — instruction-tuned（即代码需要的）
- `Qwen/Qwen3-8B-Base` — 纯预训练

代码中 line 104 应改为 `Qwen/Qwen3-8B`。

### 4. Qwen3 数据
**不存在。** `data/` 下只有 `gemma2/`、`gemma2_v2/`、`llama31/`，无 `qwen3/` 目录。

### 5. GPU 状态
**完全空闲。** NVIDIA RTX PRO 6000 Blackwell Server Edition, 98GB VRAM, 0MB 占用，无 GPU 进程。

### 6. 下载所需信息
- HuggingFace ID: **`Qwen/Qwen3-8B`**
- ModelScope ID: **`Qwen/Qwen3-8B`**（AutoDL 推荐用 ModelScope 下载更快）
- 预计大小 ~16GB

### 需要确认

1. **是否修正 `collect_activations.py:104`** 的默认值从 `Qwen/Qwen3-8B-Instruct` → `Qwen/Qwen3-8B`？
2. **是否现在启动 Qwen3-8B 下载？** 建议用 ModelScope 下载到 `/root/autodl-tmp/models/`。

---
