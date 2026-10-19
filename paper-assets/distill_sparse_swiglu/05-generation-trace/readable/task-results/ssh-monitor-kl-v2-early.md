# ssh monitor kl v2 early

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_monitor-kl-v2-early_20260515T151956_result.json`
- **Structured JSON:** [`e50d095c836df3d35a49.json`](../../sessions/e5/e50d095c836df3d35a49.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

无错误、无 OOM、无 Traceback。汇总结果：

```
s42  step 1:  kl_raw=1.1797, kl_norm=1.179688, sparsity=0.406
s42  step 50: kl_raw=0.6641, kl_norm=0.664062, sparsity=0.516
s123 step 1:  kl_raw=1.0703, kl_norm=1.070312, sparsity=0.406
s123 step 50: kl_raw=0.6562, kl_norm=0.656250, sparsity=0.514
```

验证：
- **kl_norm ≈ kl_raw**: 两个实验全部步骤 kl_norm = kl_raw（差异 < 0.001），bug 修复确认生效。旧 bug 的 kl_norm≈7e-5 不再出现。
- **kl_raw 下降**: s42 1.18→0.66, s123 1.07→0.66，均在下降 ✓
- **sparsity 范围**: 两个都从 0.406 → 0.51x，在 0.3-0.6 范围内 ✓
- **无 OOM/Error/Traceback** ✓

**VERDICT: BOTH OK**

---
