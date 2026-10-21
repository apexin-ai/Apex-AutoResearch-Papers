# eval contamination 60 uniform

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_contamination_60_uniform_20260516T010607_result.json`
- **Structured JSON:** [`ef6b631b3c473286a060.json`](../../sessions/ef/ef6b631b3c473286a060.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断报告：contamination_60_uniform_seed42

### EXIT_CODE=129 诊断
- 训练**已完成** 6103/6103 步，model 已正常保存到 `output/models/contamination_60_uniform_seed42/final`
- 日志最后输出 `Training complete. Model saved to ...` 之后才出现 `EXIT_CODE=129`
- **SIGHUP 发生在训练完成并保存模型之后**，可能是 SSH 会话断开触发，对训练结果无影响
- 日志中无 error/traceback/OOM

### Checkpoint 完整性
- 文件完整：model.safetensors (1.11GB) + config + tokenizer 等全部存在
- 目录总大小 1.2GB，符合 Qwen3-0.6B 预期
- 模型加载验证通过：**596.0M 参数**

### Eval 结果
| 指标 | 值 |
|------|-----|
| **Loss** | 2.8773 |
| **Perplexity** | 17.77 |
| **Tokens** | 4,077,068 |
| 耗时 | 183s |

### Train Metrics
| 指标 | 值 |
|------|-----|
| **train_loss** | 7.649 |
| train_runtime | 12904.8s (~3.6h) |
| train_samples/s | 7.567 |
| train_steps/s | 0.473 |

### 结论
**不需要重跑。** 训练正常完成，checkpoint 完整可加载，eval 结果正常。EXIT_CODE=129 是训练完成后的 SIGHUP，无害。

---
