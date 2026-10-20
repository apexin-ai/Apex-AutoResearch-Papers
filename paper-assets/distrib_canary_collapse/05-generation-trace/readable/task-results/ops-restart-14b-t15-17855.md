# ops restart 14b t15 17855

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_restart-14b-t15-17855_20260522T090739_result.json`
- **Structured JSON:** [`ba46f96ccd841a83b677.json`](../../sessions/ba/ba46f96ccd841a83b677.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。验证结果：

- **GPU 0**: 10293 MiB 占用, 89% utilization — `scale_14b_t15_a060_v2` (PID 656957) 运行中
- **GPU 1**: 10293 MiB 占用, 89% utilization — `scale_14b_t15_a050_v2` (PID 657037) 运行中
- 两个 tmux session (`scale_14b_t15_a060_v2`, `scale_14b_t15_a050_v2`) 均已创建
- 两个 python 进程均从 `--start_gen 2` 启动，使用正确的 `HF_HOME=/root/autodl-tmp/.hf_cache`

日志分别在 `/tmp/t15_a060_v2.log` 和 `/tmp/t15_a050_v2.log`。

---
