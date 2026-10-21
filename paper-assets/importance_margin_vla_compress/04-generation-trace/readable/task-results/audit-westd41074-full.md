# audit westd41074 full

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_westd41074_full_20260522T200531_result.json`
- **Structured JSON:** [`d12eb55c23539f24d045.json`](../../sessions/d1/d12eb55c23539f24d045.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

进程存活，模型加载中。以下是完整汇报：

---

## 四卡审计表 (westd-41074)

| GPU | 显存占用 | 利用率 | 进程 | 状态 |
|-----|---------|--------|------|------|
| 0 | 10448/97887 MiB | 55% | PID 3789: π0.5 Random k=0.85 Long s42 | Task 3/10 进行中, 总 SR 49.3% |
| 1 | 10406/97887 MiB | 24% | PID 3863: π0.5 Random k=0.7 Long s42 | Task 3/10 进行中, 总 SR 76.0% |
| 2 | ~0 MiB (加载中) | 0% | PID 57623: **新部署** π0.5 Random k=0.5 Long s42 | 模型加载中 |
| 3 | 27535/97887 MiB | 0% | PID 59671: OpenVLA SC M64 v6 训练 | step 72900/100000 (72.9%) |

## Attention k=0.7 Object 收割结果

| 指标 | 值 |
|------|-----|
| SR | **0.6%** (3/500) |
| keep_ratio | 0.7 |
| prune_mode | attention |
| suite | libero_object |
| seed | 42 |
| 结论 | **negative** — 灾难性失败，attention importance 无法为 π0.5 识别任务相关 vision tokens |

已注册 registry: `eval_pi05_attention_k07_object_seed42` → DONE (negative)

## 新部署实验

| 优先级 | 实验 | GPU | 状态 |
|--------|------|-----|------|
| #1 | π0.5 Long Random k=0.5 s42 | cuda:2 | **已部署**，模型加载中 |
| #2 | π0.5 Long Random k=0.3 s42 | — | 等待空卡 |
| #3 | π0.5 Object Random k=0.7 s43 | — | 等待空卡 |
| #4 | X-VLA Long L2norm k=0.7 s42 | — | 等待空卡 |

## 备注
- GPU 0/1 的 Long 实验（k=0.85, k=0.7）正在运行，预计各还需 ~2-3h 完成
- GPU 3 M64 训练在 72.9%，约还需 ~12h 完成
- 优先级 #2-#4 需等 GPU 0/1 释放后才能部署

---
