# eval occ s1 45K deploy auto eval

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_occ-s1-45K-deploy-auto-eval_20260521T115404_result.json`
- **Structured JSON:** [`bbb15097a32e47e2c6c0.json`](../../sessions/bb/bbb15097a32e47e2c6c0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个脚本已成功部署并在后台运行：

| 脚本 | PID | GPU | 状态 |
|------|-----|-----|------|
| auto_eval_45K.sh | 389300 | cuda:0 | 等待 45000_chkpt 中 |
| auto_eval_50K.sh | 389317 | cuda:2 | 等待 50000_chkpt 中 |

checkpoint 出现后会自动验证完整性（safetensors 文件数）并启动 eval（20 rollouts）。日志分别写入 `/root/eval_logs/occ_s1_45000_eval.log` 和 `/root/eval_logs/occ_s1_50000_eval_20r.log`。

---
