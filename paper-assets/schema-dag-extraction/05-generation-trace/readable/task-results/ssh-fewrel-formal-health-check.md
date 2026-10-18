# ssh fewrel formal health check

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_fewrel-formal-health-check_20260515T120947_result.json`
- **Structured JSON:** [`437c1ea511787dbbdaf6.json`](../../sessions/43/437c1ea511787dbbdaf6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验启动失败

**原因**：缺少必需参数 `--mode`。脚本立即退出并打印 usage 信息：

```
run_fewrel_formal.py: error: the following arguments are required: --mode
```

**状态汇总**：
- PID 262365：已死亡
- GPU 占用：无
- 日志仅包含 argparse 报错，未进入任何实际执行阶段

**修复**：重新提交时需加 `--mode` 参数（可选值：`exp1`, `exp2`, `dry_run`）。建议先用 `--mode dry_run` 验证流程，再跑正式实验。

---
