# infra eval prestage s3 d051

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_eval-prestage-s3-d051_20260525T202557_result.json`
- **Structured JSON:** [`00a8ed6dbb301a70b5cd.json`](../../sessions/00/00a8ed6dbb301a70b5cd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Report saved. Here's the executive summary:

---

**CRITICAL — westd-10894 磁盘已满，3 个实验已崩溃**

3 个 resume 实验在保存 30000_chkpt 时因磁盘满 (250G/250G) 全部崩溃 (exit code 1, ~04:24 UTC):
- **ablation_occ_detach_s3**: 30000_chkpt 完整，可立即 eval
- **full_occ_ln_s3**: 30000_chkpt 损坏，需从 20000_chkpt 重跑 10K steps
- **mvp_occ_s3**: 30000_chkpt 未创建，需从 20000_chkpt 重跑 10K steps

**cutoff_45k_s2_v2** 仍在运行 (step 10624/50005)，但下次保存时 (~8h 后) 也会因磁盘满崩溃。

**另外发现**: `eval_batch_10894.sh` 和 `cka_batch_s3.sh` 对 resume 实验写的是 `50000_chkpt`，实际应为 `30000_chkpt`。

**紧急行动**:
1. 立即清理 10894 旧 checkpoint (~121G 可回收：cutoff_45k_s2 v1、full_occ_ln_s0/s1/s2 等)
2. 删除损坏的 full_occ_ln_s3 30000_chkpt
3. 清空后重跑 mvp_occ_s3 和 full_occ_ln_s3 各 10K steps (~2.5h each)
4. 修复脚本中的 checkpoint 路径

**westd-34685**: 4 个实验正常训练中，61G 空间充足，eval 脚本和数据就绪。

详细报告已保存到 `artifacts/eval_readiness_report.md`，含所有 eval/CKA 命令模板。

---
