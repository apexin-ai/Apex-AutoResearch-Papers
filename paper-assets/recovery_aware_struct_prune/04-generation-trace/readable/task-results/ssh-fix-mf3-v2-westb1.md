# ssh fix mf3 v2 westb1

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_fix_mf3_v2_westb1_20260522T150659_result.json`
- **Structured JSON:** [`5639717ef821f659f916.json`](../../sessions/56/5639717ef821f659f916.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GPU:1 98% utilization，13015 MiB 占用，正在生成第一个 sample。进度条用 `\r` 覆写所以 tail 看不到更新。进程健康运行中。

## 汇报

| 项目 | 结果 |
|------|------|
| 旧进程 kill | PID 217798 已 kill（SIGTERM 成功） |
| 正确 model_path | `/root/autodl-tmp/recovery_aware_struct_prune/grpo_qwen_math_cka_only_20`（config.json + model.safetensors 12G 均存在） |
| 新 PID | bash wrapper: 220338, python 实际进程: **220343** |
| GPU:1 显存 | **13015 MiB**，utilization 98% |
| 推理状态 | 模型已加载，500 samples 推理进行中。第一个 sample 正在生成（max_new_tokens=2048，tqdm 用 `\r` 刷新所以日志文件看不到中间进度） |

**修复点**：原崩溃因 `python` 命令在非 conda 环境下不存在 + 相对路径。本次用 `source conda.sh && conda activate base` + 绝对路径解决。预估 ~61s/sample，500 samples 约 8.5 小时完成。

---
