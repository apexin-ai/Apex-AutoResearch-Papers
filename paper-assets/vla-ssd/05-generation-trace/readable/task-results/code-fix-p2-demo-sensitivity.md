# code fix p2 demo sensitivity

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix_p2_demo_sensitivity_20260516T102929_result.json`
- **Structured JSON:** [`5a376d37741e580dd2f3.json`](../../sessions/5a/5a376d37741e580dd2f3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**脚本修复完毕，dry-run 验证通过。**

- **L0 RSA 50demos = 0.6117**（与主分析一致，之前错误值是 0.048）
- **L0 RSA 25demos = 0.5931**
- Probe 部分未动，L0 50demos=0.6448, 25demos=0.5709

修复内容：`compute_rsa_for_layer` 从 "demo-mean-then-distance" 改为 Method B "timestep-wise pdist then average"——对每个 timestep 算 pairwise cosine rep distance + euclidean action distance，跨 timestep 平均后做 Spearman。

旧进程（PID 720674，跑了 32 分钟的错误代码）已一并 kill。等待 submit_training_job 提交完整实验。

---
