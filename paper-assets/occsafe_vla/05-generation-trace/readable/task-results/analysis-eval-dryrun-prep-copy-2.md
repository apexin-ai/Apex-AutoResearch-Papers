# analysis eval dryrun prep

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval_dryrun_prep_20260525T055947_result.json`
- **Structured JSON:** [`ae6cd3dc4630f6c52b41.json`](../../sessions/ae/ae6cd3dc4630f6c52b41.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run 完成，一切正常。

**结果汇总：**

1. ✅ 两个脚本已创建：
   - `/root/occsafe_vla/eval_batch_34685.sh` — 单实验 eval
   - `/root/occsafe_vla/scp_and_eval.sh` — scp + eval 一键

2. ✅ Dry-run 成功（`full_occ_retrain_s0`, cuda:2, 1 rollout）：
   - 10 tasks 全部完成，耗时 60s
   - TSR=0.9000 (90%), CAR=0.8000 (80%)
   - 结果保存至 `/root/occsafe_vla/artifacts/safelibero_libero_spatial_20260525_140125.json`

**34685 训练完成后的使用方式：**
```bash
# 在 10894 上，对每个实验分配一个 GPU
bash /root/occsafe_vla/scp_and_eval.sh cutoff_25k_s2_v3 0 0
bash /root/occsafe_vla/scp_and_eval.sh reverse_cutoff_s2_v3 1 1
bash /root/occsafe_vla/scp_and_eval.sh cutoff_45k_s1_v3 2 2
bash /root/occsafe_vla/scp_and_eval.sh cutoff_15k_s2_v2 3 3
```

---
