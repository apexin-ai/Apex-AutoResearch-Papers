# research d088 code survey

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_d088-code-survey_20260520T161513_result.json`
- **Structured JSON:** [`40c3ca0844e94afbdec6.json`](../../sessions/40/40c3ca0844e94afbdec6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已收集所有必要信息。

## VLA 特征提取

- **模型类**: `SmolVLAWrapper`（`src/smolvla_wrapper.py`）
- **加载方式**: `SmolVLAPolicy.from_pretrained(pretrained_path)` → frozen, eval mode
- **obs_features 获取方式**: `encode_prefix()` 方法直接返回，无需 hook
  - VLM forward pass → hidden states → mean pooling → 960D
  - `self.vlm_hidden_size = self.flow.vlm_with_expert.config.text_config.hidden_size  # 960`
- **obs_features 维度**: **(B, 960)** float32
- **调用链**: `preprocess_obs()` → `encode_prefix(imgs, img_masks, lt, lm, state)` → 返回 `(obs_feat, kv_cache, pad_masks)`
- **端到端接口**: `get_obs_features_and_samples()` 直接返回 `(obs_feat, samples)`，evaluate.py 中所有 mode 都通过这个接口获取

## evaluate.py mode 系统

**现有 modes** (`--mode` choices):

| Mode | 函数 | unc_dim | 逻辑 |
|------|------|---------|------|
| `vla_only` | `select_action_vla_only` | N/A | mean of K samples, no CRM |
| `crm_scalar` | `select_action_crm` | 3 | CRM + scalar uncertainty |
| `crm_perdof` | `select_action_crm` | 40 | CRM + full per-DOF CGS |
| `acr_vla` | `select_action_crm` | 40 | alias for crm_perdof |
| `crm_obs_only` | `select_action_crm` | 0 | CRM + obs_features only, uf=None |
| `reconvla` | `select_action_reconvla` | N/A | scalar Euclidean argmin |
| `random_selection` | `select_action_random` | N/A | random K pick |
| `adaptive_k` | `select_action_adaptive_k` | 0 | K=2 L2 probe → conditional K=10 + CRM obs_only |

**新增 `adaptive_unc_head` mode 需要改的地方**:
1. `parse_args()`: 在 `--mode` choices 加 `"adaptive_unc_head"`
2. `evaluate()` L~400: `unc_dim` 分支加新 mode 的处理
3. 新建 `select_action_unc_head()` 函数
4. `evaluate()` 的 rollout 分发逻辑（L~460 的 if/elif chain）加分支
5. 新增 UncertaintyHead 模型加载逻辑（checkpoint 路径参数）

## CRM 接口

- **输入**: `base_action (B, 30)` + `uncertainty_features (B, 40 | None)` + `obs_features (B, 960)`
- **forward 签名**: `crm(base_action, uf_input, obs_feat) → refined_action (B, 30)`
- **架构**: 2 hidden layers, dim 256, ReLU, residual (output = base + clipped_delta)
- **K=1 时 CRM 用法** (crm_obs_only): `uf_input=None`，CRM 只看 `base_action + obs_features`，input_dim = 30 + 960 = 990
- **GatedCRM** (`src/gated_crm.py`): 扩展版，额外按 per-DOF std 做 hard/soft gating

## Precompute 数据

- **路径**: `/root/autodl-tmp/crm_cache/spatial/`（object/ 目录为空）
- **格式**: `.pt` torch tensors
- **字段和维度**:

| 文件 | Shape | 含义 |
|------|-------|------|
| `obs_features.pt` | (2402, 960) float32 | VLM hidden states per timestep |
| `k_samples.pt` | (2402, 10, 5, 6) float32 | K=10 samples, H_eff=5, 6D pose |
| `expert_actions.pt` | (2402, 5, 6) float32 | ground truth expert actions |

- **数据量**: 2402 个 (obs, K_samples, expert) triplets（spatial benchmark）
- **partial 文件**: 分片缓存 (500 samples/shard)，最终合并为上述三个文件
- **Checkpoints**: `/root/autodl-tmp/checkpoints/crm_v3/` 下有 `obs_only/`, `perdof/`, `scalar_unc/`, `norm_stats.pt`

## 实现建议

- **UncertaintyHead 输入维度**: 960（obs_features）
- **训练数据提取方案**: 从 `crm_cache/spatial/` 已有数据直接提取
  - 输入: `obs_features.pt` → (2402, 960)
  - 目标 (action variance): 从 `k_samples.pt` (2402, 10, 5, 6) 计算
    - 方案 A: per-sample L2 pairwise disagreement → scalar target
    - 方案 B: per-DOF std across K=10 → (2402, 30) target（与 CGS 的 per_dof_stds 对齐）
    - 方案 C: flatten 后全局 std → scalar target
  - 不需要重新跑 VLA forward pass，数据已缓存
- **新增 mode 代码量**: ~50 行（新 select 函数 + evaluate 分发 + 模型加载），加上 UncertaintyHead 模型定义 ~30 行

---
