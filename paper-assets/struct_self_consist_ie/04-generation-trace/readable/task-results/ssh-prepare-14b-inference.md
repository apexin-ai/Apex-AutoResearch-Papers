# ssh prepare 14b inference

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_prepare-14b-inference_20260520T070045_result.json`
- **Structured JSON:** [`e3a949edc9a11791ab20.json`](../../sessions/e3/e3a949edc9a11791ab20.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个文件全部写入成功。

---

## 报告

### 关键修正
任务描述说的是 14B，但服务器上实际训练的是 **Qwen2.5-32B-Instruct QLoRA**（rank=32, alpha=64, 4-bit quant, 4 GPU torchrun）。所有脚本已按 32B 准备。

### 准备好的文件

| 文件 | 路径 |
|------|------|
| Export 配置 | `export_config_qwen25_32b_fewnerd.yaml` |
| Inference 脚本 | `run_32b_fewnerd_inference.sh` |
| 执行 checklist | `32b_post_completion_checklist.md` |

### 训练状态
- 进度: **56.2%** (step 23150 / 41180)
- 已用时: 21h24m, 剩余: ~16h40m
- **ETA: ~May 21 13:40 UTC**

### ⚠️ 磁盘空间问题
- 可用: **79GB**
- Merged 32B 模型: **~62GB**
- **必须在 export 前清理 ≥20GB**（旧 checkpoint 可回收 ~21GB: wnut17-lora 5.3G, 4b-conll 4.1G, scierc-v2 3.4G, llama 6.4G, smoke 1.7G）

### 时间估算

| 步骤 | 预计耗时 |
|------|---------|
| Export (merge) | ~15-20 min |
| Inference 第一轮 (seed 42+123 并行, TP=2) | ~2-4h |
| Inference 第二轮 (seed 456, TP=2) | ~2-4h |
| **Export 后总计** | **~4.5-8.5h** |

### Inference 分流方案（全在 autodl-5090）
32B bf16 需要 TP=2（2x 5090 = 64GB）。4 卡可同时跑 2 个 seed：
- GPU 0,1 → seed 42 | GPU 2,3 → seed 123（并行）
- 任一完成后 → seed 456

---
