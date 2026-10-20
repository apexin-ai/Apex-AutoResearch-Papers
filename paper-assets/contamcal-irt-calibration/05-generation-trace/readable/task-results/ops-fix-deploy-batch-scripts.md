# ops fix deploy batch scripts

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fix-deploy-batch-scripts_20260516T035204_result.json`
- **Structured JSON:** [`5e706e98b8e3f940ad21.json`](../../sessions/5e/5e706e98b8e3f940ad21.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

0.5B d000_s123/mmlu 正在 cuda:5 运行中（s1_embedding 和 s2_minkpp 已完成，s4_selfcritique 进行中）。其余 11 个子任务尚未开始。

## 报告

### 1. 脚本状态
- **部署前**: 0.5B 提交时脚本不存在 → EXIT_CODE=127
- **部署后**: 两个脚本均已存在，创建于 10:28，权限 `-rwxr-xr-x`
  - `/root/contamcal-irt-calibration/exp002/run_05B_s123_signals.sh`
  - `/root/contamcal-irt-calibration/exp002/run_15B_s123_signals.sh`
- 内容正确（4 dosages × 3 benchmarks = 12 tasks，含 conda 激活、离线模式、失败计数）

### 2. 1.5B 状态
- **正常运行中**，无 EXIT_CODE=127 错误
- cuda:0，PID 691872，当前任务：d000_s123/mmlu Reference log-probs ~24%（3366/14042）
- 脚本在提交前已创建，1.5B 批次无需修复

### 3. 0.5B 当前状态
- cuda:5 上有单独启动的 d000_s123/mmlu 任务（非批次脚本），进行中
- 已完成信号：s1_embedding_mmlu, s2_minkpp_mmlu
- 正在计算：s4_selfcritique_mmlu（chunks 目录已创建）
- 完成后 cuda:5 空闲，不会自动继续其余 11 个子任务

### 4. 0.5B 后续计划
- 等 cuda:5 当前 d000_s123/mmlu 完成
- 重提交完整批次到 cuda:5：`bash run_05B_s123_signals.sh`
- 注意：现有脚本无 skip-if-done 逻辑，d000_s123/mmlu 会被重新计算。如需避免重复，可在提交前给脚本加上 skip 逻辑。是否需要？

---
