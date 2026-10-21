# submit downsample eval retry

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_submit_downsample-eval-retry_20260519T065446_result.json`
- **Structured JSON:** [`4bbdfde069b06adff965.json`](../../sessions/4b/4bbdfde069b06adff965.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

推理已启动，模型加载成功并开始 inference。registry 已更新为 RUNNING。

**总结：**
- **失败原因 1**：上次提交用了错误的参数名（`--adapter_path` vs `--checkpoint_dir` 等），EXIT_CODE=2
- **失败原因 2**：第二次修复参数名后，GPU 1 被其他进程占用 18GB，导致 OOM
- **当前状态**：已迁移到空闲的 GPU 2，pid=808206，推理正常运行中（9784 test instances, batch_size=16）

---
