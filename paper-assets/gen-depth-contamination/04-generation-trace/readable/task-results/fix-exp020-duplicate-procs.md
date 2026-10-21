# fix exp020 duplicate procs

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_exp020_duplicate_procs_20260516T113129_result.json`
- **Structured JSON:** [`53c602f6880800d196ff.json`](../../sessions/53/53c602f6880800d196ff.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。汇总：

### 结果

1. **Kill 的进程**: PID 27742 和 28604 已成功终止。PID 27042 继续运行。

2. **数据完整性**: **正常。** 所有 6 个 depth 文件 (depth_0 ~ depth_5) 各 5000 行，符合 `--num_samples 5000` 预期。数据生成阶段已全部完成。

3. **nuc09 当前进度**: 数据生成已完成（6 个 depth 全部 5000 行）。`results_exp020_pythia_nuc09/` 目录为空，说明 PID 27042 正在执行后续的 evaluation/results 阶段。

4. **重复启动原因**: 脚本 `exp020_pythia_decoding.sh` 本身是串行的（4 个 config 顺序执行），不会并行启动。从进程参数看：
   - PID 27742 用的 `--model_path EleutherAI/pythia-1.4b`（HF hub ID，非本地路径）
   - PID 27042 和 28604 用的本地 snapshot 路径
   
   说明有人手动执行了至少 2 次额外启动（可能是脚本失败后重跑、或误操作多次 `nohup` 同一命令）。不是脚本 bug，是人为重复触发。

---
