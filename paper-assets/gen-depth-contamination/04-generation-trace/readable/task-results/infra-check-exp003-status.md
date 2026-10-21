# infra check exp003 status

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_check_exp003_status_20260513T064031_result.json`
- **Structured JSON:** [`74dc494108cce1043c0d.json`](../../sessions/74/74dc494108cce1043c0d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp-003 状态报告

**exp-003 未在运行，且从未成功启动。**

### 原因
脚本 `scripts/run_exp003_ablation.sh` 需要一个参数 `{1|2|3|4}` 指定配置编号，但 `submit_training_job` 调用时未传入该参数。日志显示脚本被调用了 4 次，每次都打印 Usage 后以 `EXIT_CODE=1` 退出。

### 详细状态
- **tmux session**: 无（已退出或从未创建）
- **相关进程**: 无
- **GPU**: 空闲（0% utilization, 0 MiB memory）
- **结果文件**: 无 `results_exp003_*` 或 `data_exp003_*` 目录
- **日志**: `/root/runs/gen-depth-contamination/exp_003_decoding_ablation.log`（716字节），内容为 4 次重复的 usage 提示

### 根因
提交命令缺少必需的 config 编号参数。需要以 `run_exp003_ablation.sh 1`、`run_exp003_ablation.sh 2` 等方式分别调用，或修改提交逻辑依次运行 4 个配置。

---
