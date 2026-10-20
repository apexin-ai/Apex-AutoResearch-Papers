# analyze eval sft rasp rlvr 20

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval_sft_rasp_rlvr_20_20260516T181903_result.json`
- **Structured JSON:** [`80855dc52d565056f6dc.json`](../../sessions/80/80855dc52d565056f6dc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE (negative)，artifact 已注册。

## 实验结果总结

| 模型 | GSM8K Accuracy | N |
|------|---------------|---|
| Standard SFT (baseline) | 59.29% | 1319 |
| **RASP-RLVR 20% post-SFT** | **58.30% ± 1.36%** | **1319** |
| RASP SFT (standard CKA) | 61.49% | 1319 |

**结论：Negative。**

RASP-RLVR 20% 经过 SFT 恢复后 GSM8K 准确率为 58.30%（769/1319），不仅低于 RASP SFT 的 61.49%（-3.19pp），甚至低于 Standard SFT 的 59.29%（-0.99pp）。

RLVR 恢复策略在反向 CKA scoring 剪枝模型上**未能产生正面效果**——性能反而退化。可能原因：
1. 反向 CKA scoring 保留的结构与 RLVR 训练信号不兼容
2. RLVR 数据的 reward signal 在剪枝后的稀疏结构上产生了有害的梯度更新
3. checkpoint-1870 可能过拟合了 RLVR 数据（avg response length 227 较短，EOS rate 98%，生成倾向截断推理）

---
