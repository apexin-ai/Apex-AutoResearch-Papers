# analysis llama eval completion

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_llama_eval_completion_20260521T034404_result.json`
- **Structured JSON:** [`eec5228ab45c04dc10c7.json`](../../sessions/ee/eec5228ab45c04dc10c7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。汇报如下：

```
状态：success（8/8 步全部完成）

                    GAR-ours    GAR-dongre   PPL
TF Base:            0.0166      0.0038       3.45   (N=50, T=4)
TF TG:              0.4836      0.0180       2.57   (N=50, T=4)
AR Base:            0.0086      0.0118       1.24   (N=5,  T=10)
AR TG:              0.0304      0.0217       1.32   (N=5,  T=10)

TF-AR Gap ratio (TG,  ours):   15.9x
TF-AR Gap ratio (Base, ours):  1.9x   ← control，无 TG 时 gap 很小
TF-AR Gap ratio (TG,  dongre): 0.83x  ← dongre 指标无 gap（AR ≥ TF）

vs Qwen v7: Llama 16x gap vs Qwen 32x gap
```

**C5 结论**：Llama-3.1-8B 确认跨模型泛化。TG 模型 GAR-ours 训练推理 gap 16x，虽低于 Qwen 的 32x 但仍非常显著。Base model control 仅 1.9x，说明 gap 是 TG 训练引入的 exposure bias 导致。

**注意事项**：
- TF/AR eval 设定不同（N=50/T=4 vs N=5/T=10），绝对值对比需谨慎
- GAR-dongre 指标完全不展现 gap（ratio < 1），仅 GAR-ours 捕捉到 exposure bias 效应
- Gate dynamic range 集中在 L24/L28/L30（diff 0.23-0.38），与 Qwen 类似的中高层 pattern

---
