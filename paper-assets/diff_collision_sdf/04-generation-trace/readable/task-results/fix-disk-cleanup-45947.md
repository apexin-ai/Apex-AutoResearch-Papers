# fix disk cleanup 45947

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_disk-cleanup-45947_20260529T043820_result.json`
- **Structured JSON:** [`b0c501175fc06c2df76e.json`](../../sessions/b0/b0c501175fc06c2df76e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练正常运行。

## 结果汇总

**磁盘清理**（释放 ~47.6G）:

| 已删除 | 大小 |
|--------|------|
| seed2_l1/29999 | 7.2G |
| lora_baseline_seed2/29999 | 7.2G |
| a3_refine_object_seed0/29999 | 7.1G |
| a3_refine_spatial_seed0/29999 | 7.1G |
| baseline_object_pudding_eval/ | 19G |

清理后：250G → 204G used，47G 可用（82%）

**训练重启**:
- PID: 41134（Python 子进程）
- 已从 step 2000 成功 resume
- GPU 0: 100% 利用率，19.1GB/97.9GB 显存
- 当前进度：step 2003/30000，loss=0.1349，~4.4s/it
- 预估完成时间：约 34 小时

---
