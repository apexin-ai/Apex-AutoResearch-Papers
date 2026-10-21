# ops eval prep 34685

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_eval-prep-34685_20260526T105249_result.json`
- **Structured JSON:** [`e99c6adfc85ec43c89ee.json`](../../sessions/e9/e99c6adfc85ec43c89ee.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已写入 `artifacts/eval_commands_34685.md`。

**结果摘要：**

| 实验 | GPU | 50K checkpoint 路径 |
|------|-----|-------------------|
| vanilla_v2_s1 | 0 | `.../vanilla_v2_s1/...-vanilla_v2_s1--50000_chkpt` |
| vanilla_v2_s2 | 1 | `.../vanilla_v2_s2/...-vanilla_v2_s2--50000_chkpt` |
| detach_ln_s3 | 2 | `.../detach_ln_s3/...-detach_ln_s3--50000_chkpt` |
| cutoff_25k_s1_v2 | 3 | `.../cutoff_25k_s1_v2/...-cutoff_25k_s1_v2--50000_chkpt` |

关键发现：
- 4 个实验目前都只有 `dataset_statistics.json`，尚无 checkpoint 保存
- 从 10894 上已完成实验确认 checkpoint 命名 pattern：checkpoint 目录与 run 目录同级，格式为 `{run_name}--{step}_chkpt`
- cutoff_25k_s1_v2 通过 `/proc/453581/cmdline` 确认了 `--run_root_dir` 和 `--run_id_note`
- `/tmp/cutoff_25k_s1_v2.log` 不存在，日志实际在 `~/runs/occsafe_vla/cutoff_25k_s1_v2.log`

---
