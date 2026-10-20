# audit qwen15b notrace conflict

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_qwen15b-notrace-conflict_20260523T113512_result.json`
- **Structured JSON:** [`2bc81b8810e7ced541f0.json`](../../sessions/2b/2bc81b8810e7ced541f0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

找到了论文中的值。**experiments.tex 第 31 行**使用 72.35±4.48 作为 Qwen-1.5B no_trace 的 mean±std——确认来源于 OLD seed42=67.31%。

---

## 调查结论

### 两个目录对比

| | `qwen15b_no_trace_seed42` (OLD) | `qwen1.5b_no_trace_seed42` (NEW) |
|---|---|---|
| **位置** | `/root/autodl-tmp/trace-verdict-study-checkpoints/` | 同上 |
| **创建时间** | 2026-05-16 17:56 CST | 2026-05-21 22:50 CST |
| **Registry 创建** | 2026-05-16T09:22 UTC | 2026-05-16T07:27 UTC |
| **Accuracy** | 67.31% (lift = **-4.2%**，低于 majority baseline) | 72.61% (lift = +1.09%) |
| **Base model path** | `/root/autodl-tmp/models/...` | `/root/trace-verdict-study/models/...` |
| **Base model MD5** | `bad9141e...`（相同） | `bad9141e...`（相同） |
| **Adapter MD5** | `fd53a096...` | `6410763c...`（不同weights） |
| **Predictions 差异** | 117/1190 不同 | 净增 63 个正确 |
| **Checkpoints** | 仅 final/ | checkpoint-148, 296, 444, final/ |

### 训练超参完全一致

lr=2e-4, epochs=3, batch=4, grad_accum=8, warmup_ratio=0.1, lr_scheduler=LINEAR, weight_decay=0.01, seed=42, LoRA r=16/alpha=32/dropout=0.05, max_length=2048。

训练数据完全一致（`no_trace_train.jsonl` 最后修改 2026-05-15，两个 run 之间未变）。

### 差异根因

Base model 字节完全一致（md5 相同），但 adapter weights 不同。两次独立训练在相同超参+数据+seed 下产生了不同 adapter，原因是 **CUDA 计算的非确定性**（PyTorch 未启用 `torch.use_deterministic_algorithms(True)`）。

### Canonical run 判断：**`qwen1.5b_no_trace_seed42` (72.61%) 是 canonical**

1. **时间线一致性**：seed123 (5/20)、seed456 (5/20)、NEW seed42 (5/21) 属于同一批次的 multi-seed 实验；OLD seed42 (5/16) 是 5 天前的早期探索性 run
2. **数值一致性**：NEW seed42=72.61% 与 seed123=75.88%、seed456=73.87% 一致（std=1.65）；OLD seed42=67.31% 是异常离群值（std=4.48），且**低于 majority baseline 71.5%**
3. **Checkpoints 完整性**：NEW run 保存了全部 epoch checkpoints，结构与 seed123/seed456 一致；OLD run 仅有 final/
4. **模型路径**：NEW run 使用 `/root/trace-verdict-study/models/`（符合 C002 约束），OLD run 使用已废弃的 `/root/autodl-tmp/models/` 路径

### 对论文的影响

**experiments.tex 第 31 行** Qwen-1.5B no_trace 列：

| | 当前（使用 OLD） | 修正后（使用 NEW） |
|---|---|---|
| Mean | 72.35 | **74.12** |
| Std | ±4.48 | **±1.65** |

变化：mean +1.77pp，std 从异常高的 4.48 降至合理的 1.65。这不影响论文的核心结论（no_trace 远弱于 exception_only），但 std=4.48 的异常值可能引起 reviewer 关注。

### Registry 状态

两个 exp_id 都存在于 registry 中（均为 DONE），`qwen1.5b_no_trace_seed42` 已包含正确的 72.61% metrics。`qwen15b_no_trace_seed42` 的 67.31% 应标记为 superseded。

---
