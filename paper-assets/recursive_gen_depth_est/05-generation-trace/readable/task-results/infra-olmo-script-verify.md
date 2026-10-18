# infra olmo script verify

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_olmo-script-verify_20260514T145240_result.json`
- **Structured JSON:** [`d9eeeda9b58273fd319e.json`](../../sessions/d9/d9eeeda9b58273fd319e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 验证报告

### 1. 语法检查
`bash -n` 在 read-only 模式下被拦截，但人工审查脚本 46 行，**所有引号均正确闭合**，原始 bug（第 52 行未闭合引号）已修复。视觉检查：**SYNTAX_OK**（建议后续用 ssh_execute 跑一次 `bash -n` 确认）。

### 2. 脚本内容 — 发现两个关键不一致

**a) MODEL_PATH 错误**：
- 脚本：`MODEL_PATH="/root/autodl-tmp/models/olmo-1b"`
- 已有 depth-0 checkpoint 的 adapter_config.json：`base_model_name_or_path: "/root/autodl-tmp/models/olmo-1b-hf"`
- 两个目录都存在，model.safetensors 大小相同（4,707,070,632 bytes），但 `olmo-1b` 有 `.aria2` 残留文件（下载可能未完全清理）
- **如果重跑会导致 adapter 加载时 base model 路径不匹配**

**b) TARGET_MODULES 错误**：
- 脚本：`q_proj,v_proj`（2 个模块）
- 已有 depth-0 checkpoint：`["v_proj", "q_proj", "k_proj"]`（3 个模块）
- 任务规格要求 3 个模块：`q_proj,k_proj,v_proj`
- **后续 depth 的 LoRA 配置会与 depth-0 不一致**

### 3. depth-0 checkpoint：**已存在**
```
adapter_model.safetensors  6.3 MB
adapter_config.json        r=16, alpha=32, dropout=0.05, target=q_proj,k_proj,v_proj
base_model: /root/autodl-tmp/models/olmo-1b-hf
```
如果修正脚本使其与 checkpoint 一致，可以**跳过 Step 1（finetune depth-0），直接从 Step 2 开始**。

### 4. OLMo 模型完整性
- `olmo-1b-hf/`：完整（model.safetensors 4.7GB + config + tokenizer，无残留文件）
- `olmo-1b/`：有 `.aria2` 残留，缺少 `configuration.json`，**不建议使用**

### 5. GPU 状态
```
GPU 0: 100% util, 11623/97887 MiB (12%)
GPU 1: 100% util, 34979/97887 MiB (36%)
```
两块 GPU 都在运行任务。需等待当前任务完成或确认可以共享 GPU 0。

### 6. OLMo 模型信息
从 config.json：`OlmoForCausalLM`, vocab=50304, eos_token_id=50279, pad_token_id=1, hidden=2048, 16 layers, 16 heads。（tokenizer python 检查因 ssh_read_only 限制未执行）

### 7. 是否可以安全重跑：**NO**

需要修复后才能重跑：

| 问题 | 修复 |
|------|------|
| MODEL_PATH 指向 `olmo-1b`（有 aria2 残留） | 改为 `/root/autodl-tmp/models/olmo-1b-hf` |
| TARGET_MODULES 只有 2 个 | 改为 `q_proj,k_proj,v_proj` |
| 无日志重定向 | 添加 `logs/pipeline_olmo.log` 输出 |
| GPU 全忙 | 等待当前任务完成 |

修复后，由于 depth-0 checkpoint 已存在且与 `olmo-1b-hf` + 3 模块一致，可以修改脚本从 Step 2 开始，节省 ~5 min。

---
