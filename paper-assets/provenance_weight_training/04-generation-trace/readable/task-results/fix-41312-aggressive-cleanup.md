# fix 41312 aggressive cleanup

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_41312_aggressive_cleanup_20260518T145644_result.json`
- **Structured JSON:** [`9f8ef1fa8525ca5f47e4.json`](../../sessions/9f/9f8ef1fa8525ca5f47e4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

清理完成。

## 清理报告

### 1. 服务器确认
westd-41312 (通过 df 确认 `/dev/md0` 250G 磁盘)

### 2. 清理前
| 分区 | 已用 | 可用 | 使用率 |
|------|------|------|--------|
| /root/autodl-tmp | 250G | 68K | **100%** |
| / (overlay) | 9.4G | 21G | 32% |

### 3. 删除明细

| 操作 | 释放空间 |
|------|----------|
| Llama 训练输出 (llama3b_uniform + llama3b_adaptive) | ~50G |
| Llama 模型文件 (models/meta-llama/) | ~6.8G |
| uniform_1_7b checkpoint-1500/2000/2500 | ~29.1G |
| adaptive_1_7b checkpoint-1500/2000 | ~19.4G |
| contamination_60_* 中间 checkpoint (x4 大 + x2 小) | ~48G |
| 其他模型中间 checkpoint (12 个实验) | ~36G |
| 失败实验 (uniform_seed42 + grid_b0_2_seed123) | ~3.4G |
| HuggingFace cache | ~223M |
| __pycache__ + 旧 log | 微量 |

### 4. 清理后
| 分区 | 已用 | 可用 | 使用率 |
|------|------|------|--------|
| /root/autodl-tmp | **60G** | **191G** | **24%** |
| / (overlay) | 9.3G | 21G | 31% |

### 5. 空间评估
释放了 **~190G**。可用 191G，**足够启动 4 个训练**（需 ~30G）。

### 6. 保护文件验证
- `uniform_1_7b_seed42/checkpoint-3000` ✓
- `adaptive_1_7b_seed42/checkpoint-2500` ✓
- `scored_data*.jsonl` (9 个文件) ✓
- `models/Qwen/` ✓
- 所有 `final/` 目录 ✓（每个实验仅保留 final）
- `eval_holdout.jsonl` 在该路径不存在（可能在其他位置或该服务器上未部署）

---
