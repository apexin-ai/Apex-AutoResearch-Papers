# verify d1 v2 startup

**schema conform ie training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_d1_v2_startup_20260513T034122_result.json`
- **Structured JSON:** [`1b10044bf113bb6b29a7.json`](../../sessions/1b/1b10044bf113bb6b29a7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部正常，汇总如下：

## 1. GPU 状态

| GPU | 进程 PID | 显存占用 | GPU 利用率 | 状态 |
|-----|----------|----------|-----------|------|
| cuda:0 | 65560 | 22076 MiB / 97887 MiB | 58% | eval_C_v2 运行中 |
| cuda:1 | 67223 | 22340 MiB / 97887 MiB | 83% | D1 训练 v2 运行中 |

僵尸进程 52221 已不存在，确认已被 kill。

## 2. D1 训练日志确认

- 模型加载：`Loading model: /root/autodl-tmp/models/Qwen/Qwen3.5-9B` ✓
- LoRA 参数：`trainable params: 116,391,936 || all params: 9,070,195,200 || trainable%: 1.2832` ✓
- 训练启动：`Starting GRPO training...` ✓，进度条已开始 (0/500)
- W&B offline 模式，run ID: `kq0ig4cj`

## 3. D1 config 确认

`model_name: "/root/autodl-tmp/models/Qwen/Qwen3.5-9B"` — 本地路径 ✓

## 4. formal_A checkpoint 列表

| Checkpoint | 时间 |
|------------|------|
| checkpoint-100 | May 12 22:08 |
| checkpoint-200 | May 13 00:28 |
| checkpoint-300 | May 13 02:13 |
| checkpoint-400 | May 13 04:01 |
| checkpoint-500 | May 13 05:48 |
| merged/ | May 13 05:49 |

5 个 checkpoint + 已合并的 merged 目录，全部可用于 D2。

---
