# deploy bjb2 28827 openvla

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_bjb2-28827-openvla_20260524T062541_result.json`
- **Structured JSON:** [`231173c9f5dcb120c4a9.json`](../../sessions/23/231173c9f5dcb120c4a9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练运行至 epoch 12/50，每 epoch ~10s，预计 ~8 分钟内完成。GPU 1-5 因 eval pipeline 阻塞未部署额外任务。

## 部署汇报：bjb2-28827

### 当前状态
| GPU | 任务 | tmux | 状态 |
|---|---|---|---|
| 0 | OpenVLA CRM K=1 MultiScale 训练 (object) | `crm-openvla-k1` | RUNNING, epoch 12/50 |
| 1-5 | 空闲 | — | — |

### 实验：`crm-train-openvla-k1-multiscale-object` (registry RUNNING)
- **架构**：`MultiScaleCRM` (plan_700 K=1)，action_dim=6, obs_dim=4096, 4 层注意力融合
- **参数**：908,106 (vs SmolVLA 323K，因 obs_dim 大 4×)
- **数据**：`/root/autodl-tmp/crm_cache_k1_openvla/object` (74507 samples，预计算缓存)
- **超参**：50 epochs, batch_size=512, lr=1e-3, multi-loss, seed=42
- **输出**：`/root/autodl-tmp/checkpoints/crm_openvla_k1_multiscale/object`
- **日志**：`/root/acr-vla-conformal-refinement/logs/crm-openvla-k1-multiscale-object.log`
- **进度**：epoch 12, train_loss=0.227, val_loss=0.0775 (best at epoch 6)
- **观察**：direction loss 0.75 主导，与之前 `train-crm-openvla-obs-only` (best_val=0.0772) 同水位，说明 OpenVLA 特征对 action correction 信号弱——和 SmolVLA 不同。

### 代码适配（已做）
1. **`src/train_crm_k1.py`**：从 cache 自动检测 `actual_h_eff = vla_action.numel() // CORRECTION_DIM`（SmolVLA=5, OpenVLA=1），替换硬编码的 `H_EFF * CORRECTION_DIM` 和 `noise_scale.repeat(H_EFF)`。备份 `*.bak_pre_openvla_*`。
2. **`src/utils.py`**：补 `VLA_CONFIGS` + `get_vla_config()` 工具，让 `openvla_eval.py` import 通过。

### 阻塞：OpenVLA Eval Pipeline 不可用
GPU 1-5 未部署的根因：

1. **`openvla_wrapper.py` 加载失败** — 模型 `config.json` 的 `model_type: "openvla"` 在当前 `transformers 5.8.1` 中无 auto_map 注册。Wrapper 调用 `AutoModelForImageTextToText.from_pretrained(...)` 报 `ValueError: model type 'openvla' not recognized`。
2. **fallback 注册路径也断了** — `prismatic.extern.hf.modeling_prismatic.OpenVLAForActionPrediction` 仍可 import，但 `AutoModelForVision2Seq` 在 transformers 5.x 已移除，无法走旧的 `AutoConfig.register('openvla', ...)` 路径。
3. **`openvla_eval.py` 用旧 K=10 `ConformalRefinementModule`** — 即使模型能加载，也不支持新 K=1 `MultiScaleCRM` 推理模式，需新增 `--mode crm_k1_multiscale` 分支。

之前 `eval-openvla-object-vla-only-seed42-v2` (SR=69%) 跑通时使用的应是更早版本的 transformers + 不同 wrapper。

### 建议下一步（待 Director 决定）
- **训练完成后**（~8 分钟）：自动 DONE，不需要立即 eval。
- **解锁 OpenVLA eval**：需要 (a) 修复 wrapper 到 transformers 5.x（migrate to `AutoModelForImageTextToText` + manual register via `AutoConfig.register` + 找新的 ModelClass），(b) 给 `openvla_eval.py` 加 `crm_k1_multiscale` 模式。预估 1-2 小时工作量。
- **替代用 GPU 1-5**：当前没有可立即部署的 SmolVLA 任务（spatial/object/goal s45/s46 已 DONE，long s46 在其他服务器跑）。可考虑：跨 backbone 迁移实验、或等训练完后并行多 seed eval。

---
