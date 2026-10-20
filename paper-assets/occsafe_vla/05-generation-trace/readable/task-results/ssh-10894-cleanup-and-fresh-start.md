# ssh 10894 cleanup and fresh start

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_10894_cleanup_and_fresh_start_20260525T203528_result.json`
- **Structured JSON:** [`6a5f69de646e0c3cd2e8.json`](../../sessions/6a/6a5f69de646e0c3cd2e8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成。

## 10894 清理 + 从头启动

### 磁盘
清理前: 数据盘 (`/dev/md0`) ~252G/250G (~100%)，根分区 22G/30G (71%)
清理后: 数据盘 142G/250G (57%, 109G available)，根分区 15G/30G (48%)

删除明细:
- mvp_occ_s3: 30G
- full_occ_ln_s3: 30G
- ablation_occ_detach_s3: 35G
- full_occ_retrain_s0: 15G
- pip cache: 5.95G
- conda cache: 0.16G
- 总计释放: ~116G

### 实验状态
| 实验 | GPU | PID | 状态 | 训练类型 | 预计完成 (UTC) |
|------|-----|-----|------|----------|---------------|
| cutoff_45k_s2_v2 | cuda:0 | 4294 | 运行中 (step ~11K/50K) | 从头 | ~May 26 14:40 |
| mvp_occ_s3_v2 | cuda:1 | 33897 | 新启动 | 从头 | ~May 26 17:30 |
| full_occ_ln_s3_v2 | cuda:2 | 34102 | 新启动 | 从头 | ~May 26 17:30 |
| ablation_occ_detach_s3_v2 | cuda:3 | 34443 | 新启动 | 从头 | ~May 26 17:30 |

### 磁盘空间是否足够存未来 checkpoint: ✅
109G available, 每实验 ~15G × 4 = ~60G needed, 余量充足。

### 注意
用户给的启动命令参数有误（`--occ_loss_type` 不是有效参数），已根据 registry 中历史正确命令和运行中 cutoff 进程的实际参数修正为 `--use_occ_head True --occ_detach false/true --occ_norm_type ln/bn`，并使用 `torchrun --standalone` 而非 plain `python`。

---
