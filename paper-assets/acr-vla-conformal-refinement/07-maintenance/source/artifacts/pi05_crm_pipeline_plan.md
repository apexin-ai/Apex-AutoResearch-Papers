# π0.5 CRM Pipeline 方案 (2026-05-21, updated)

## 0. 当前阻塞状态

### Baseline Eval 全线 0% SR

6 个 baseline 实验（3 seeds × Object + Spatial）全部失败：

| 实验 | SR | 状态 |
|------|-----|------|
| Object seed42/43/44 | 0.0% (0/200 each) | 完成，EXIT_CODE=0 |
| Spatial seed42/43/44 | 0.0% (前 8 task) | 中途死亡（task 9, rollout 10/20） |

**根因进化**：不再是之前的 vision tower 单一问题，而是**双重 key mismatch**：
- Vision tower: 437 keys 已成功 remap (`vision_tower.vision_model.` → `vision_tower.`) ✅
- Language model + multi_modal_projector: **376 keys 仍 missing** ❌
  - `model.paligemma_with_expert.paligemma.model.language_model.*`
  - `model.paligemma_with_expert.paligemma.model.multi_modal_projector.*`
- 结果：vision tower 有真实权重，但 **language model 在随机权重下运行** → 0% SR
- 附加症状：gripper 恒定 ~0.98（始终 open），无法执行 pick

**官方 lerobot-eval patched 版本 3/3 = 100% SR**，证明模型本身有效。

### 阻塞解除条件
在 `_fix_pytorch_state_dict_keys`（或 `pi05_wrapper.py` 的 `_fix_vision_tower_keys`）中追加 language_model + multi_modal_projector 的 key remap，使 load_state_dict missing_keys = 0。验证方式：至少 1 个 task SR > 0%。

---

## 1. 现状摘要

### SmolVLA 现有 pipeline（LOCKED）
- `SmolVLAWrapper` (`src/smolvla_wrapper.py`)
  - `encode_prefix(...)` → `obs_features (B, 960)`, `kv_cache`, `prefix_pad_masks`
  - `generate_k_samples(kv, masks, K)` → `(B, K, chunk_size=50, FULL_ACTION_DIM=7)`
  - `preprocess_obs_batch` 已支持 batched precompute
- `MultiScaleCRM` (`src/crm_k1_model.py`)
  - 输入: `base_action (B, 30)` + `multi_scale_obs (B, 4, 960)` 或 fallback `(B, 960)`
  - 参数: `action_dim=30`, `obs_dim=960`, `hidden_dim=256`, `bottleneck_dim=192`
  - ~323K params
- `MultiScaleFeatureExtractor`
  - hooks on `text_model.layers[i].input_layernorm` (i ∈ [3,7,11,15])
  - 最后一层 hook 在 `text_model.norm`
- 训练 (`src/train_crm_k1.py`)
  - Phase 1 `--precompute`: SmolVLA + MultiScaleExtractor → cache `(multi_scale_obs, obs_features, vla_action, expert_action)`
  - Phase 2: 多损失训练 (L2 + direction + triplet + magnitude)

### π0.5 现状
- `pi05_wrapper.py` 存在：
  - `obs_features` shape `[1, 2048]`, range `[-12.82, 19.99]`
  - K-sample 输出 `[B, K, 50, 7]`，action_dim=7（同 SmolVLA）
  - `_fix_vision_tower_keys` 修复 437 个 key，但 **376 个 language_model/projector key 未修复**
- `evaluate.py` 内有 `obs_proj = nn.Linear(2048, 960)`（random init，无用）

---

## 2. 设计决策

### 决策 A：CRM obs_dim = 2048（采用）
- 不复用 SmolVLA CRM 权重
- 直接训一个 obs_dim=2048 的 MultiScaleCRM（架构相同，只改 obs_dim 参数）
- 优点：无信息损失；obs_dim 改变只影响 `layer_proj` 一层（960×192 → 2048×192）
- 缺点：需重新跑 precompute

### 决策 D：第一版只用 fallback 单 obs feature
- π0.5 backbone 是 PaliGemma (Gemma-based, 18-layer)，层索引与 SmolVLA (16-layer LLaMA) 不同
- 避免对 π0.5 内部结构的依赖，便于调试
- SmolVLA 上 multi-scale vs single 提升约 +1pp，幅度有限
- 若效果不够好再增量加 multi-scale

### 决策 E/F：沿用 H_EFF=5, CORRECTION_DIM=6
- 与 SmolVLA 对齐，便于横向比较
- CRM 只修前 5 步 pose，不修 gripper

---

## 3. 需要修改/新增的文件清单

| 文件 | 修改类型 | 说明 |
|------|---------|------|
| `src/pi05_wrapper.py` | **修复 + 新增 API** | (1) 追加 376 key remap（language_model + multi_modal_projector）；(2) 增加 `preprocess_obs_batch`（批量预处理） |
| `src/precompute_pi05.py` 或改 `src/train_crm_k1.py` | **新建/改造** | 复制 precompute 逻辑，用 `Pi05Wrapper`，不挂 multi_scale hooks，只保存 `obs_features (2048,)` + `vla_action (5, 6)` + `expert_action (5, 6)` |
| `src/crm_k1_model.py` | **零修改** | 已支持 `obs_dim` 参数；fallback 单 obs 路径直接可用 |
| `src/train_crm_k1.py` | **小改** | (1) `--vla_backbone` 参数 (`smolvla`/`pi05`)；(2) `--obs_dim` 按 backbone 切默认值；(3) cache 路径加 `_pi05` 后缀 |
| `src/evaluate.py` | **小改** | (1) 删除 `obs_proj = nn.Linear(2048, 960)`；(2) CRM `obs_dim` 跟随 backbone；(3) 加 `--crm_ckpt` 参数 |
| `src/utils.py` | **小改** | 增加 `PI05_OBS_DIM=2048` 常量 |

---

## 4. 执行步骤和命令模板

### Step 0：修复 376 key remap（阻塞性，必须先完成）

需要在 `pi05_wrapper.py` 的 `_fix_vision_tower_keys` 中，追加 language_model 和 multi_modal_projector 的 key mapping。参考 lerobot 官方 patched 版的 `_fix_pytorch_state_dict_keys` 实现。

验证命令：
```bash
ssh connect.bjb2.seetacloud.com
cd /root/acr-vla-conformal-refinement
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
python -c "
import torch
from pi05_wrapper import Pi05Wrapper
w = Pi05Wrapper('/root/autodl-tmp/models/pi05_libero_finetuned/')
# 检查 missing keys = 0
print('Missing keys should be 0')
# 检查 language model 权重非随机
lm = w.policy.model.paligemma_with_expert.paligemma.model.language_model
ws = [p for n,p in lm.named_parameters() if 'weight' in n][:5]
for i,p in enumerate(ws):
    print(f'LM weight {i}: mean_abs={p.abs().mean().item():.4f}, std={p.std().item():.4f}')
"
```
**Go 条件**：missing_keys=0，LM weight mean_abs > 0.01

### Step 0b：Quick Verify（修复后立即做）
```bash
CUDA_VISIBLE_DEVICES=0 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 TORCH_COMPILE_DISABLE=1 \
python src/evaluate.py \
  --benchmark object --mode vla_only --baseline_mode single \
  --model pi05 --pi05_path /root/autodl-tmp/models/pi05_libero_finetuned/ \
  --seed 42 --n_rollouts 5 --K 1 --max_tasks 2
```
**Go 条件**：至少 1 个 task SR > 0%

### Step 1：重跑 Baseline Eval（6 experiments, ~8h）
```bash
# 模板（每个 GPU 一个实验）
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && \
CUDA_VISIBLE_DEVICES={GPU} HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 TORCH_COMPILE_DISABLE=1 \
nohup python src/evaluate.py \
  --benchmark {object|spatial} --mode vla_only --baseline_mode single \
  --model pi05 --pi05_path /root/autodl-tmp/models/pi05_libero_finetuned/ \
  --seed {42|43|44} --n_rollouts 10 --K 1 \
  > logs/eval_pi05_{benchmark}_seed{seed}.log 2>&1 &
```
需要 6 GPU 并行，或分批串行。

### Step 2：Precompute π0.5 features（K=1, per benchmark）
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && \
CUDA_VISIBLE_DEVICES=0 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 \
nohup python src/train_crm_k1.py --precompute \
  --vla_backbone pi05 \
  --pi05_path /root/autodl-tmp/models/pi05_libero_finetuned/ \
  --benchmark object spatial \
  --cache_dir /root/autodl-tmp/crm_cache_k1_pi05/ \
  --precompute_batch_size 2 \
  > logs/precompute_pi05_k1.log 2>&1 &
```
注意：π0.5 约 16GB VRAM，`precompute_batch_size=2`；OOM 则降到 1。

### Step 3：训练 π0.5 CRM（~30-40 min）
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && \
CUDA_VISIBLE_DEVICES=0 \
nohup python src/train_crm_k1.py \
  --vla_backbone pi05 \
  --obs_dim 2048 \
  --benchmark object spatial \
  --cache_dir /root/autodl-tmp/crm_cache_k1_pi05/ \
  --output_dir /root/autodl-tmp/checkpoints/crm_k1_pi05/ \
  --epochs 50 --batch_size 512 --lr 1e-3 \
  --hidden_dim 256 --bottleneck_dim 192 \
  --max_correction_norm 1.42 \
  --loss_mode multi \
  > logs/train_crm_pi05.log 2>&1 &
```
训练时是 fallback 单 obs 路径（`multi_scale_obs` dim==1）。CRM 参数量约 ~580K（vs SmolVLA CRM ~323K，差异来自 `layer_proj` 从 960×192 变为 2048×192）。

### Step 4：CRM + π0.5 Eval（6 experiments: 3 seeds × Object + Spatial）
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && \
CUDA_VISIBLE_DEVICES={GPU} HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 TORCH_COMPILE_DISABLE=1 \
nohup python src/evaluate.py \
  --benchmark {object|spatial} --mode crm_obs_only \
  --model pi05 --pi05_path /root/autodl-tmp/models/pi05_libero_finetuned/ \
  --crm_ckpt /root/autodl-tmp/checkpoints/crm_k1_pi05/crm_k1_best.pt \
  --crm_obs_dim 2048 \
  --seed {42|43|44} --n_rollouts 10 --K 10 \
  > logs/eval_pi05_crm_{benchmark}_seed{seed}.log 2>&1 &
```

---

## 5. GPU 时间预估

| 阶段 | 单次耗时 | GPU 数 |
|------|---------|--------|
| Step 0: Key remap fix + verify | ~1h (代码 + 测试) | 1 GPU |
| Step 1: Baseline eval (6 exps) | ~6-8h wallclock | 6 GPU 并行 |
| Step 2: Precompute Object + Spatial | ~2h total | 1 GPU |
| Step 3: CRM train 50 epochs | ~30-40 min | 1 GPU |
| Step 4: CRM eval (6 exps) | ~6-8h wallclock | 6 GPU 并行 |
| **总计 wallclock（串行）** | **~17-20h** | **峰值 6 GPU** |
| **总计 wallclock（Step 1 & 2 并行）** | **~10-12h** | **峰值 6 GPU** |

---

## 6. 风险点和缓解

| 风险 | 严重性 | 缓解 |
|------|--------|------|
| **376 key remap 不完整** | **致命** | 对照 lerobot patched 版本逐一核对 key name mapping；load 后验证 missing_keys=0 |
| **Gripper 恒 0.98** | **致命** | 可能随 key fix 一并解决（language model 随机→action token 无意义）。若 fix 后仍然 0.98，需审查 action denormalization |
| **torch.compile 兼容性** | 高 | 所有命令加 `TORCH_COMPILE_DISABLE=1`；lerobot native API 有 `aten.addmm.default` 冲突 |
| **π0.5 obs_features 分布偏移** | 中 | range `[-12.82, 19.99]` 比 SmolVLA 大。precompute 时计算 mean/std 写入 CRM normalization buffer |
| **precompute_batch_size OOM** | 中 | 从 batch=2 起步，OOM 降到 1 |
| **max_correction_norm 适配** | 中 | 训练后查看 delta norm 分布；若 saturated 调大，若 sparse 调小 |
| **lerobot 包被覆盖** | 中 | Spatial 实验死因疑似 pip reinstall lerobot。锁定 lerobot 版本：`pip install lerobot==0.5.2 --no-deps` |
| **Step 2/3 在 baseline 完成前可并行** | 低 | Precompute 不依赖 eval 结果（用 demo data），可提前跑；但需确认 key fix 已生效 |

---

## 7. Go/No-Go 判定

| 阶段 | Go 条件 |
|------|---------|
| Step 0 → Step 0b | missing_keys=0；LM weight 非随机 |
| Step 0b → Step 1 | 至少 1 个 task SR > 0% |
| Step 1 → Step 2 | baseline 至少 Object mean SR > 30%（π0.5 3.6B 应强于 SmolVLA 0.4B 的 ~60%，但留容忍度） |
| Step 2 → Step 3 | precompute 完成，manifest 写入，n_samples 合理（spatial ~12k, object ~14k） |
| Step 3 → Step 4 | val_loss 收敛，无 NaN，best val_loss 显著低于初始 |
| Step 4 验证 | 至少 1 个 seed Object SR ≥ baseline SR + 3pp |

---

## 8. 不做的事

- 不复用 SmolVLA CRM 权重
- 不引入 π0.5 multi-scale extraction（第一版）
- 不修改现有 SmolVLA pipeline 任何文件
- 不在 baseline 验证通过前启动 precompute/CRM 训练
- 不在 pi05 CRM eval 完成前启动 adaptive K 实验
