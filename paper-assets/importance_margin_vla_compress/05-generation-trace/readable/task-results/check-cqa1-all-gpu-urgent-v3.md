# check cqa1 all gpu urgent v3

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_cqa1_all_gpu_urgent_v3_20260518T235724_result.json`
- **Structured JSON:** [`08bcda8777d5f1cfdc7d.json`](../../sessions/08/08bcda8777d5f1cfdc7d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Eval M64 启动成功，确认 `SmartCompressWrapper loaded: M=64`。汇总如下：

---

```
GPU 0 (eval_baseline_prune_k05): 完成 | SR=0.0% | per-task=[0,0,0,0,0,0,0,0,0,0]%
GPU 1 (train_m64_seed43):        完成 | step 99999/100000 | loss=0.093 | ckpt=1.59GB | eval 已启动 PID=560607
GPU 2 (eval_m32_spatial):        运行中 | task 9/10 ep 7/50 | 已完成 task 0-8: [58,62,52,82,28,18,82,70,56]%
GPU 3 (eval_m32_seed43):         运行中 | task 6/10 ep 35/50 | 已完成 task 0-5: [72,38,68,36,68,48]%
```

**GPU 0 详情:** baseline_control + random_prune (zero_mask) 在 libero_object 上 SR=0.0%，10 个 task 全部为 0。随机 pruning 彻底摧毁了模型能力。

**GPU 1 详情:** 训练正常收敛完成 (final loss 0.093, eval/action_loss 0.058)。已用 `eval_smart_compress_libero.py` 在 GPU 1 启动 M=64 的 libero_object eval，日志确认 `SmartCompressWrapper loaded: M=64`。

**GPU 2/3** 预计各约 1 小时内完成。

---
