# diagnose westd41074 gpu3 and anomalies

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_westd41074_gpu3_and_anomalies_20260524T205134_result.json`
- **Structured JSON:** [`6a1ddf451f78c72fa50e.json`](../../sessions/6a/6a1ddf451f78c72fa50e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

PID 794748 在 GPU2 上正常运行，利用率 39%。796424 已 killed。GPU3 已空闲。

汇总结果：

```
异常1: 已完成 SR=91.0% (libero_goal, pi05 l2norm k=0.9 seed43)
       结果保存: eval_results/pi05_l2norm_k0.90_libero_goal_seed43.json

异常2: 保留PID=794748 (正常运行, GPU2利用率39%), killed PID=796424 (网络错误崩溃)
       796424崩溃原因: tokenizer下载时 "Network is unreachable"

异常3: 正常运行中 (PID=756339, GPU2占用10767MiB)
       进度: Task 4/10, ep=20, 当前累计SR=53.0% (106/200)
       GPU利用率0%是瞬时快照，进程实际在正常推理
```

---
