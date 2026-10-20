# diagnose full gpu progress check

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_full_gpu_progress_check_20260519T054343_result.json`
- **Structured JSON:** [`52fea60238cec10f511d.json`](../../sessions/52/52fea60238cec10f511d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

cuda:3 现在有进程了（PID 618028, 27438MiB），s44_r2 已正常启动。

```
cuda:0: D112 step 3 — 258/567 steps (~7s/step), 剩余 ~36 min
cuda:1+2: 14B SFT — 72/144 steps (~64s/step), 剩余 ~77 min
cuda:3: 1.7B s44_r2 — 12/567 steps (~3s/step), 剩余 ~28 min (PID 618028, 刚启动)
```

补充：
- **1.7B s43_r2 已完成** — 13:38 保存至 `/root/autodl-tmp/rsft_output_qwen3_1_7b_k1_s43`（567/567 steps, final loss=0.553）
- 14B SFT epoch 1 eval 已完成（eval_loss=0.635, token_acc=0.847），现在在 epoch 2
- D112 step 3 训练 PID 613083 仍活跃，尚未完成，不触发 step 4 eval

---
