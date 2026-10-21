# diagnose urgent full gpu check and results

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_urgent-full-gpu-check-and-results_20260523T032640_result.json`
- **Structured JSON:** [`b888c2fb57d987c5124f.json`](../../sessions/b8/b888c2fb57d987c5124f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 状态

| GPU | 显存 | 利用率 | PID | 任务 | 状态 |
|-----|------|--------|-----|------|------|
| 0 | 26857/97887 MiB | 93% | 220069 | 8B s43 no-evi eval | 运行中 (33min) |
| 1 | 32479/97887 MiB | 92% | 194682 | 14B gen s43 | 运行中 (9h10m) |
| 2 | **0/97887 MiB** | **0%** | — | — | **空闲** |
| 3 | 6071/97887 MiB | 46% | 214028 | 1.7B s43 with-evi eval | 运行中 (2h18m) |

## DPO 1ep
**状态: 已完成** ✓ cuda:2 已释放

| 指标 | 值 |
|------|-----|
| train_loss | 0.5932 |
| rewards/accuracies | 0.8163 |
| rewards/margins | 1.008 |
| train_runtime | 2043s (~34min) |
| epoch | 1.0 |

输出: `/root/autodl-tmp/dpo_output_rebuilt_1ep/`
- `adapter_model.safetensors` (528MB)
- checkpoints: 100, 187

## 8B s43 no-evi eval
**PID 220069: alive (33min)**
进度: **14/32 batches (44%)**, ETA ~43min
- 使用 `--no_evidence` 参数（从 log 看是正确加载了 8B rsft s43 adapter）
- 输出目录存在但尚无 predictions 文件

## 1.7B s43 with-evi eval
**PID 214028: alive (2h18m)**
进度: **189/500 docs (38%)**, 当前 ~39s/it, ETA ~3h20m

## 14B gen s43
**PID 194682: alive (9h10m)**
进度: **12736 lines** in `generations.jsonl`

## 空闲 GPU
**cuda:2** — DPO 训练完成后已释放，可用于新任务。

---
