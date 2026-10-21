# research check p2v2 status

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_check_p2v2_status_20260516T220259_result.json`
- **Structured JSON:** [`201599fe4d13378db32e.json`](../../sessions/20/201599fe4d13378db32e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完整结果如下：

```
=== P2v2 RESULT ===
文件: /root/autodl-tmp/vla-ssd/results/ablations/demo_sensitivity_25.json
大小: 2251 bytes, 生成时间: May 16 19:00

=== COMPARISON ===
RSA profile correlation: 0.9696
Probe profile correlation: 0.8189
RSA peak 50:  layer 12, RSA=0.6282
RSA peak 25:  layer 12, RSA=0.6059
Probe peak 50: layer 9, R²=0.6587
Probe peak 25: layer 11, R²=0.6088

=== DATA DIMENSIONS ===
Layers with data: rsa_50=33, rsa_25=33, probe_50=33, probe_25=33

=== TMUX ===
(无 demo 相关 session)

=== 耗时 ===
elapsed_seconds: 1583.8 (~26 min)
```

实验已完成。RSA 层间 profile 在 50→25 demos 下相关性 0.97（极高），peak 位置稳定在 layer 12。Probe profile 相关性 0.82，peak 从 layer 9 偏移到 layer 11。整体绝对值下降（RSA 约 -0.02，Probe 约 -0.05~0.07），但 shape 高度保持。

---
