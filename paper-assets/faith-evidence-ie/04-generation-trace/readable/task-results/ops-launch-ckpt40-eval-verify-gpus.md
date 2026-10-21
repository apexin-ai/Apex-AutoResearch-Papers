# ops launch ckpt40 eval verify gpus

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_launch-ckpt40-eval-verify-gpus_20260514T211139_result.json`
- **Structured JSON:** [`6791cc77387902ff0cde.json`](../../sessions/67/6791cc77387902ff0cde.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Eval 已成功启动，正在 cuda:2 上推理 (0/62 batches)。

## GPU 全貌 (nvidia-smi)

| GPU | PID | 任务 | 利用率 | 显存 |
|-----|-----|------|--------|------|
| cuda:0 | 90085 | P0 训练 (grpo-ced-lr5e6-r1) | 62% | 13645/32607 MiB |
| cuda:1 | 96500 | ckpt-20 eval | 79% | 9719/32607 MiB |
| cuda:2 | 100555 | **ckpt-40 eval (刚启动)** | loading→inference | 6924/32607 MiB |
| cuda:3 | 94758 | rp_r2 训练 | 57% | 13645/32607 MiB |

## P0 ckpt-40 eval
- **状态: STARTED**
- PID: 100549 (子进程 100555 在 GPU 上)
- Log: `/tmp/eval_lr5e6_ckpt40.log`
- 进度: Inference 0/62 batches, 模型加载完毕, 985 docs / 12275 gold triples

## P0 训练 (PID 90085)
- **状态: ALIVE** (Rl, 运行 1h31m55s)
- 任务: grpo-s3-ced-lr5e6-r1, max_steps=200
- GPU: cuda:0

## rp_r2 (PID 94758)
- **状态: ALIVE** (Rl, 运行 1h06m28s)
- **实际 GPU: cuda:3**
- 任务: grpo-s3-ced-lr5e6-rp-r2

## ckpt-20 eval (PID 96500)
- **状态: ALIVE** (Rl+, 运行 48m51s)
- GPU: cuda:1

4 张卡全部在用，无异常。

---
