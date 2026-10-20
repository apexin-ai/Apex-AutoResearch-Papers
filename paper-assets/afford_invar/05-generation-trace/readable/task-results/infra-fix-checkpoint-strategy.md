# infra fix checkpoint strategy

**afford invar** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_fix-checkpoint-strategy_20260520T002115_result.json`
- **Structured JSON:** [`782d2efda9865bff5748.json`](../../sessions/78/782d2efda9865bff5748.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇报：

---

## 修复结果

### 磁盘
- **清理前**: 158G used (45%)
- **清理后**: 143G used (41%)
- **释放**: ~15GB（删除了 2500、3000、3500、4000 四个旧 OFT checkpoint）

### Checkpoint 内容分析
| 训练 | 每 checkpoint 大小 | 原因 |
|------|------------------|------|
| **OFT baseline** | **15GB** | `merge_lora_during_training=True`（默认），每次保存都 merge_and_unload → 4 个 model shards (~14.8GB) + action_head (288MB) |
| **transfer_v2** | **756MB** | 只存 adapter_model.safetensors (462MB) + action_head (288MB)，无 merge |

### 修复措施
1. **Kill OFT baseline** 并从 step 4500 checkpoint resume
2. **新参数**: `--merge_lora_during_training False --save_freq 2000`
   - 未来 checkpoint 从 15GB 降至 ~756MB
   - 保存频率从 500 步 → 2000 步
3. 当前仅剩 4500_chkpt (15GB) 作为 resume 基点，当 2 个新 checkpoint 产生后会被 cleanup 脚本自动清理
4. Cleanup 脚本仍在运行（每 300 秒，保留最新 2 个）

### 训练进程状态
| 训练 | 状态 | 当前 step | 速度 |
|------|------|----------|------|
| OFT baseline (v2) | 已 resume，运行中 | ~4520 | ~4.2 it/s |
| transfer_v2 | 正常运行 | ~3870 | ~4.5 it/s |

### 注意事项
- 4500_chkpt 含 merged model，可直接用于推理评估；后续 checkpoint 只含 adapter，需要离线 merge
- 新 OFT baseline 在 tmux session `oft_baseline_v2` 中，日志在 `/root/afford_invar/results/phase1_oft_baseline_v2.log`

---
