# exp extended sparsity submit

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_extended_sparsity_submit_20260514T090618_result.json`
- **Structured JSON:** [`a7ef0d5ac5145920c786.json`](../../sessions/a7/a7ef0d5ac5145920c786.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 个实验全部提交成功，registry 已更新为 RUNNING。

**汇总：**

| 实验 | GPU | tmux session | Python PID | 状态 |
|------|-----|-------------|-----------|------|
| bf16_ds_imp_s010 | cuda:0 | bf16_ds_imp_s010 | 102651 | RUNNING |
| bf16_ds_imp_s035 | cuda:2 | bf16_ds_imp_s035 | 102789 | RUNNING |
| bf16_qw_imp_s010 | cuda:3 | bf16_qw_imp_s010 | 102928 | RUNNING |

日志路径：`/root/autodl-tmp/pacs/logs/bf16_ds_imp_s0{10,35}.log` 和 `bf16_qw_imp_s010.log`

参考同类实验，预计每个 ~30-60 分钟完成。bf16_qw_imp_s035 等 cuda:0 释放后再提交。

---
