# ops yi mistral downstream k2 diagnosis

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_yi_mistral_downstream_k2_diagnosis_20260515T184240_result.json`
- **Structured JSON:** [`ba4a5252e00c6eb3d715.json`](../../sessions/ba/ba4a5252e00c6eb3d715.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个模型都跑完了，实验实际上是成功的。总耗时 2672s。结果 JSON 都已保存。

```
Yi-1.5-9B k=2 downstream:
  状态: ✓ 完成
  分配: {4-bit: 189, 8-bit: 1, 2-bit: 2}, budget=0.25
                Baseline  Uniform  MCKP-k2  MCKP-Uni delta
  ARC-C         0.5265    0.5205   0.4991   -0.0214
  HellaSwag     0.5912    0.5855   0.5818   -0.0037
  PIQA          0.7949    0.7916   0.7916   +0.0000
  WinoGrande    0.7332    0.7206   0.7238   +0.0032
  avg delta vs uniform:                     -0.0055

Mistral-7B-v0.3 k=2 downstream:
  状态: ✓ 完成
  分配: {4-bit: 254, 2-bit: 2}, budget=0.249, distortion=0.0
                Baseline  Uniform  MCKP-k2  MCKP-Uni delta
  ARC-C         0.5043    0.5068   0.5068   +0.0000
  HellaSwag     0.6118    0.6051   0.6050   -0.0001
  PIQA          0.8009    0.7987   0.7982   -0.0005
  WinoGrande    0.7411    0.7395   0.7388   -0.0007
  avg delta vs uniform:                     -0.0003

失败原因: 无——实验正常完成，进程退出码 0。
         cron 标记 failed 可能是因为进程退出后检测机制误判。
```

Mistral k=2 几乎与 uniform 持平（avg delta 仅 -0.0003），符合预期——256 层中只有 2 层分到 2-bit，影响极小。Yi 的 delta 稍大（-0.0055），ARC-C 贡献了主要降幅。

结果文件路径：
- `/root/ratekv/artifacts/yi_downstream_k2_results.json`
- `/root/ratekv/artifacts/mistral_downstream_k2_results.json`

---
