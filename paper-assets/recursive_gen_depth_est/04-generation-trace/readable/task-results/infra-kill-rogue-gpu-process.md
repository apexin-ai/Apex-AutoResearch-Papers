# infra kill rogue gpu process

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_kill-rogue-gpu-process_20260514T145519_result.json`
- **Structured JSON:** [`ed5104d49abc5a4b5108.json`](../../sessions/ed/ed5104d49abc5a4b5108.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总如下：

---

## 执行结果

### 1. Step 1 — nvidia-smi（kill 前）
```
Thu May 14 22:55:46 2026
+-----------------------------------------------------------------------------------------+
| GPU  Name                 Persistence-M | Memory-Usage         | GPU-Util |
|   0  NVIDIA RTX PRO 6000 Blac...    On  | 11623MiB / 97887MiB  |   96%   |
|   1  NVIDIA RTX PRO 6000 Blac...    On  | 15641MiB / 97887MiB  |   64%   |
+-----------------------------------------------------------------------------------------+
| Processes:                                                                  |
|  GPU    PID   Type   Process name                        GPU Memory Usage   |
|    0  125083    C    python                                11614MiB          |
|    1  126022    C    python                                15632MiB          |
+-----------------------------------------------------------------------------------------+
```

### 2. Step 2 — 进程确认
- **PID 122428/122434（rogue GPT-2 XL）：已不存在**，无需 kill
- **PID 123665（原 cross_model_gpt2xl_001）：已结束**，但其 pipeline 子进程继续运行

当前进程：
- **cuda:0 PID 125083**: `python scripts/lora_finetune.py ... --model_name /root/autodl-tmp/models/pythia-1.4b --gpu 0` — Pythia temp09 finetuning
- **cuda:1 PID 126022**: `python scripts/generate_next_depth.py --adapter_dir checkpoints/gpt2xl/lora_depth_0 ... --model_name /root/autodl-tmp/models/gpt2-xl --gpu 0` — GPT-2 XL 正常 pipeline（cross_model_gpt2xl_001 的子进程，父 PID 123660）

### 3. Kill 结果
**无需执行** — rogue 进程 122428/122434 已自行退出或被其他方式终止。

### 4. Step 4 — nvidia-smi（同 Step 1，无 kill 操作）
同上。cuda:0 现在被 Pythia temp09 占用，cuda:1 被 GPT-2 XL 正常 pipeline 占用。

### 5. Checkpoint 污染检查
**无污染。**
- `checkpoints/gpt2xl/` 仅含 `lora_depth_0/`
- `lora_depth_0/` 内文件时间戳 22:42-22:54，与 cuda:1 注册任务（14:42 UTC = 22:42 UTC+8）一致
- `lora_depth_1/`、`lora_depth_2/` 不存在
- 当前 PID 126022 正在生成 `depth_1.jsonl`，训练正常推进

### 6. OLMo 脚本修复
- `MODEL_PATH`: `olmo-1b` → `olmo-1b-hf` ✓
- `TARGET_MODULES`: `q_proj,v_proj` → `q_proj,k_proj,v_proj` ✓
- 语法检查：**SYNTAX_OK** ✓

### 7. Pythia temp09 (PID 125067) 状态
**存活。** PID 125067 是 pipeline wrapper（bash），其子进程 PID 125083 正在 cuda:0 上执行 `lora_finetune.py`，显存 11614 MiB，GPU 利用率 96%。

---
