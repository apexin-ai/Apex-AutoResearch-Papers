# diagnose w38 attn k05 s45 utilization

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_w38_attn_k05_s45_utilization_20260528T052237_result.json`
- **Structured JSON:** [`f5fcb14a15a844caccd6.json`](../../sessions/f5/f5fcb14a15a844caccd6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**实验已正常结束。**

- **状态**: `EXIT_CODE=0`，已完成全部 10 个 task（T0-T9），总耗时 168.4 min
- **最终结果**: `libero_10 prune=attention keep=0.5 SR=49.4%`
- **结果文件**: `/root/autodl-tmp/importance_margin_vla_compress/eval_results/pi05_attention_k0.50_libero_10_seed45.json`
- **GPU 利用率 0%, 显存 1 MiB**: 进程已退出，GPU 已释放

GPU 利用率低是因为实验已经跑完了，不是卡住。cuda:3 现在空闲可用。

---
