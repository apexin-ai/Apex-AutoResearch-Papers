# deploy bjb2 28827 gpu1 5 smolvla

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_bjb2-28827-gpu1-5-smolvla_20260524T064526_result.json`
- **Structured JSON:** [`391e90c95cee777dc083.json`](../../sessions/39/391e90c95cee777dc083.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 4 个 eval 已部署并进入 rollout 阶段。

## 部署结果

| GPU | 实验 ID | tmux session | 状态 |
|-----|---------|--------------|------|
| 2 | eval-supp-vla-only-spatial-s45 | 同名 | RUNNING，model loaded, env loaded |
| 3 | eval-supp-crm-norm005-spatial-s45 | 同名 | RUNNING，CRM loaded, norm=0.05 override 生效 |
| 4 | eval-supp-adapt-tau025-spatial-s45 | 同名 | RUNNING，CRM loaded, norm=0.2 + conformal_threshold=0.25 |
| 5 | eval-supp-vla-only-spatial-s46 | 同名 | RUNNING，model loaded, env loaded |

GPU 显存均 ~6.2 GB，利用率 17–30%。日志写到 `/root/acr-vla-conformal-refinement/logs/&lt;session>.log`，JSON 输出会自动落到 `logs/eval_spatial_*_seed4{5,6}.json`。

## 参数修正
任务里给的 `--crm_norm` 和 `--tau` 不是 evaluate.py 的有效 flag，已映射到实际参数名：
- `--crm_norm` → `--max_correction_norm`
- `--tau` → `--conformal_threshold`

## 服务器状态提醒
- **GPU 0 的 crm-openvla-k1 训练已正常完成**（50/50 epoch，best val_loss=0.077477，checkpoint 在 `/root/autodl-tmp/checkpoints/crm_openvla_k1_multiscale/object`），session 已自行退出，GPU 0 当前 1 MiB 空闲。
- GPU 1 仍空闲（0 MiB）。
- 没有发现需要清理的 eval-goal-*/eval-long-* 旧 session。

## 命名注意
注册表里已存在 `eval-supp-spatial-vla-only-s45` 和 `eval-supp-spatial-crm-norm005-s45`（之前在 cqa1-32758 跑过的「第六 seed」实验，suite-mode-seed 顺序）。本次任务使用的 `eval-supp-&lt;mode>-spatial-s&lt;seed>` 是新条目，两套不冲突。

---
