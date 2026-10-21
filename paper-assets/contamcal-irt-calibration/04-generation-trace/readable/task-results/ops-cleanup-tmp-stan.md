# ops cleanup tmp stan

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cleanup-tmp-stan_20260515T092250_result.json`
- **Structured JSON:** [`5a0acf85e2c9e07af91b.json`](../../sessions/5a/5a0acf85e2c9e07af91b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已删除 4 个 Stan tmp 目录，释放约 **714MB**。

- 清理前：20G used / 11G avail (65%)
- 清理后：19G used / 12G avail (63%)

剩余 tmp 目录均为 wandb 临时文件和一个小目录 (`tmp897tun7i`)，无其他大型 Stan/CmdStan 目录。

---
