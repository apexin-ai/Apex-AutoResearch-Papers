# ops diagnose s1 l01 exit

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_diagnose_s1_l01_exit_20260523T055349_result.json`
- **Structured JSON:** [`ebed16aabd18def35dc5.json`](../../sessions/eb/ebed16aabd18def35dc5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

**根因：磁盘满** — `/root/autodl-tmp/` 350G/350G (100%)，仅剩 8KB。

**崩溃详情：**
- 在 step 8000 保存 checkpoint 时触发 `SafetensorError: No space left on device (os error 28)`
- 最后完成的 step: 7999，运行 5h32m
- 最后指标: loss=0.0248, action=0.0243, sdf=0.0357, ee=0.0133

**已保存的有效 checkpoint：**
- step 4000, step 6000, best (step 6000, loss=0.0254)
- `tmp_8000` 是损坏的（仅 384K），需清理

**影响范围：** 所有 4 个实验（s1_l005, s1_l01, s2_l005, s2_l01）全部因同一原因退出。

**磁盘占用分布：**
| 目录 | 大小 |
|------|------|
| checkpoints/ 总计 | 311G |
| baseline_object_pudding | 76G |
| baseline_spatial_bowl | 76G |
| a1_sdf_pi05_object_pudding (4 runs) | 112G |
| a1_sdf_object_pudding | 21G |
| a1_sdf_spatial_bowl | 21G |
| a3_grad_refine | 7.1G |
| .hf_cache | 3.3G |

**恢复需要：** 清理旧 checkpoint（baseline 占 152G）腾出空间后可从 step 6000 resume。

Registry 已更新为 DONE(failed)，cron 之前已不存在。

---
