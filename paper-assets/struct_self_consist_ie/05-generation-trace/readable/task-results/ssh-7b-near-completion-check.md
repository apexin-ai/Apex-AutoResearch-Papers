# ssh 7b near completion check

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_7b-near-completion-check_20260520T014647_result.json`
- **Structured JSON:** [`c3a2cb688ebec735b3d7.json`](../../sessions/c3/c3a2cb688ebec735b3d7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态总结

**5090-c — 7B 训练**
- 当前阶段：**training**（尚未进入 export）
- 进度：20117/20590 (97.7%)，~2.35s/step
- 剩余：473 步 ≈ **~18.5 分钟**
- loss=0.0059，收敛良好

**5090-b — 模型下载**
- 进程仍在运行
- 4 个 safetensors 分片全部 incomplete：2.0G + 1.6G + 2.3G + 2.0G = **~7.9GB / ~15GB (约 53%)**
- 预计还需 **~15-20 分钟**

## 分流建议

**暂不拦截，等两边都就绪再决定。** 原因：
1. 训练还有 ~18.5 分钟，之后 export（LoRA merge）还需 ~5-10 分钟，总共 ~25-30 分钟后才进入 inference
2. 5090-b 下载也还需 ~15-20 分钟，到 export 完成时应该刚好下载完
3. 建议在训练完成时再查一次：如果 5090-b 下载已完成，拦截 pipeline 把 merged model rsync 到 5090-b 跑 inference（4 GPU，预计 ~2x 加速）；如果没完成，就让 pipeline 在 5090-c 继续

下一步：~20 分钟后复查两边状态。

---
