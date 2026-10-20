# ops fix deepseek seed123 launch

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fix-deepseek-seed123-launch_20260523T095337_result.json`
- **Structured JSON:** [`20d35cd51d3669165b2c.json`](../../sessions/20/20d35cd51d3669165b2c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练已成功启动并在跑。

**状态汇总：**
- **PID**: 874893
- **GPU**: cuda:0, 98% 利用率, 23112MiB 进程显存 (72293MiB 总占用含 ~49GB 僵尸)
- **训练阶段**: 已进入 training loop (0/444 steps), gradient checkpointing 已启用
- **cuda:1**: 未受影响 (CodeLlama PID 870613, 100%)

**原始命令的 bug**: `cd /root/autodl-tmp/trace-verdict-study` 路径不存在。已修正为 `cd /root/trace-verdict-study`，同时修正了 model_path 和 python 路径。

---
