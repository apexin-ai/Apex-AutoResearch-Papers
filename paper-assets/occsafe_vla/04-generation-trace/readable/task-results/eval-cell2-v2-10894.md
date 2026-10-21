# eval cell2 v2 10894

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_cell2_v2_10894_20260527T154901_result.json`
- **Structured JSON:** [`b1e2541fed7245d5d4d5.json`](../../sessions/b1/b1e2541fed7245d5d4d5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 eval 均正常启动，正在加载模型（tensorflow GPU warning 是无害的，不影响 PyTorch eval）。

**汇总：**

| Eval | GPU | PID | Checkpoint | tmux session |
|------|-----|-----|------------|--------------|
| full_occ_ln_v2_s1c_eval | cuda:0 | 592547 | `...full_occ_ln_v2_s1c--50000_chkpt` | full_occ_ln_v2_s1c_eval |
| full_occ_ln_v2_s2_eval | cuda:1 | 592815 | `...full_occ_ln_v2_s2--50000_chkpt` | full_occ_ln_v2_s2_eval |

预计每个 eval ~30-40min 完成，约 UTC 16:20-16:30 前出结果。完成后 Cell 2 v2 将有 n=3 数据点。

---
