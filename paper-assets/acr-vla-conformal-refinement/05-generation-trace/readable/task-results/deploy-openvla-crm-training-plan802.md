# deploy openvla crm training plan802

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_openvla-crm-training-plan802_20260520T183812_result.json`
- **Structured JSON:** [`69cb9d51467530e11ffd.json`](../../sessions/69/69cb9d51467530e11ffd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

部署完成。

**结果汇总：**
- **PID**: 778591（tmux session: `crm-openvla-train`）
- **GPU**: cuda:3，占用 541 MiB，5% utilization
- **初始 loss**: ~0.19–0.26（epoch 1 正常下降中）
- **Cron**: 已注册，120s 间隔监控

**代码修复**：`train_crm.py` 原本硬编码 `H_EFF=5`，但 OpenVLA precompute 产出的 `h_eff=1`。做了 3 处修改：
1. 从 manifest 读取 `h_eff` 替代硬编码常量
2. `obs_only` 模式跳过 CGS 计算（K=1 无法计算协方差）
3. 合并了 74,507 个独立 sample 文件为 `obs_features.pt` / `k_samples.pt` / `expert_actions.pt`

---
