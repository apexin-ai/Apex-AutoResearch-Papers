# infra disk fix and restart

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_disk-fix-and-restart_20260513T231133_result.json`
- **Structured JSON:** [`4d3a8467d43875dcb3b0.json`](../../sessions/4d/4d3a8467d43875dcb3b0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 报告

### 磁盘状态
| 分区 | 大小 | 已用 | 可用 | 使用率 |
|------|------|------|------|--------|
| 根分区 `/` | 30G | 14G | **17G** | 45% |
| 数据盘 `/root/autodl-tmp` | 250G | 26G | **225G** | 11% |

根分区释放了 **13GB**（从 27G → 14G）。

### 符号链接
`/root/provenance_weight_training/output` → `/root/autodl-tmp/provenance_weight_training/output` ✓

### 根分区大文件
- `/root/miniconda3` — 12G（conda 环境，必需）
- `/root/provenance_weight_training` — 6.7G（代码+数据，合理）
- 无异常大文件

### Checkpoint 状态

| Seed | checkpoint-500 | checkpoint-1000 | Resume 建议 |
|------|---------------|----------------|-------------|
| 42 | ✓ 完整（1.13GB + trainer_state） | ✗ 已删除（缺 optimizer/scheduler/rng） | **从 checkpoint-500 resume** |
| 123 | ✓ 完整（1.13GB + trainer_state） | ✗ 已删除（36KB 损坏） | **从 checkpoint-500 resume** |
| 456 | ✓ 完整（1.13GB + trainer_state） | ✗ 已删除（36KB 损坏） | **从 checkpoint-500 resume** |

### GPU 状态
4× NVIDIA RTX PRO 6000 Blackwell (98GB each)，全部空闲（0% utilization, 0 MiB used）。

**结论**：磁盘问题已修复，3 个 uniform baseline 均可从 checkpoint-500 (step 500/6103) resume。4 GPU 空闲待命，可通过 submit_training_job 提交训练。

---
