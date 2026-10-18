# diagnose yi mistral downstream k2

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_yi_mistral_downstream_k2_20260515T184243_result.json`
- **Structured JSON:** [`6a79ebc16610701cd0f1.json`](../../sessions/6a/6a79ebc16610701cd0f1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结论：实验未失败

日志显示实验 **正常完成**，return_code=0，总耗时 2672 秒。

### 关键证据

**日志末尾输出了完整结果表：**
```
Task                   Baseline    Uniform    MCKP-k2   MCKP-Uni
-----------------------------------------------------------------
arc_challenge            0.5043     0.5068     0.5068    +0.0000
hellaswag                0.6118     0.6051     0.6050    -0.0001
piqa                     0.8009     0.7987     0.7982    -0.0005
winogrande               0.7411     0.7395     0.7388    -0.0007

Saved to /root/ratekv/artifacts/mistral_downstream_k2_results.json
Total elapsed: 2672s
```

**"无 W&B 指标"的原因：** 该脚本本身不上报 W&B，结果直接保存到本地 JSON 文件 (`mistral_downstream_k2_results.json`)。这不是失败，是脚本设计如此。

### 其他观察

- **脚本存在**：`/root/ratekv/run_yi_mistral_downstream_k2.py` (5600 bytes)
- **模型**：Yi-1.5-9B 不在 `/root/autodl-tmp/models/` 下（只有 `LLM-Research` 和 `Mistral-7B-v0.3`），但脚本成功加载了模型（可能走 HF cache 路径）
- **GPU 正常**：2× NVIDIA RTX PRO 6000 Black (98GB)，当前有其他 python 进程在跑
- **一个无害警告**：`fatal: not a git repository` — 某处调了 git 命令但不影响结果

### 结论

**没有失败。** 实验已成功完成，结果在 `/root/ratekv/artifacts/mistral_downstream_k2_results.json`。缺少 W&B 指标是因为脚本没有集成 W&B 上报，不是异常退出。

---
