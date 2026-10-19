# fix disk cleanup immediate

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_disk_cleanup_immediate_20260514T191433_result.json`
- **Structured JSON:** [`6dad31a2b751339b0b0d.json`](../../sessions/6d/6dad31a2b751339b0b0d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。汇总：

### 磁盘清理
| 目录 | 大小 | 状态 |
|------|------|------|
| m2_embed_verify_output/ | — | 不存在（已清） |
| m2_starcoder_output/ | — | 不存在（已清） |
| m2_pilot_data/ | — | 不存在（已清） |
| m2_embed_verify_data/ | — | 不存在（已清） |
| random_s42/final/ | 5.8GB | **已删除** |
| random_s43/final/ | 5.8GB | **已删除** |
| full_m2_outputs/random_s42/ | 4KB | 忽略 |

**释放 ~12GB，可用 108GB → 120GB / 250GB (53%)**

### BM25 early_stopping 修复
- `run_m2_full_qwen.sh`：bm25_s42 的 `--early-stopping-patience 2` **已删除**，s42 将跑完整 3 epoch
- `scripts/run_m2_full_bm25_starcoder.sh`：s42 patience 已经是 0，**无需修改**
- 主循环里 s43/s44 的 `--early-stopping-patience 2` 保持不变

### 训练状态
- 当前跑到 **[2/9] random_s44**，epoch 1，step 350/1408，loss=0.2364
- 双 GPU 100% 利用率，62GB + 54GB 显存
- bm25_s42 是第 7 个 run，脚本修改已在磁盘生效

---
