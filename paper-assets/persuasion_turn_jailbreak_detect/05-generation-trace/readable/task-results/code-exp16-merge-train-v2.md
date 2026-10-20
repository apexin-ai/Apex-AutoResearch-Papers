# code exp16 merge train v2

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp16-merge-train-v2_20260519T194753_result.json`
- **Structured JSON:** [`5c0d914a0fbd46b93128.json`](../../sessions/5c/5c0d914a0fbd46b93128.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

进程在运行（PID 293352 占 26.2% CPU，已使用 797MB 内存），日志是 Python 缓冲延迟，训练正常启动。

---

## 汇报

### 1. Llama benign 完成确认
`benign_llama_250.jsonl`: **250 行**，labels={'benign'} ✓
`crescendo_jailbreak_llama.jsonl`: **251 行**，labels={'jailbreak'} ✓

### 2. 数据合并结果

| Split | Total | llama | qwen | benign | jailbreak |
|-------|-------|-------|------|--------|-----------|
| train | 350 | 176 | 174 | 176 | 174 |
| val | 74 | 36 | 38 | 36 | 38 |
| test | 76 | 38 | 38 | 38 | 38 |
| **total** | **500** | **250** | **250** | **250** | **250** |

输出目录：`data/mixed_llm/`

### 3. 训练提交状态

| Job | GPU | tmux session | 内容 |
|-----|-----|-------------|------|
| `exp16_vanilla_train` | cuda:0 | exp16_vanilla_train | vanilla baseline × 3 seeds (42/123/456) |
| `exp16_9class_train` | cuda:1 | exp16_9class_train | 9-class DAPT+GRU × 3 seeds (42/123/456), 每 seed 2 阶段 |

注意：去掉了 `--use_wandb` 因为服务器未配置 wandb API key。如需 wandb 追踪，需先 `wandb login`。

---
