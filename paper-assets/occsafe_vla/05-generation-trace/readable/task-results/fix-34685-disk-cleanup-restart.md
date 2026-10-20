# fix 34685 disk cleanup restart

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_34685-disk-cleanup-restart_20260527T211548_result.json`
- **Structured JSON:** [`0773096722493d435fec.json`](../../sessions/07/0773096722493d435fec.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个 GPU 全部 99% 利用率，两个实验已开始训练。

## 汇报

### Phase 1: 磁盘清理
| 删除项 | 大小 |
|--------|------|
| detach_ln_v2_s2 不完整 20000_chkpt | 6.1G |
| vanilla_object_s0 不完整 15000_chkpt | 532K |
| detach_ln_s3 中间 40000_chkpt | 15G |
| full_occ_ln_v2_s3 旧 10000_chkpt | 15G |
| detach_ln_v2_s3 旧 10000_chkpt | 15G |
| **总计释放** | **~51G** |

磁盘：60G → **110G free** (69% used)

### Phase 2: 实验重启
| 实验 | GPU | Resume Step | 剩余步数 |
|------|-----|------------|---------|
| detach_ln_v2_s2 | cuda:0 | 15000 | 35005 |
| vanilla_object_s0 | cuda:1 | 10000 | 40005 |

两个实验已成功加载 checkpoint 并开始训练（action_loss 正常：0.14 / 0.19）。

### Phase 3: 状态确认
- 4 个 GPU 全部 99% 利用率，62GB 显存
- 代码内置 checkpoint 轮转（保留最近 3 个），磁盘不会再爆

### ETA 预估（~1.0s/step）
| 实验 | 预计完成 (UTC) | 北京时间 |
|------|---------------|---------|
| detach_ln_v2_s2 | ~15:00 | ~23:00 |
| vanilla_object_s0 | ~16:30 | ~00:30 (29日) |
| full_occ_ln_v2_s3 | ~14:40 | ~22:40 |
| detach_ln_v2_s3 | ~14:40 | ~22:40 |

**注意**：4 个实验都会超出 12:00 UTC deadline 约 3-4.5 小时。

---
