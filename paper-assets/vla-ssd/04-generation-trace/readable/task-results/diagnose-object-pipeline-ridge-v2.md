# diagnose object pipeline ridge v2

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_object_pipeline_ridge_v2_20260521T090006_result.json`
- **Structured JSON:** [`09f6ae43844787977e85.json`](../../sessions/09/09f6ae43844787977e85.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

### 1. object_pipeline_ridge_v2 实际上**成功完成了**

日志仅 238 行，从 15:13:55 开始到 16:50:12 结束，一次性完成全部 6 个 Phase，耗时 96.3 分钟。所有结果文件已生成：

| 文件 | 时间 |
|------|------|
| action_r2_probing.json | 15:23 |
| l1_attention_profile.json | 15:23 |
| cross_instruction_classification.json | 15:26 |
| rsa_analysis.json | 15:26 |
| counterfactual_combined.json | 16:50 |

**cron 标记为 "failed (5次)" 是误报**——日志中没有任何错误或重启痕迹。可能是 cron 监控逻辑把 v1 的失败次数累计到了 v2 上，或者进程退出码检测有 bug。

### 2. object_pipeline_ridge (v1) 的失败原因

**根因：网络不可达**。`transformers` 加载 processor 时，即使 checkpoint 在本地 (`/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-object`)，`trust_remote_code=True` 仍尝试从 HuggingFace Hub 下载 `processing_prismatic.py`。当时网络不通，导致：

```
OSError: Network is unreachable -> huggingface.co/openvla/openvla-7b/resolve/main/processing_prismatic.py
```

### 3. 两次失败是否同一原因

不是。**v1 失败（网络问题），v2 成功（无错误）**。v2 被误标为 failed。

### 4. 建议操作

1. **将 v2 状态更正为 succeeded**——结果数据完整可用。
2. **防止 v1 类问题复发**：在脚本中加 `TRANSFORMERS_OFFLINE=1` 环境变量或 `local_files_only=True` 参数，避免依赖网络下载 dynamic module。确保 `processing_prismatic.py` 已存在于本地 checkpoint 目录中。
3. **排查 cron 监控逻辑**——为什么把一个成功完成的实验标记为 failed 5 次。

---
