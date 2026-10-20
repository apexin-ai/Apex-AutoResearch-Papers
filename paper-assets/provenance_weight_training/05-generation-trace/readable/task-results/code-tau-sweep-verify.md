# code tau sweep verify

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_tau_sweep_verify_20260515T123928_result.json`
- **Structured JSON:** [`27b6abc33dee1d651cf0.json`](../../sessions/27/27b6abc33dee1d651cf0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证完毕，结果已写入 `artifacts/tau_sweep_commands.md`。

**结论**：4 个 tau sweep 脚本全部就绪，无需创建。

- 脚本路径：`training/run_tau_0.{5,7,9,95}_seed42.sh`
- 参数、数据路径、模型路径均验证通过
- 输出目录尚未创建（训练时自动创建）
- **当前阻塞**：4 个 GPU 全被占用。GPU 1 最先释放（~9 min），GPU 2 最晚（~105 min）
- 预计 4 个实验共 **~14.8 GPU-hours**，wall-clock **~5.5 小时**完成

---
