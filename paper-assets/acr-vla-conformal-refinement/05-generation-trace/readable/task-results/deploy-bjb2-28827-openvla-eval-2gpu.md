# deploy bjb2 28827 openvla eval 2gpu

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_bjb2-28827-openvla-eval-2gpu_20260520T191957_result.json`
- **Structured JSON:** [`578469254e0f549611f1.json`](../../sessions/57/578469254e0f549611f1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### OpenVLA CRM Eval — 情况 B：需要代码适配，无法部署

`evaluate.py` 硬编码了 SmolVLA，不支持 OpenVLA：

| 位置 | 问题 |
|------|------|
| L80 | `--smolvla_path` 参数，无 `--vla_type` 选项 |
| L466-467 | `from smolvla_wrapper import SmolVLAWrapper` 硬编码导入 |
| L468-469 | `SmolVLAWrapper(args.smolvla_path, device=...)` 直接实例化 |
| 全局 | `obs_dim=960` 是 SmolVLA 特征维度，OpenVLA 不同 |

**需要修改才能跑 OpenVLA eval：**
1. 新增 `--vla_type` 参数 (`smolvla` / `openvla`)
2. 条件导入和实例化 VLA wrapper（需要写 `OpenVLAWrapper` 或复用已有的）
3. 根据 VLA 类型设置 `obs_dim`（OpenVLA feature dim ≠ 960）
4. CRM checkpoint 的输入维度需匹配（`crm_openvla_obs_only` 的 CRM 是用 OpenVLA features 训练的，obs_dim 不同）

### D088 Eval 状态（非 D088-prefixed，n_rollouts=10）

| Seed | PID | 状态 | SR |
|------|-----|------|----|
| 42 | 741948 | **仍在运行** (cuda:0) | — |
| 43 | 742213 | **仍在运行** (cuda:1) | — |
| 44 | 728278 | **完成** → DONE/negative | **11%**（baseline ~14%）|

seed44 详细：`adaptive_trigger_rate=0.0`, `avg_K=1.0`, `crm_trigger_rate=87.95%` — uncertainty head 在 τ=0.42 下从未触发 K>1，全程 K=1 单样本 + selective CRM。

### 清理

- **norm003-seed43**：只有 1 个进程（PID 742550, cuda:4），无重复，无需 kill。

---
