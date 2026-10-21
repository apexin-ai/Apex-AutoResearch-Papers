# infra westd30476 1 7b check

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_westd30476_1_7b_check_20260520T041510_result.json`
- **Structured JSON:** [`e925079befd2f73e466f.json`](../../sessions/e9/e925079befd2f73e466f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总报告

| 项目 | 状态 | 详情 |
|------|------|------|
| **1.7B 模型权重** | ❌ 缺失 | 服务器上只有 `Qwen3-0.6B`（在 `/root/provenance_weight_training/models/Qwen/Qwen3-0.6B`），未找到任何 `Qwen3-1.7B` 目录 |
| **训练数据** | ✅ 存在 | `/root/provenance_weight_training/data/scored_data.jsonl`，371,499 行，~930MB |
| **训练代码** | ✅ 存在 | `/root/provenance_weight_training/training/pretrain_weighted.py`（May 18 更新） |
| **已有 1.7B 输出** | ❌ 无 | `adaptive_1_7b_seed42`、`uniform_1_7b_seed42`、`uniform_1_7b_seed42_resumed` 均不存在。仅有一个旧输出：`batchsize16_nmin8_r2` |
| **q=0.2 / q=0.5 checkpoint** | ❌ 无 | 无任何 `detect_remove*` 目录 |
| **GPU** | ✅ 4× NVIDIA RTX PRO 6000 Blackwell Server Edition | 每卡 ~96GB 显存，当前全部空闲（0 MiB used） |
| **磁盘** | ✅ 充足 | 数据盘 `/root/autodl-tmp/` 111GB 可用；根分区 20GB 可用 |

**结论**：需要先下载 Qwen3-1.7B 模型权重到服务器，其余条件（数据、代码、GPU、磁盘）均已就绪。

---
