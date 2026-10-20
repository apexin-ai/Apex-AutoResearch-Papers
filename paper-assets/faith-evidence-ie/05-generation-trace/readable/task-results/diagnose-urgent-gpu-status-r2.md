# diagnose urgent gpu status r2

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_urgent-gpu-status-r2_20260520T204754_result.json`
- **Structured JSON:** [`d98a131dd97cb6fc573e.json`](../../sessions/d9/d98a131dd97cb6fc573e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 进程状态
- PID 48806 (14B RSFT train): **dead — 成功完成** ✓
- PID 45587 (s43 2048 eval): **alive** — 143/247 (58%), 已运行 2h21m, 预估剩余 ~1h36m (CUDA:1)
- PID 40255 (s44 2048 eval): **alive** — 236/247 (96%), 已运行 3h40m, 预估剩余 ~12min (CUDA:2)
- PID 42346 (s42 2048 eval): **alive** — 222/247 (90%), 已运行 3h07m, 预估剩余 ~26min (CUDA:3)

## GPU 状态
| GPU | 显存占用 | 利用率 |
|-----|---------|--------|
| 0 | 0 MiB | 0% — **空闲** |
| 1 | 18879 MiB | 92% — s43 eval |
| 2 | 18879 MiB | 91% — s44 eval |
| 3 | 18879 MiB | 92% — s42 eval |

## 14B RSFT Train 结果
- Checkpoint: `/root/autodl-tmp/rsft_output_14b/adapter_model.safetensors`（已确认存在）
- train_loss: **0.5005**, mean_token_accuracy: **0.8783**
- 3 epochs, 1131 steps, runtime 3958s (~66min)

## Eval 预计完成时间
- s44: ~12 分钟后
- s42: ~26 分钟后
- s43: ~1.5 小时后

## Rsync 状态
路径 `/root/autodl-tmp/sft_output_8b_*/` 无匹配 — 找到 0 个 adapter 文件（14B 的在 `sft_output_14b/` 下，路径 pattern 不匹配）

## 异常/需要注意
- GPU 0 空闲，14B 训练已完成。可用于后续任务。
- s43 eval 比另外两个慢很多（58% vs 90%/96%），可能是启动更晚或 batch 间有波动，但进程正常。

---
