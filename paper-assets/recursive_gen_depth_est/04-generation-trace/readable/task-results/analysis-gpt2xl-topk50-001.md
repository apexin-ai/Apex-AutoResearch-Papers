# analysis gpt2xl topk50 001

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_gpt2xl_topk50_001_20260515T021757_result.json`
- **Structured JSON:** [`dbb7f832967c4e1249bc.json`](../../sessions/db/dbb7f832967c4e1249bc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**Pipeline 状态：生成完成，评估未执行。**

Pipeline (`run_pipeline_gpt2xl_topk50.sh`) 只包含 Steps 1-5（生成 + 微调），不含分类评估。数据已就绪（4 个 depth × 5000 samples），但 `results/gpt2xl_topk50/` 目录不存在。

### 已提取的信息

**Finetune losses:**
| Depth | Final Training Loss |
|-------|-------------------|
| depth_0 | (复用自 gpt2xl nucleus，symlink) |
| depth_1 | 1.9886 |
| depth_2 | 1.7554 |

**Checkpoints:**
- `lora_depth_0` → symlink 到 `checkpoints/gpt2xl/lora_depth_0`
- `lora_depth_1` (2026-05-15 08:01)
- `lora_depth_2` (2026-05-15 09:11)

**Pipeline 运行时间:** 06:47 → 10:15 (约 3.5 小时)

---

### 需要执行评估

参照 `run_eval_gpt2xl_temp09.sh`，需要为 `gpt2xl_topk50` 运行评估脚本，包括：
1. Code contamination 检测
2. Feature extraction
3. 4-class classification
4. 3-class (d1/d2/d3) classification
5. 3-class filtered classification

是否需要我创建 `run_eval_gpt2xl_topk50.sh` 并用 `ssh_execute` 执行？

---
