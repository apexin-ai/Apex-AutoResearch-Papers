# research pi05 crm pipeline prep 20260521T110149 retry2 — Part 2 of 2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Worker execution logs

[← Part 1](part-001.md) · [Transcript overview](../research-pi05-crm-pipeline-prep-20260521t110149-retry2.md) · [Structured JSON](../../../sessions/8e/8ef99e2587ded47e1fae.json)

## Round 3

### Assistant

_source line 309_

<details><summary>Logged reasoning block</summary>

```text
Now I have the full picture. Let me write the updated plan. The key issue is:

1. The existing plan (`pi05_crm_pipeline_plan.md`) was written on 2026-05-21 and is comprehensive
2. But since then, the baseline eval revealed a NEW blocking issue: not just vision tower keys (437 fixed), but also 376 language_model + multi_modal_projector keys are missing
3. The existing plan's Step 0 was supposed to catch this, but the reality is worse than anticipated

The plan needs to be updated to reflect:
- The actual blocking issue (language model keys, not just vision tower)


- That the official lerobot-eval patched version worked perfectly on all tests
- That my custom wrapper's key remapping is incomplete and needs fixing
- That the gripper is stuck at 0.98 and needs investigation

I should overwrite the existing file since the task asks me to write to that exact path.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0b83dcf7-139e-42b0-bcd9-687872ddb233",
  "uuid": "ac2d4310-2913-4789-bd94-9eae646410e4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RMg2QujfDonrMNT8nTrZao",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1274,
      "cache_read_input_tokens": 58359,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1274
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Assistant

_source line 310_

Now writing the updated plan that reflects the actual current state.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0b83dcf7-139e-42b0-bcd9-687872ddb233",
  "uuid": "6d311cfe-b626-4946-a3d9-4c1c56db7d89",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RMg2QujfDonrMNT8nTrZao",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1274,
      "cache_read_input_tokens": 58359,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1274
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 311_

<details open><summary>🔧 Tool call — Write · `toolu_01HWXSeukFphVnYXsYRWwLct`</summary>

````json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/pi05_crm_pipeline_plan.md",
  "content": "# π0.5 CRM Pipeline 方案 (2026-05-21, updated)\n\n## 0. 当前阻塞状态\n\n### Baseline Eval 全线 0% SR\n\n6 个 baseline 实验（3 seeds × Object + Spatial）全部失败：\n\n| 实验 | SR | 状态 |\n|------|-----|------|\n| Object seed42/43/44 | 0.0% (0/200 each) | 完成，EXIT_CODE=0 |\n| Spatial seed42/43/44 | 0.0% (前 8 task) | 中途死亡（task 9, rollout 10/20） |\n\n**根因进化**：不再是之前的 vision tower 单一问题，而是**双重 key mismatch**：\n- Vision tower: 437 keys 已成功 remap (`vision_tower.vision_model.` → `vision_tower.`) ✅\n- Language model + multi_modal_projector: **376 keys 仍 missing** ❌\n  - `model.paligemma_with_expert.paligemma.model.language_model.*`\n  - `model.paligemma_with_expert.paligemma.model.multi_modal_projector.*`\n- 结果：vision tower 有真实权重，但 **language model 在随机权重下运行** → 0% SR\n- 附加症状：gripper 恒定 ~0.98（始终 open），无法执行 pick\n\n**官方 lerobot-eval patched 版本 3/3 = 100% SR**，证明模型本身有效。\n\n### 阻塞解除条件\n在 `_fix_pytorch_state_dict_keys`（或 `pi05_wrapper.py` 的 `_fix_vision_tower_keys`）中追加 language_model + multi_modal_projector 的 key remap，使 load_state_dict missing_keys = 0。验证方式：至少 1 个 task SR > 0%。\n\n---\n\n## 1. 现状摘要\n\n### SmolVLA 现有 pipeline（LOCKED）\n- `SmolVLAWrapper` (`src/smolvla_wrapper.py`)\n  - `encode_prefix(...)` → `obs_features (B, 960)`, `kv_cache`, `prefix_pad_masks`\n  - `generate_k_samples(kv, masks, K)` → `(B, K, chunk_size=50, FULL_ACTION_DIM=7)`\n  - `preprocess_obs_batch` 已支持 batched precompute\n- `MultiScaleCRM` (`src/crm_k1_model.py`)\n  - 输入: `base_action (B, 30)` + `multi_scale_obs (B, 4, 960)` 或 fallback `(B, 960)`\n  - 参数: `action_dim=30`, `obs_dim=960`, `hidden_dim=256`, `bottleneck_dim=192`\n  - ~323K params\n- `MultiScaleFeatureExtractor`\n  - hooks on `text_model.layers[i].input_layernorm` (i ∈ [3,7,11,15])\n  - 最后一层 hook 在 `text_model.norm`\n- 训练 (`src/train_crm_k1.py`)\n  - Phase 1 `--precompute`: SmolVLA + MultiScaleExtractor → cache `(multi_scale_obs, obs_features, vla_action, expert_action)`\n  - Phase 2: 多损失训练 (L2 + direction + triplet + magnitude)\n\n### π0.5 现状\n- `pi05_wrapper.py` 存在：\n  - `obs_features` shape `[1, 2048]`, range `[-12.82, 19.99]`\n  - K-sample 输出 `[B, K, 50, 7]`，action_dim=7（同 SmolVLA）\n  - `_fix_vision_tower_keys` 修复 437 个 key，但 **376 个 language_model/projector key 未修复**\n- `evaluate.py` 内有 `obs_proj = nn.Linear(2048, 960)`（random init，无用）\n\n---\n\n## 2. 设计决策\n\n### 决策 A：CRM obs_dim = 2048（采用）\n- 不复用 SmolVLA CRM 权重\n- 直接训一个 obs_dim=2048 的 MultiScaleCRM（架构相同，只改 obs_dim 参数）\n- 优点：无信息损失；obs_dim 改变只影响 `layer_proj` 一层（960×192 → 2048×192）\n- 缺点：需重新跑 precompute\n\n### 决策 D：第一版只用 fallback 单 obs feature\n- π0.5 backbone 是 PaliGemma (Gemma-based, 18-layer)，层索引与 SmolVLA (16-layer LLaMA) 不同\n- 避免对 π0.5 内部结构的依赖，便于调试\n- SmolVLA 上 multi-scale vs single 提升约 +1pp，幅度有限\n- 若效果不够好再增量加 multi-scale\n\n### 决策 E/F：沿用 H_EFF=5, CORRECTION_DIM=6\n- 与 SmolVLA 对齐，便于横向比较\n- CRM 只修前 5 步 pose，不修 gripper\n\n---\n\n## 3. 需要修改/新增的文件清单\n\n| 文件 | 修改类型 | 说明 |\n|------|---------|------|\n| `src/pi05_wrapper.py` | **修复 + 新增 API** | (1) 追加 376 key remap（language_model + multi_modal_projector）；(2) 增加 `preprocess_obs_batch`（批量预处理） |\n| `src/precompute_pi05.py` 或改 `src/train_crm_k1.py` | **新建/改造** | 复制 precompute 逻辑，用 `Pi05Wrapper`，不挂 multi_scale hooks，只保存 `obs_features (2048,)` + `vla_action (5, 6)` + `expert_action (5, 6)` |\n| `src/crm_k1_model.py` | **零修改** | 已支持 `obs_dim` 参数；fallback 单 obs 路径直接可用 |\n| `src/train_crm_k1.py` | **小改** | (1) `--vla_backbone` 参数 (`smolvla`/`pi05`)；(2) `--obs_dim` 按 backbone 切默认值；(3) cache 路径加 `_pi05` 后缀 |\n| `src/evaluate.py` | **小改** | (1) 删除 `obs_proj = nn.Linear(2048, 960)`；(2) CRM `obs_dim` 跟随 backbone；(3) 加 `--crm_ckpt` 参数 |\n| `src/utils.py` | **小改** | 增加 `PI05_OBS_DIM=2048` 常量 |\n\n---\n\n## 4. 执行步骤和命令模板\n\n### Step 0：修复 376 key remap（阻塞性，必须先完成）\n\n需要在 `pi05_wrapper.py` 的 `_fix_vision_tower_keys` 中，追加 language_model 和 multi_modal_projector 的 key mapping。参考 lerobot 官方 patched 版的 `_fix_pytorch_state_dict_keys` 实现。\n\n验证命令：\n```bash\nssh connect.bjb2.seetacloud.com\ncd /root/acr-vla-conformal-refinement\nsource /root/miniconda3/etc/profile.d/conda.sh && conda activate base\npython -c \"\nimport torch\nfrom pi05_wrapper import Pi05Wrapper\nw = Pi05Wrapper('/root/autodl-tmp/models/pi05_libero_finetuned/')\n# 检查 missing keys = 0\nprint('Missing keys should be 0')\n# 检查 language model 权重非随机\nlm = w.policy.model.paligemma_with_expert.paligemma.model.language_model\nws = [p for n,p in lm.named_parameters() if 'weight' in n][:5]\nfor i,p in enumerate(ws):\n    print(f'LM weight {i}: mean_abs={p.abs().mean().item():.4f}, std={p.std().item():.4f}')\n\"\n```\n**Go 条件**：missing_keys=0，LM weight mean_abs > 0.01\n\n### Step 0b：Quick Verify（修复后立即做）\n```bash\nCUDA_VISIBLE_DEVICES=0 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 TORCH_COMPILE_DISABLE=1 \\\npython src/evaluate.py \\\n  --benchmark object --mode vla_only --baseline_mode single \\\n  --model pi05 --pi05_path /root/autodl-tmp/models/pi05_libero_finetuned/ \\\n  --seed 42 --n_rollouts 5 --K 1 --max_tasks 2\n```\n**Go 条件**：至少 1 个 task SR > 0%\n\n### Step 1：重跑 Baseline Eval（6 experiments, ~8h）\n```bash\n# 模板（每个 GPU 一个实验）\nsource /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && \\\nCUDA_VISIBLE_DEVICES={GPU} HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 TORCH_COMPILE_DISABLE=1 \\\nnohup python src/evaluate.py \\\n  --benchmark {object|spatial} --mode vla_only --baseline_mode single \\\n  --model pi05 --pi05_path /root/autodl-tmp/models/pi05_libero_finetuned/ \\\n  --seed {42|43|44} --n_rollouts 10 --K 1 \\\n  > logs/eval_pi05_{benchmark}_seed{seed}.log 2>&1 &\n```\n需要 6 GPU 并行，或分批串行。\n\n### Step 2：Precompute π0.5 features（K=1, per benchmark）\n```bash\nsource /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && \\\nCUDA_VISIBLE_DEVICES=0 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 \\\nnohup python src/train_crm_k1.py --precompute \\\n  --vla_backbone pi05 \\\n  --pi05_path /root/autodl-tmp/models/pi05_libero_finetuned/ \\\n  --benchmark object spatial \\\n  --cache_dir /root/autodl-tmp/crm_cache_k1_pi05/ \\\n  --precompute_batch_size 2 \\\n  > logs/precompute_pi05_k1.log 2>&1 &\n```\n注意：π0.5 约 16GB VRAM，`precompute_batch_size=2`；OOM 则降到 1。\n\n### Step 3：训练 π0.5 CRM（~30-40 min）\n```bash\nsource /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && \\\nCUDA_VISIBLE_DEVICES=0 \\\nnohup python src/train_crm_k1.py \\\n  --vla_backbone pi05 \\\n  --obs_dim 2048 \\\n  --benchmark object spatial \\\n  --cache_dir /root/autodl-tmp/crm_cache_k1_pi05/ \\\n  --output_dir /root/autodl-tmp/checkpoints/crm_k1_pi05/ \\\n  --epochs 50 --batch_size 512 --lr 1e-3 \\\n  --hidden_dim 256 --bottleneck_dim 192 \\\n  --max_correction_norm 1.42 \\\n  --loss_mode multi \\\n  > logs/train_crm_pi05.log 2>&1 &\n```\n训练时是 fallback 单 obs 路径（`multi_scale_obs` dim==1）。CRM 参数量约 ~580K（vs SmolVLA CRM ~323K，差异来自 `layer_proj` 从 960×192 变为 2048×192）。\n\n### Step 4：CRM + π0.5 Eval（6 experiments: 3 seeds × Object + Spatial）\n```bash\nsource /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && \\\nCUDA_VISIBLE_DEVICES={GPU} HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 TORCH_COMPILE_DISABLE=1 \\\nnohup python src/evaluate.py \\\n  --benchmark {object|spatial} --mode crm_obs_only \\\n  --model pi05 --pi05_path /root/autodl-tmp/models/pi05_libero_finetuned/ \\\n  --crm_ckpt /root/autodl-tmp/checkpoints/crm_k1_pi05/crm_k1_best.pt \\\n  --crm_obs_dim 2048 \\\n  --seed {42|43|44} --n_rollouts 10 --K 10 \\\n  > logs/eval_pi05_crm_{benchmark}_seed{seed}.log 2>&1 &\n```\n\n---\n\n## 5. GPU 时间预估\n\n| 阶段 | 单次耗时 | GPU 数 |\n|------|---------|--------|\n| Step 0: Key remap fix + verify | ~1h (代码 + 测试) | 1 GPU |\n| Step 1: Baseline eval (6 exps) | ~6-8h wallclock | 6 GPU 并行 |\n| Step 2: Precompute Object + Spatial | ~2h total | 1 GPU |\n| Step 3: CRM train 50 epochs | ~30-40 min | 1 GPU |\n| Step 4: CRM eval (6 exps) | ~6-8h wallclock | 6 GPU 并行 |\n| **总计 wallclock（串行）** | **~17-20h** | **峰值 6 GPU** |\n| **总计 wallclock（Step 1 & 2 并行）** | **~10-12h** | **峰值 6 GPU** |\n\n---\n\n## 6. 风险点和缓解\n\n| 风险 | 严重性 | 缓解 |\n|------|--------|------|\n| **376 key remap 不完整** | **致命** | 对照 lerobot patched 版本逐一核对 key name mapping；load 后验证 missing_keys=0 |\n| **Gripper 恒 0.98** | **致命** | 可能随 key fix 一并解决（language model 随机→action token 无意义）。若 fix 后仍然 0.98，需审查 action denormalization |\n| **torch.compile 兼容性** | 高 | 所有命令加 `TORCH_COMPILE_DISABLE=1`；lerobot native API 有 `aten.addmm.default` 冲突 |\n| **π0.5 obs_features 分布偏移** | 中 | range `[-12.82, 19.99]` 比 SmolVLA 大。precompute 时计算 mean/std 写入 CRM normalization buffer |\n| **precompute_batch_size OOM** | 中 | 从 batch=2 起步，OOM 降到 1 |\n| **max_correction_norm 适配** | 中 | 训练后查看 delta norm 分布；若 saturated 调大，若 sparse 调小 |\n| **lerobot 包被覆盖** | 中 | Spatial 实验死因疑似 pip reinstall lerobot。锁定 lerobot 版本：`pip install lerobot==0.5.2 --no-deps` |\n| **Step 2/3 在 baseline 完成前可并行** | 低 | Precompute 不依赖 eval 结果（用 demo data），可提前跑；但需确认 key fix 已生效 |\n\n---\n\n## 7. Go/No-Go 判定\n\n| 阶段 | Go 条件 |\n|------|---------|\n| Step 0 → Step 0b | missing_keys=0；LM weight 非随机 |\n| Step 0b → Step 1 | 至少 1 个 task SR > 0% |\n| Step 1 → Step 2 | baseline 至少 Object mean SR > 30%（π0.5 3.6B 应强于 SmolVLA 0.4B 的 ~60%，但留容忍度） |\n| Step 2 → Step 3 | precompute 完成，manifest 写入，n_samples 合理（spatial ~12k, object ~14k） |\n| Step 3 → Step 4 | val_loss 收敛，无 NaN，best val_loss 显著低于初始 |\n| Step 4 验证 | 至少 1 个 seed Object SR ≥ baseline SR + 3pp |\n\n---\n\n## 8. 不做的事\n\n- 不复用 SmolVLA CRM 权重\n- 不引入 π0.5 multi-scale extraction（第一版）\n- 不修改现有 SmolVLA pipeline 任何文件\n- 不在 baseline 验证通过前启动 precompute/CRM 训练\n- 不在 pi05 CRM eval 完成前启动 adaptive K 实验\n"
}
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0b83dcf7-139e-42b0-bcd9-687872ddb233",
  "uuid": "69947c65-2096-42ea-9369-d71034540047",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RMg2QujfDonrMNT8nTrZao",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1274,
      "cache_read_input_tokens": 58359,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1274
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 312 · 2026-05-21T11:13:24.130Z_

<details><summary>↩ Tool result · `toolu_01HWXSeukFphVnYXsYRWwLct`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/pi05_crm_pipeline_plan.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0b83dcf7-139e-42b0-bcd9-687872ddb233",
  "uuid": "79dd88f7-8345-4720-88b3-742fe2fccc0d",
  "tool_use_result": {
    "type": "update",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/pi05_crm_pipeline_plan.md",
    "content": "# π0.5 CRM Pipeline 方案 (2026-05-21, updated)\n\n## 0. 当前阻塞状态\n\n### Baseline Eval 全线 0% SR\n\n6 个 baseline 实验（3 seeds × Object + Spatial）全部失败：\n\n| 实验 | SR | 状态 |\n|------|-----|------|\n| Object seed42/43/44 | 0.0% (0/200 each) | 完成，EXIT_CODE=0 |\n| Spatial seed42/43/44 | 0.0% (前 8 task) | 中途死亡（task 9, rollout 10/20） |\n\n**根因进化**：不再是之前的 vision tower 单一问题，而是**双重 key mismatch**：\n- Vision tower: 437 keys 已成功 remap (`vision_tower.vision_model.` → `vision_tower.`) ✅\n- Language model + multi_modal_projector: **376 keys 仍 missing** ❌\n  - `model.paligemma_with_expert.paligemma.model.language_model.*`\n  - `model.paligemma_with_expert.paligemma.model.multi_modal_projector.*`\n- 结果：vision tower 有真实权重，但 **language model 在随机权重下运行** → 0% SR\n- 附加症状：gripper 恒定 ~0.98（始终 open），无法执行 pick\n\n**官方 lerobot-eval patched 版本 3/3 = 100% SR**，证明模型本身有效。\n\n### 阻塞解除条件\n在 `_fix_pytorch_state_dict_keys`（或 `pi05_wrapper.py` 的 `_fix_vision_tower_keys`）中追加 language_model + multi_modal_projector 的 key remap，使 load_state_dict missing_keys = 0。验证方式：至少 1 个 task SR > 0%。\n\n---\n\n## 1. 现状摘要\n\n### SmolVLA 现有 pipeline（LOCKED）\n- `SmolVLAWrapper` (`src/smolvla_wrapper.py`)\n  - `encode_prefix(...)` → `obs_features (B, 960)`, `kv_cache`, `prefix_pad_masks`\n  - `generate_k_samples(kv, masks, K)` → `(B, K, chunk_size=50, FULL_ACTION_DIM=7)`\n  - `preprocess_obs_batch` 已支持 batched precompute\n- `MultiScaleCRM` (`src/crm_k1_model.py`)\n  - 输入: `base_action (B, 30)` + `multi_scale_obs (B, 4, 960)` 或 fallback `(B, 960)`\n  - 参数: `action_dim=30`, `obs_dim=960`, `hidden_dim=256`, `bottleneck_dim=192`\n  - ~323K params\n- `MultiScaleFeatureExtractor`\n  - hooks on `text_model.layers[i].input_layernorm` (i ∈ [3,7,11,15])\n  - 最后一层 hook 在 `text_model.norm`\n- 训练 (`src/train_crm_k1.py`)\n  - Phase 1 `--precompute`: SmolVLA + MultiScaleExtractor → cache `(multi_scale_obs, obs_features, vla_action, expert_action)`\n  - Phase 2: 多损失训练 (L2 + direction + triplet + magnitude)\n\n### π0.5 现状\n- `pi05_wrapper.py` 存在：\n  - `obs_features` shape `[1, 2048]`, range `[-12.82, 19.99]`\n  - K-sample 输出 `[B, K, 50, 7]`，action_dim=7（同 SmolVLA）\n  - `_fix_vision_tower_keys` 修复 437 个 key，但 **376 个 language_model/projector key 未修复**\n- `evaluate.py` 内有 `obs_proj = nn.Linear(2048, 960)`（random init，无用）\n\n---\n\n## 2. 设计决策\n\n### 决策 A：CRM obs_dim = 2048（采用）\n- 不复用 SmolVLA CRM 权重\n- 直接训一个 obs_dim=2048 的 MultiScaleCRM（架构相同，只改 obs_dim 参数）\n- 优点：无信息损失；obs_dim 改变只影响 `layer_proj` 一层（960×192 → 2048×192）\n- 缺点：需重新跑 precompute\n\n### 决策 D：第一版只用 fallback 单 obs feature\n- π0.5 backbone 是 PaliGemma (Gemma-based, 18-layer)，层索引与 SmolVLA (16-layer LLaMA) 不同\n- 避免对 π0.5 内部结构的依赖，便于调试\n- SmolVLA 上 multi-scale vs single 提升约 +1pp，幅度有限\n- 若效果不够好再增量加 multi-scale\n\n### 决策 E/F：沿用 H_EFF=5, CORRECTION_DIM=6\n- 与 SmolVLA 对齐，便于横向比较\n- CRM 只修前 5 步 pose，不修 gripper\n\n---\n\n## 3. 需要修改/新增的文件清单\n\n| 文件 | 修改类型 | 说明 |\n|------|---------|------|\n| `src/pi05_wrapper.py` | **修复 + 新增 API** | (1) 追加 376 key remap（language_model + multi_modal_projector）；(2) 增加 `preprocess_obs_batch`（批量预处理） |\n| `src/precompute_pi05.py` 或改 `src/train_crm_k1.py` | **新建/改造** | 复制 precompute 逻辑，用 `Pi05Wrapper`，不挂 multi_scale hooks，只保存 `obs_features (2048,)` + `vla_action (5, 6)` + `expert_action (5, 6)` |\n| `src/crm_k1_model.py` | **零修改** | 已支持 `obs_dim` 参数；fallback 单 obs 路径直接可用 |\n| `src/train_crm_k1.py` | **小改** | (1) `--vla_backbone` 参数 (`smolvla`/`pi05`)；(2) `--obs_dim` 按 backbone 切默认值；(3) cache 路径加 `_pi05` 后缀 |\n| `src/evaluate.py` | **小改** | (1) 删除 `obs_proj = nn.Linear(2048, 960)`；(2) CRM `obs_dim` 跟随 backbone；(3) 加 `--crm_ckpt` 参数 |\n| `src/utils.py` | **小改** | 增加 `PI05_OBS_DIM=2048` 常量 |\n\n---\n\n## 4. 执行步骤和命令模板\n\n### Step 0：修复 376 key remap（阻塞性，必须先完成）\n\n需要在 `pi05_wrapper.py` 的 `_fix_vision_tower_keys` 中，追加 language_model 和 multi_modal_projector 的 key mapping。参考 lerobot 官方 patched 版的 `_fix_pytorch_state_dict_keys` 实现。\n\n验证命令：\n```bash\nssh connect.bjb2.seetacloud.com\ncd /root/acr-vla-conformal-refinement\nsource /root/miniconda3/etc/profile.d/conda.sh && conda activate base\npython -c \"\nimport torch\nfrom pi05_wrapper import Pi05Wrapper\nw = Pi05Wrapper('/root/autodl-tmp/models/pi05_libero_finetuned/')\n# 检查 missing keys = 0\nprint('Missing keys should be 0')\n# 检查 language model 权重非随机\nlm = w.policy.model.paligemma_with_expert.paligemma.model.language_model\nws = [p for n,p in lm.named_parameters() if 'weight' in n][:5]\nfor i,p in enumerate(ws):\n    print(f'LM weight {i}: mean_abs={p.abs().mean().item():.4f}, std={p.std().item():.4f}')\n\"\n```\n**Go 条件**：missing_keys=0，LM weight mean_abs > 0.01\n\n### Step 0b：Quick Verify（修复后立即做）\n```bash\nCUDA_VISIBLE_DEVICES=0 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 TORCH_COMPILE_DISABLE=1 \\\npython src/evaluate.py \\\n  --benchmark object --mode vla_only --baseline_mode single \\\n  --model pi05 --pi05_path /root/autodl-tmp/models/pi05_libero_finetuned/ \\\n  --seed 42 --n_rollouts 5 --K 1 --max_tasks 2\n```\n**Go 条件**：至少 1 个 task SR > 0%\n\n### Step 1：重跑 Baseline Eval（6 experiments, ~8h）\n```bash\n# 模板（每个 GPU 一个实验）\nsource /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && \\\nCUDA_VISIBLE_DEVICES={GPU} HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 TORCH_COMPILE_DISABLE=1 \\\nnohup python src/evaluate.py \\\n  --benchmark {object|spatial} --mode vla_only --baseline_mode single \\\n  --model pi05 --pi05_path /root/autodl-tmp/models/pi05_libero_finetuned/ \\\n  --seed {42|43|44} --n_rollouts 10 --K 1 \\\n  > logs/eval_pi05_{benchmark}_seed{seed}.log 2>&1 &\n```\n需要 6 GPU 并行，或分批串行。\n\n### Step 2：Precompute π0.5 features（K=1, per benchmark）\n```bash\nsource /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && \\\nCUDA_VISIBLE_DEVICES=0 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 \\\nnohup python src/train_crm_k1.py --precompute \\\n  --vla_backbone pi05 \\\n  --pi05_path /root/autodl-tmp/models/pi05_libero_finetuned/ \\\n  --benchmark object spatial \\\n  --cache_dir /root/autodl-tmp/crm_cache_k1_pi05/ \\\n  --precompute_batch_size 2 \\\n  > logs/precompute_pi05_k1.log 2>&1 &\n```\n注意：π0.5 约 16GB VRAM，`precompute_batch_size=2`；OOM 则降到 1。\n\n### Step 3：训练 π0.5 CRM（~30-40 min）\n```bash\nsource /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && \\\nCUDA_VISIBLE_DEVICES=0 \\\nnohup python src/train_crm_k1.py \\\n  --vla_backbone pi05 \\\n  --obs_dim 2048 \\\n  --benchmark object spatial \\\n  --cache_dir /root/autodl-tmp/crm_cache_k1_pi05/ \\\n  --output_dir /root/autodl-tmp/checkpoints/crm_k1_pi05/ \\\n  --epochs 50 --batch_size 512 --lr 1e-3 \\\n  --hidden_dim 256 --bottleneck_dim 192 \\\n  --max_correction_norm 1.42 \\\n  --loss_mode multi \\\n  > logs/train_crm_pi05.log 2>&1 &\n```\n训练时是 fallback 单 obs 路径（`multi_scale_obs` dim==1）。CRM 参数量约 ~580K（vs SmolVLA CRM ~323K，差异来自 `layer_proj` 从 960×192 变为 2048×192）。\n\n### Step 4：CRM + π0.5 Eval（6 experiments: 3 seeds × Object + Spatial）\n```bash\nsource /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && \\\nCUDA_VISIBLE_DEVICES={GPU} HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 TORCH_COMPILE_DISABLE=1 \\\nnohup python src/evaluate.py \\\n  --benchmark {object|spatial} --mode crm_obs_only \\\n  --model pi05 --pi05_path /root/autodl-tmp/models/pi05_libero_finetuned/ \\\n  --crm_ckpt /root/autodl-tmp/checkpoints/crm_k1_pi05/crm_k1_best.pt \\\n  --crm_obs_dim 2048 \\\n  --seed {42|43|44} --n_rollouts 10 --K 10 \\\n  > logs/eval_pi05_crm_{benchmark}_seed{seed}.log 2>&1 &\n```\n\n---\n\n## 5. GPU 时间预估\n\n| 阶段 | 单次耗时 | GPU 数 |\n|------|---------|--------|\n| Step 0: Key remap fix + verify | ~1h (代码 + 测试) | 1 GPU |\n| Step 1: Baseline eval (6 exps) | ~6-8h wallclock | 6 GPU 并行 |\n| Step 2: Precompute Object + Spatial | ~2h total | 1 GPU |\n| Step 3: CRM train 50 epochs | ~30-40 min | 1 GPU |\n| Step 4: CRM eval (6 exps) | ~6-8h wallclock | 6 GPU 并行 |\n| **总计 wallclock（串行）** | **~17-20h** | **峰值 6 GPU** |\n| **总计 wallclock（Step 1 & 2 并行）** | **~10-12h** | **峰值 6 GPU** |\n\n---\n\n## 6. 风险点和缓解\n\n| 风险 | 严重性 | 缓解 |\n|------|--------|------|\n| **376 key remap 不完整** | **致命** | 对照 lerobot patched 版本逐一核对 key name mapping；load 后验证 missing_keys=0 |\n| **Gripper 恒 0.98** | **致命** | 可能随 key fix 一并解决（language model 随机→action token 无意义）。若 fix 后仍然 0.98，需审查 action denormalization |\n| **torch.compile 兼容性** | 高 | 所有命令加 `TORCH_COMPILE_DISABLE=1`；lerobot native API 有 `aten.addmm.default` 冲突 |\n| **π0.5 obs_features 分布偏移** | 中 | range `[-12.82, 19.99]` 比 SmolVLA 大。precompute 时计算 mean/std 写入 CRM normalization buffer |\n| **precompute_batch_size OOM** | 中 | 从 batch=2 起步，OOM 降到 1 |\n| **max_correction_norm 适配** | 中 | 训练后查看 delta norm 分布；若 saturated 调大，若 sparse 调小 |\n| **lerobot 包被覆盖** | 中 | Spatial 实验死因疑似 pip reinstall lerobot。锁定 lerobot 版本：`pip install lerobot==0.5.2 --no-deps` |\n| **Step 2/3 在 baseline 完成前可并行** | 低 | Precompute 不依赖 eval 结果（用 demo data），可提前跑；但需确认 key fix 已生效 |\n\n---\n\n## 7. Go/No-Go 判定\n\n| 阶段 | Go 条件 |\n|------|---------|\n| Step 0 → Step 0b | missing_keys=0；LM weight 非随机 |\n| Step 0b → Step 1 | 至少 1 个 task SR > 0% |\n| Step 1 → Step 2 | baseline 至少 Object mean SR > 30%（π0.5 3.6B 应强于 SmolVLA 0.4B 的 ~60%，但留容忍度） |\n| Step 2 → Step 3 | precompute 完成，manifest 写入，n_samples 合理（spatial ~12k, object ~14k） |\n| Step 3 → Step 4 | val_loss 收敛，无 NaN，best val_loss 显著低于初始 |\n| Step 4 验证 | 至少 1 个 seed Object SR ≥ baseline SR + 3pp |\n\n---\n\n## 8. 不做的事\n\n- 不复用 SmolVLA CRM 权重\n- 不引入 π0.5 multi-scale extraction（第一版）\n- 不修改现有 SmolVLA pipeline 任何文件\n- 不在 baseline 验证通过前启动 precompute/CRM 训练\n- 不在 pi05 CRM eval 完成前启动 adaptive K 实验\n",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 5,
        "newStart": 1,
        "newLines": 31,
        "lines": [
          "-# π0.5 CRM Pipeline 方案 (2026-05-21)",
          "+# π0.5 CRM Pipeline 方案 (2026-05-21, updated)",
          " ",
          "+## 0. 当前阻塞状态",
          "+",
          "+### Baseline Eval 全线 0% SR",
          "+",
          "+6 个 baseline 实验（3 seeds × Object + Spatial）全部失败：",
          "+",
          "+| 实验 | SR | 状态 |",
          "+|------|-----|------|",
          "+| Object seed42/43/44 | 0.0% (0/200 each) | 完成，EXIT_CODE=0 |",
          "+| Spatial seed42/43/44 | 0.0% (前 8 task) | 中途死亡（task 9, rollout 10/20） |",
          "+",
          "+**根因进化**：不再是之前的 vision tower 单一问题，而是**双重 key mismatch**：",
          "+- Vision tower: 437 keys 已成功 remap (`vision_tower.vision_model.` → `vision_tower.`) ✅",
          "+- Language model + multi_modal_projector: **376 keys 仍 missing** ❌",
          "+  - `model.paligemma_with_expert.paligemma.model.language_model.*`",
          "+  - `model.paligemma_with_expert.paligemma.model.multi_modal_projector.*`",
          "+- 结果：vision tower 有真实权重，但 **language model 在随机权重下运行** → 0% SR",
          "+- 附加症状：gripper 恒定 ~0.98（始终 open），无法执行 pick",
          "+",
          "+**官方 lerobot-eval patched 版本 3/3 = 100% SR**，证明模型本身有效。",
          "+",
          "+### 阻塞解除条件",
          "+在 `_fix_pytorch_state_dict_keys`（或 `pi05_wrapper.py` 的 `_fix_vision_tower_keys`）中追加 language_model + multi_modal_projector 的 key remap，使 load_state_dict missing_keys = 0。验证方式：至少 1 个 task SR > 0%。",
          "+",
          "+---",
          "+",
          " ## 1. 现状摘要",
          " ",
          " ### SmolVLA 现有 pipeline（LOCKED）"
        ]
      },
      {
        "oldStart": 9,
        "oldLines": 98,
        "newStart": 35,
        "newLines": 109,
        "lines": [
          "   - `preprocess_obs_batch` 已支持 batched precompute",
          " - `MultiScaleCRM` (`src/crm_k1_model.py`)",
          "   - 输入: `base_action (B, 30)` + `multi_scale_obs (B, 4, 960)` 或 fallback `(B, 960)`",
          "-  - 参数: `action_dim=H_EFF*CORRECTION_DIM=30`, `obs_dim=960`, `hidden_dim=256`, `bottleneck_dim=192`",
          "-  - 支持多层 FiLM + action-conditioned attention，~323K params",
          "+  - 参数: `action_dim=30`, `obs_dim=960`, `hidden_dim=256`, `bottleneck_dim=192`",
          "+  - ~323K params",
          " - `MultiScaleFeatureExtractor`",
          "-  - hooks 注册在 `flow.vlm_with_expert.vlm.model.text_model.layers[i].input_layernorm` (i ∈ [3,7,11,15])",
          "+  - hooks on `text_model.layers[i].input_layernorm` (i ∈ [3,7,11,15])",
          "   - 最后一层 hook 在 `text_model.norm`",
          " - 训练 (`src/train_crm_k1.py`)",
          "-  - Phase 1 `--precompute`: 用 SmolVLA + MultiScaleExtractor 跑 LIBERO demo，cache `(multi_scale_obs, obs_features, vla_action, expert_action)` per sample",
          "-  - Phase 2: 加载 cache，多损失训练 (L2 + direction + triplet + magnitude)",
          "+  - Phase 1 `--precompute`: SmolVLA + MultiScaleExtractor → cache `(multi_scale_obs, obs_features, vla_action, expert_action)`",
          "+  - Phase 2: 多损失训练 (L2 + direction + triplet + magnitude)",
          " ",
          " ### π0.5 现状",
          "-- `pi05_wrapper.py` 已存在（diag log 确认）：",
          "+- `pi05_wrapper.py` 存在：",
          "   - `obs_features` shape `[1, 2048]`, range `[-12.82, 19.99]`",
          "-  - K-sample 输出 `[B, K, 50, 7]`，action_dim=7（同 SmolVLA：6D pose + 1D gripper）",
          "-  - `_fix_vision_tower_keys` 已修复 437 个 key mapping",
          "-- `evaluate.py` 内已注入 `obs_proj = nn.Linear(2048, 960)`，但**未训练（random init）**，等于丢掉所有信息",
          "-- 现 baseline eval 在跑（3 seeds × Object + Spatial 共 6 jobs）",
          "+  - K-sample 输出 `[B, K, 50, 7]`，action_dim=7（同 SmolVLA）",
          "+  - `_fix_vision_tower_keys` 修复 437 个 key，但 **376 个 language_model/projector key 未修复**",
          "+- `evaluate.py` 内有 `obs_proj = nn.Linear(2048, 960)`（random init，无用）",
          " ",
          "-### ⚠️ 阻塞性风险（必须先确认）",
          "-1. **Vision tower 权重静默加载失败 bug**：mem 记录此前 5 轮 fix 都是 0% SR，根因是 `load_state_dict` 被 try/except 吞掉。官方 lerobot-eval patched 后 3/3 success",
          "-2. **当前 baseline 状态**：进度报告显示 `eval-pi05-baseline-object-seed42` 在 bjb2-40593 上前 2 个 task 全 0% (0/40)。**需要先确认 vision tower fix 是否已生效于当前 eval 跑的代码路径**，否则后续 CRM 工作全部白做",
          "-3. **Gripper 恒为 0.98 bug**：diag log 显示所有 sample 的 gripper 值恒定 ~0.98，无法 pick。需确认是否随 vision tower fix 一并解决",
          "+---",
          " ",
          " ## 2. 设计决策",
          " ",
          "-### 决策 A：CRM obs_dim = 2048（推荐）",
          "+### 决策 A：CRM obs_dim = 2048（采用）",
          " - 不复用 SmolVLA CRM 权重",
          " - 直接训一个 obs_dim=2048 的 MultiScaleCRM（架构相同，只改 obs_dim 参数）",
          "-- 优点：无信息损失；CRM MLP 主要参数在 hidden_dim×hidden_dim，obs_dim 改变只影响 `layer_proj` 一层",
          "-- 缺点：需重新跑 precompute（约 2-3h/benchmark）",
          "+- 优点：无信息损失；obs_dim 改变只影响 `layer_proj` 一层（960×192 → 2048×192）",
          "+- 缺点：需重新跑 precompute",
          " ",
          "-### 决策 B：固定 Linear(2048→960) + 复用 SmolVLA CRM（不推荐）",
          "-- 用 SmolVLA 的 obs 统计量去 normalize 投影后的 960D 特征——分布不匹配",
          "-- 即便 projection 可学习，仍是 bottleneck，且复用 SmolVLA CRM 的语义假设不一定迁移",
          "+### 决策 D：第一版只用 fallback 单 obs feature",
          "+- π0.5 backbone 是 PaliGemma (Gemma-based, 18-layer)，层索引与 SmolVLA (16-layer LLaMA) 不同",
          "+- 避免对 π0.5 内部结构的依赖，便于调试",
          "+- SmolVLA 上 multi-scale vs single 提升约 +1pp，幅度有限",
          "+- 若效果不够好再增量加 multi-scale",
          " ",
          "-### 决策 C：Linear(2048→960) + 联合训练新 CRM",
          "-- 比 A 多一层参数，无明显收益。否决",
          "+### 决策 E/F：沿用 H_EFF=5, CORRECTION_DIM=6",
          "+- 与 SmolVLA 对齐，便于横向比较",
          "+- CRM 只修前 5 步 pose，不修 gripper",
          " ",
          "-**采用方案 A**",
          "+---",
          " ",
          "-### 决策 D：multi_scale_obs 使用方式",
          "-- π0.5 text backbone 是 PaliGemma（Gemma-based, 18-layer），层数和 SmolVLA (16-layer LLaMA) 不同",
          "-- 第一版**只用 fallback 单 obs feature** (`obs_features` 已是 mean-pool 输出)：",
          "-  - 优点：避免对 π0.5 内部结构的依赖、便于调试、与 baseline 比较干净",
          "-  - 缺点：放弃多尺度信号（SmolVLA 上 multi-scale 提升约 +1pp，幅度有限）",
          "-- 若效果不够好，再增量加 multi-scale（需先验证 π0.5 text_model layer 索引）",
          "-",
          "-### 决策 E：H_EFF",
          "-- π0.5 采用开环回放 chunk_size=50（diag log 确认），SmolVLA 用 H_EFF=5",
          "-- 沿用 H_EFF=5 与 SmolVLA 对齐，便于横向比较；CRM 仍在前 5 步内做 correction，后 45 步用 VLA 原始动作",
          "-",
          "-### 决策 F：CORRECTION_DIM",
          "-- 沿用 CORRECTION_DIM=6（只修 pose，不修 gripper）。同 SmolVLA",
          "-",
          " ## 3. 需要修改/新增的文件清单",
          " ",
          " | 文件 | 修改类型 | 说明 |",
          " |------|---------|------|",
          "-| `src/pi05_wrapper.py` | **新增 API** | 增加 `preprocess_obs_batch`（批量预处理）；保留 `encode_prefix` 返回 `obs_features (B, 2048)` + `kv_cache` + `prefix_pad_masks`；保留 `generate_k_samples` 返回 `(B, K, 50, 7)` |",
          "-| `src/precompute_pi05.py` | **新建** | 复制 `train_crm_k1.py::precompute_features_k1` 的逻辑，改用 `Pi05Wrapper`，**不挂 multi_scale hooks**，只保存 `obs_features (2048,)` + `vla_action (5, 6)` + `expert_action (5, 6)` |",
          "-| `src/crm_k1_model.py` | **零修改** | 已支持 `obs_dim=2048` 参数；fallback 单 obs 路径直接可用 |",
          "-| `src/train_crm_k1.py` | **小改** | (1) 增加 `--vla_backbone` 参数 (`smolvla`/`pi05`)；(2) `--obs_dim` 默认按 backbone 切；(3) precompute 分支根据 backbone 选 wrapper；(4) cache 路径加 `_pi05` 后缀避免覆盖 SmolVLA cache |",
          "-| `src/evaluate.py` | **小改** | (1) 删除已有 `obs_proj = nn.Linear(2048, 960)`（random init 路径必死）；(2) `select_action_crm` 中根据 `args.model` 切换 wrapper；(3) CRM 实例化时 `obs_dim` 跟随 backbone；(4) 加载 `--crm_ckpt` 参数指向 π0.5 CRM checkpoint |",
          "-| `src/utils.py` | **小改** | 增加 `PI05_OBS_DIM=2048` 常量，避免硬编码 |",
          "+| `src/pi05_wrapper.py` | **修复 + 新增 API** | (1) 追加 376 key remap（language_model + multi_modal_projector）；(2) 增加 `preprocess_obs_batch`（批量预处理） |",
          "+| `src/precompute_pi05.py` 或改 `src/train_crm_k1.py` | **新建/改造** | 复制 precompute 逻辑，用 `Pi05Wrapper`，不挂 multi_scale hooks，只保存 `obs_features (2048,)` + `vla_action (5, 6)` + `expert_action (5, 6)` |",
          "+| `src/crm_k1_model.py` | **零修改** | 已支持 `obs_dim` 参数；fallback 单 obs 路径直接可用 |",
          "+| `src/train_crm_k1.py` | **小改** | (1) `--vla_backbone` 参数 (`smolvla`/`pi05`)；(2) `--obs_dim` 按 backbone 切默认值；(3) cache 路径加 `_pi05` 后缀 |",
          "+| `src/evaluate.py` | **小改** | (1) 删除 `obs_proj = nn.Linear(2048, 960)`；(2) CRM `obs_dim` 跟随 backbone；(3) 加 `--crm_ckpt` 参数 |",
          "+| `src/utils.py` | **小改** | 增加 `PI05_OBS_DIM=2048` 常量 |",
          " ",
          "-## 4. 命令模板",
          "+---",
          " ",
          "-### Step 0：阻塞性验证（必做，零成本）",
          "+## 4. 执行步骤和命令模板",
          "+",
          "+### Step 0：修复 376 key remap（阻塞性，必须先完成）",
          "+",
          "+需要在 `pi05_wrapper.py` 的 `_fix_vision_tower_keys` 中，追加 language_model 和 multi_modal_projector 的 key mapping。参考 lerobot 官方 patched 版的 `_fix_pytorch_state_dict_keys` 实现。",
          "+",
          "+验证命令：",
          " ```bash",
          "-# bjb2-40593 上的当前 pi05 baseline",
          " ssh connect.bjb2.seetacloud.com",
          " cd /root/acr-vla-conformal-refinement",
          "-# 确认 vision_tower 权重是否非随机",
          "+source /root/miniconda3/etc/profile.d/conda.sh && conda activate base",
          " python -c \"",
          " import torch",
          " from pi05_wrapper import Pi05Wrapper",
          " w = Pi05Wrapper('/root/autodl-tmp/models/pi05_libero_finetuned/')",
          "-vt = w.policy.model.vlm.vision_tower",
          "-ws = [p for n,p in vt.named_parameters() if 'weight' in n]",
          "-print('mean abs:', sum(p.abs().mean() for p in ws).item() / len(ws))",
          "-print('std:', sum(p.std() for p in ws).item() / len(ws))",
          "+# 检查 missing keys = 0",
          "+print('Missing keys should be 0')",
          "+# 检查 language model 权重非随机",
          "+lm = w.policy.model.paligemma_with_expert.paligemma.model.language_model",
          "+ws = [p for n,p in lm.named_parameters() if 'weight' in n][:5]",
          "+for i,p in enumerate(ws):",
          "+    print(f'LM weight {i}: mean_abs={p.abs().mean().item():.4f}, std={p.std().item():.4f}')",
          " \"",
          "-# 期望: mean abs > 0.01, std > 0.01（随机初始化通常 mean~0, std~0.02，需对比 lerobot patched 版本）",
          " ```",
          "-若发现 vision tower 仍是随机权重，**先停所有 pi05 工作**，patch lerobot 的 `_fix_pytorch_state_dict_keys`，参考 mem 记录的 fix。",
          "+**Go 条件**：missing_keys=0，LM weight mean_abs > 0.01",
          " ",
          "-### Step 1：本地准备 pi05_wrapper batch API（半天）",
          "-读 `src/pi05_wrapper.py`（在服务器上），按 SmolVLA `preprocess_obs_batch` 的接口加一个 batch 版本。验证 batch 输出与逐样本一致。",
          "+### Step 0b：Quick Verify（修复后立即做）",
          "+```bash",
          "+CUDA_VISIBLE_DEVICES=0 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 TORCH_COMPILE_DISABLE=1 \\",
          "+python src/evaluate.py \\",
          "+  --benchmark object --mode vla_only --baseline_mode single \\",
          "+  --model pi05 --pi05_path /root/autodl-tmp/models/pi05_libero_finetuned/ \\",
          "+  --seed 42 --n_rollouts 5 --K 1 --max_tasks 2",
          "+```",
          "+**Go 条件**：至少 1 个 task SR > 0%",
          " ",
          "-### Step 2：Precompute π0.5 features（K=5，每 benchmark 一次）",
          "+### Step 1：重跑 Baseline Eval（6 experiments, ~8h）",
          " ```bash",
          "-# bjb2-40593 cuda:0（pi05 baseline 完成后腾出 GPU）",
          "+# 模板（每个 GPU 一个实验）",
          " source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && \\",
          "+CUDA_VISIBLE_DEVICES={GPU} HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 TORCH_COMPILE_DISABLE=1 \\",
          "+nohup python src/evaluate.py \\",
          "+  --benchmark {object|spatial} --mode vla_only --baseline_mode single \\",
          "+  --model pi05 --pi05_path /root/autodl-tmp/models/pi05_libero_finetuned/ \\",
          "+  --seed {42|43|44} --n_rollouts 10 --K 1 \\",
          "+  > logs/eval_pi05_{benchmark}_seed{seed}.log 2>&1 &",
          "+```",
          "+需要 6 GPU 并行，或分批串行。",
          "+",
          "+### Step 2：Precompute π0.5 features（K=1, per benchmark）",
          "+```bash",
          "+source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && \\",
          " CUDA_VISIBLE_DEVICES=0 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 \\",
          " nohup python src/train_crm_k1.py --precompute \\",
          "   --vla_backbone pi05 \\"
        ]
      },
      {
        "oldStart": 109,
        "oldLines": 13,
        "newStart": 146,
        "newLines": 10,
        "lines": [
          "   --cache_dir /root/autodl-tmp/crm_cache_k1_pi05/ \\",
          "   --precompute_batch_size 2 \\",
          "   > logs/precompute_pi05_k1.log 2>&1 &",
          "-echo $!",
          " ```",
          "-**注意**：",
          "-- `precompute_batch_size=2`（π0.5 vRAM 13GB vs SmolVLA 1GB，batch 不能开太大）",
          "-- K=1 cache 与 K=5/K=10 cache 是不同 schema（former 是 per-sample .pt，latter 是 merged）。沿用 K=1 schema 保持与 train_crm_k1 兼容",
          "+注意：π0.5 约 16GB VRAM，`precompute_batch_size=2`；OOM 则降到 1。",
          " ",
          "-### Step 3：训练 π0.5 CRM",
          "+### Step 3：训练 π0.5 CRM（~30-40 min）",
          " ```bash",
          " source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && \\",
          " CUDA_VISIBLE_DEVICES=0 \\"
        ]
      },
      {
        "oldStart": 129,
        "oldLines": 16,
        "newStart": 163,
        "newLines": 14,
        "lines": [
          "   --hidden_dim 256 --bottleneck_dim 192 \\",
          "   --max_correction_norm 1.42 \\",
          "   --loss_mode multi \\",
          "-  --wandb_run_name crm-k1-pi05 \\",
          "   > logs/train_crm_pi05.log 2>&1 &",
          " ```",
          "-注：训练时是 fallback 单 obs 路径（multi_scale_obs.dim()==1）",
          "+训练时是 fallback 单 obs 路径（`multi_scale_obs` dim==1）。CRM 参数量约 ~580K（vs SmolVLA CRM ~323K，差异来自 `layer_proj` 从 960×192 变为 2048×192）。",
          " ",
          "-### Step 4：CRM + π0.5 eval（6 实验：3 seeds × Object+Spatial）",
          "+### Step 4：CRM + π0.5 Eval（6 experiments: 3 seeds × Object + Spatial）",
          " ```bash",
          "-# 模板（每台服务器一个 seed × benchmark）",
          " source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && \\",
          "-CUDA_VISIBLE_DEVICES=X HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 \\",
          "+CUDA_VISIBLE_DEVICES={GPU} HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 TORCH_COMPILE_DISABLE=1 \\",
          " nohup python src/evaluate.py \\",
          "   --benchmark {object|spatial} --mode crm_obs_only \\",
          "   --model pi05 --pi05_path /root/autodl-tmp/models/pi05_libero_finetuned/ \\"
        ]
      },
      {
        "oldStart": 148,
        "oldLines": 49,
        "newStart": 180,
        "newLines": 54,
        "lines": [
          "   > logs/eval_pi05_crm_{benchmark}_seed{seed}.log 2>&1 &",
          " ```",
          " ",
          "+---",
          "+",
          " ## 5. GPU 时间预估",
          " ",
          "-参考 SmolVLA precompute 数据（K=5, batch=4: object ~60min, spatial ~47min, 共 ~107min）和 π0.5 latency profile（VLA sample K=10 = 211ms ≈ SmolVLA 同样级别 batched）：",
          "+| 阶段 | 单次耗时 | GPU 数 |",
          "+|------|---------|--------|",
          "+| Step 0: Key remap fix + verify | ~1h (代码 + 测试) | 1 GPU |",
          "+| Step 1: Baseline eval (6 exps) | ~6-8h wallclock | 6 GPU 并行 |",
          "+| Step 2: Precompute Object + Spatial | ~2h total | 1 GPU |",
          "+| Step 3: CRM train 50 epochs | ~30-40 min | 1 GPU |",
          "+| Step 4: CRM eval (6 exps) | ~6-8h wallclock | 6 GPU 并行 |",
          "+| **总计 wallclock（串行）** | **~17-20h** | **峰值 6 GPU** |",
          "+| **总计 wallclock（Step 1 & 2 并行）** | **~10-12h** | **峰值 6 GPU** |",
          " ",
          "-| 阶段 | 单次耗时 | GPU |",
          "-|------|---------|-----|",
          "-| Precompute Object (K=1) | ~50 min | 1 GPU |",
          "-| Precompute Spatial (K=1) | ~45 min | 1 GPU |",
          "-| CRM 训练 50 epochs | ~30-40 min | 1 GPU |",
          "-| Eval per (seed, benchmark, K=10) | ~6-8 h | 1 GPU |",
          "-| **6 eval 并行** | **~6-8 h wallclock** | **6 GPU** |",
          "-| **总计 wallclock** | **~8-10 h** | **峰值 6 GPU** |",
          "+---",
          " ",
          " ## 6. 风险点和缓解",
          " ",
          " | 风险 | 严重性 | 缓解 |",
          " |------|--------|------|",
          "-| **vision tower 权重仍随机** | **致命** | Step 0 强制验证；若发现问题先 patch lerobot 再做后续 |",
          "-| Gripper 恒为 0.98 | 致命 | 同上，与 vision tower fix 一起解决；precompute 前用 quick verify 跑 5 rollout 看 SR > 0% |",
          "-| precompute_batch_size OOM | 中 | 从 batch=2 起步；监控 GPU mem，OOM 后降到 1 |",
          "-| π0.5 obs_features 分布偏移 | 中 | range `[-12.82, 19.99]` 比 SmolVLA 大很多。precompute 时计算 mean/std 写入 CRM normalization buffer，避免训练不稳定 |",
          "-| pi05 用 chunk_size=50 开环 vs CRM H_EFF=5 | 中 | CRM 只 correct 前 5 步；剩余 45 步用 raw VLA。在 evaluate 中保留这个 mismatch（与 SmolVLA 同语义） |",
          "-| CRM 复用 SmolVLA `max_correction_norm=1.42` 在 pi05 上不适用 | 中 | 训练后查看 delta norm 分布；若 saturated 调大；若 sparse 调小。或与 norm 主配置 0.02 对齐重训 |",
          "-| Multi-scale extraction 跨架构差异 | 低 | 决策 D 已搁置，第一版只用 single obs |",
          "-| Cache 路径污染 SmolVLA cache | 低 | 强制 `--cache_dir` 末尾 `_pi05` 后缀 |",
          "-| HF cache 磁盘满 | 低 | π0.5 模型已在 `/root/autodl-tmp/models/`，cache 也走 `/root/autodl-tmp/` |",
          "-| K=2 adaptive 信号在 pi05 上未验证 | 低 | 主路径先跑 K=10 CRM；adaptive K 作为后续 follow-up |",
          "+| **376 key remap 不完整** | **致命** | 对照 lerobot patched 版本逐一核对 key name mapping；load 后验证 missing_keys=0 |",
          "+| **Gripper 恒 0.98** | **致命** | 可能随 key fix 一并解决（language model 随机→action token 无意义）。若 fix 后仍然 0.98，需审查 action denormalization |",
          "+| **torch.compile 兼容性** | 高 | 所有命令加 `TORCH_COMPILE_DISABLE=1`；lerobot native API 有 `aten.addmm.default` 冲突 |",
          "+| **π0.5 obs_features 分布偏移** | 中 | range `[-12.82, 19.99]` 比 SmolVLA 大。precompute 时计算 mean/std 写入 CRM normalization buffer |",
          "+| **precompute_batch_size OOM** | 中 | 从 batch=2 起步，OOM 降到 1 |",
          "+| **max_correction_norm 适配** | 中 | 训练后查看 delta norm 分布；若 saturated 调大，若 sparse 调小 |",
          "+| **lerobot 包被覆盖** | 中 | Spatial 实验死因疑似 pip reinstall lerobot。锁定 lerobot 版本：`pip install lerobot==0.5.2 --no-deps` |",
          "+| **Step 2/3 在 baseline 完成前可并行** | 低 | Precompute 不依赖 eval 结果（用 demo data），可提前跑；但需确认 key fix 已生效 |",
          " ",
          "+---",
          "+",
          " ## 7. Go/No-Go 判定",
          " ",
          "-每个阶段完成后，下一阶段才能启动：",
          "-",
          " | 阶段 | Go 条件 |",
          " |------|---------|",
          "-| Step 0 → Step 1 | vision tower 权重非随机；pi05 baseline 至少一个 task SR > 0% |",
          "-| Step 1 → Step 2 | `preprocess_obs_batch` 输出与 single-sample 数值一致（abs diff < 1e-5） |",
          "-| Step 2 → Step 3 | precompute 完成，cache manifest 写入，n_samples 与 SmolVLA cache 一致（spatial ~12k, object ~14k） |",
          "-| Step 3 → Step 4 | val_loss 收敛（best ≤ 训练前期 + 显著下降），无 NaN |",
          "-| Step 4 验证 | 至少 1 个 seed Object SR ≥ pi05 baseline SR + 3pp，否则需诊断（参考 `diagnose_*.md` 模板） |",
          "+| Step 0 → Step 0b | missing_keys=0；LM weight 非随机 |",
          "+| Step 0b → Step 1 | 至少 1 个 task SR > 0% |",
          "+| Step 1 → Step 2 | baseline 至少 Object mean SR > 30%（π0.5 3.6B 应强于 SmolVLA 0.4B 的 ~60%，但留容忍度） |",
          "+| Step 2 → Step 3 | precompute 完成，manifest 写入，n_samples 合理（spatial ~12k, object ~14k） |",
          "+| Step 3 → Step 4 | val_loss 收敛，无 NaN，best val_loss 显著低于初始 |",
          "+| Step 4 验证 | 至少 1 个 seed Object SR ≥ baseline SR + 3pp |",
          " ",
          "+---",
          "+",
          " ## 8. 不做的事",
          " ",
          "-- 不复用 SmolVLA CRM 权重做 fine-tune（决策 A 否决）",
          "-- 不引入 π0.5 multi-scale extraction（决策 D 第一版 skip）",
          "+- 不复用 SmolVLA CRM 权重",
          "+- 不引入 π0.5 multi-scale extraction（第一版）",
          " - 不修改现有 SmolVLA pipeline 任何文件",
          "-- 不在 pi05 eval 完成前启动 adaptive K 实验",
          "+- 不在 baseline 验证通过前启动 precompute/CRM 训练",
          "+- 不在 pi05 CRM eval 完成前启动 adaptive K 实验"
        ]
      }
    ],
    "originalFile": "# π0.5 CRM Pipeline 方案 (2026-05-21)\n\n## 1. 现状摘要\n\n### SmolVLA 现有 pipeline（LOCKED）\n- `SmolVLAWrapper` (`src/smolvla_wrapper.py`)\n  - `encode_prefix(...)` → `obs_features (B, 960)`, `kv_cache`, `prefix_pad_masks`\n  - `generate_k_samples(kv, masks, K)` → `(B, K, chunk_size=50, FULL_ACTION_DIM=7)`\n  - `preprocess_obs_batch` 已支持 batched precompute\n- `MultiScaleCRM` (`src/crm_k1_model.py`)\n  - 输入: `base_action (B, 30)` + `multi_scale_obs (B, 4, 960)` 或 fallback `(B, 960)`\n  - 参数: `action_dim=H_EFF*CORRECTION_DIM=30`, `obs_dim=960`, `hidden_dim=256`, `bottleneck_dim=192`\n  - 支持多层 FiLM + action-conditioned attention，~323K params\n- `MultiScaleFeatureExtractor`\n  - hooks 注册在 `flow.vlm_with_expert.vlm.model.text_model.layers[i].input_layernorm` (i ∈ [3,7,11,15])\n  - 最后一层 hook 在 `text_model.norm`\n- 训练 (`src/train_crm_k1.py`)\n  - Phase 1 `--precompute`: 用 SmolVLA + MultiScaleExtractor 跑 LIBERO demo，cache `(multi_scale_obs, obs_features, vla_action, expert_action)` per sample\n  - Phase 2: 加载 cache，多损失训练 (L2 + direction + triplet + magnitude)\n\n### π0.5 现状\n- `pi05_wrapper.py` 已存在（diag log 确认）：\n  - `obs_features` shape `[1, 2048]`, range `[-12.82, 19.99]`\n  - K-sample 输出 `[B, K, 50, 7]`，action_dim=7（同 SmolVLA：6D pose + 1D gripper）\n  - `_fix_vision_tower_keys` 已修复 437 个 key mapping\n- `evaluate.py` 内已注入 `obs_proj = nn.Linear(2048, 960)`，但**未训练（random init）**，等于丢掉所有信息\n- 现 baseline eval 在跑（3 seeds × Object + Spatial 共 6 jobs）\n\n### ⚠️ 阻塞性风险（必须先确认）\n1. **Vision tower 权重静默加载失败 bug**：mem 记录此前 5 轮 fix 都是 0% SR，根因是 `load_state_dict` 被 try/except 吞掉。官方 lerobot-eval patched 后 3/3 success\n2. **当前 baseline 状态**：进度报告显示 `eval-pi05-baseline-object-seed42` 在 bjb2-40593 上前 2 个 task 全 0% (0/40)。**需要先确认 vision tower fix 是否已生效于当前 eval 跑的代码路径**，否则后续 CRM 工作全部白做\n3. **Gripper 恒为 0.98 bug**：diag log 显示所有 sample 的 gripper 值恒定 ~0.98，无法 pick。需确认是否随 vision tower fix 一并解决\n\n## 2. 设计决策\n\n### 决策 A：CRM obs_dim = 2048（推荐）\n- 不复用 SmolVLA CRM 权重\n- 直接训一个 obs_dim=2048 的 MultiScaleCRM（架构相同，只改 obs_dim 参数）\n- 优点：无信息损失；CRM MLP 主要参数在 hidden_dim×hidden_dim，obs_dim 改变只影响 `layer_proj` 一层\n- 缺点：需重新跑 precompute（约 2-3h/benchmark）\n\n### 决策 B：固定 Linear(2048→960) + 复用 SmolVLA CRM（不推荐）\n- 用 SmolVLA 的 obs 统计量去 normalize 投影后的 960D 特征——分布不匹配\n- 即便 projection 可学习，仍是 bottleneck，且复用 SmolVLA CRM 的语义假设不一定迁移\n\n### 决策 C：Linear(2048→960) + 联合训练新 CRM\n- 比 A 多一层参数，无明显收益。否决\n\n**采用方案 A**\n\n### 决策 D：multi_scale_obs 使用方式\n- π0.5 text backbone 是 PaliGemma（Gemma-based, 18-layer），层数和 SmolVLA (16-layer LLaMA) 不同\n- 第一版**只用 fallback 单 obs feature** (`obs_features` 已是 mean-pool 输出)：\n  - 优点：避免对 π0.5 内部结构的依赖、便于调试、与 baseline 比较干净\n  - 缺点：放弃多尺度信号（SmolVLA 上 multi-scale 提升约 +1pp，幅度有限）\n- 若效果不够好，再增量加 multi-scale（需先验证 π0.5 text_model layer 索引）\n\n### 决策 E：H_EFF\n- π0.5 采用开环回放 chunk_size=50（diag log 确认），SmolVLA 用 H_EFF=5\n- 沿用 H_EFF=5 与 SmolVLA 对齐，便于横向比较；CRM 仍在前 5 步内做 correction，后 45 步用 VLA 原始动作\n\n### 决策 F：CORRECTION_DIM\n- 沿用 CORRECTION_DIM=6（只修 pose，不修 gripper）。同 SmolVLA\n\n## 3. 需要修改/新增的文件清单\n\n| 文件 | 修改类型 | 说明 |\n|------|---------|------|\n| `src/pi05_wrapper.py` | **新增 API** | 增加 `preprocess_obs_batch`（批量预处理）；保留 `encode_prefix` 返回 `obs_features (B, 2048)` + `kv_cache` + `prefix_pad_masks`；保留 `generate_k_samples` 返回 `(B, K, 50, 7)` |\n| `src/precompute_pi05.py` | **新建** | 复制 `train_crm_k1.py::precompute_features_k1` 的逻辑，改用 `Pi05Wrapper`，**不挂 multi_scale hooks**，只保存 `obs_features (2048,)` + `vla_action (5, 6)` + `expert_action (5, 6)` |\n| `src/crm_k1_model.py` | **零修改** | 已支持 `obs_dim=2048` 参数；fallback 单 obs 路径直接可用 |\n| `src/train_crm_k1.py` | **小改** | (1) 增加 `--vla_backbone` 参数 (`smolvla`/`pi05`)；(2) `--obs_dim` 默认按 backbone 切；(3) precompute 分支根据 backbone 选 wrapper；(4) cache 路径加 `_pi05` 后缀避免覆盖 SmolVLA cache |\n| `src/evaluate.py` | **小改** | (1) 删除已有 `obs_proj = nn.Linear(2048, 960)`（random init 路径必死）；(2) `select_action_crm` 中根据 `args.model` 切换 wrapper；(3) CRM 实例化时 `obs_dim` 跟随 backbone；(4) 加载 `--crm_ckpt` 参数指向 π0.5 CRM checkpoint |\n| `src/utils.py` | **小改** | 增加 `PI05_OBS_DIM=2048` 常量，避免硬编码 |\n\n## 4. 命令模板\n\n### Step 0：阻塞性验证（必做，零成本）\n```bash\n# bjb2-40593 上的当前 pi05 baseline\nssh connect.bjb2.seetacloud.com\ncd /root/acr-vla-conformal-refinement\n# 确认 vision_tower 权重是否非随机\npython -c \"\nimport torch\nfrom pi05_wrapper import Pi05Wrapper\nw = Pi05Wrapper('/root/autodl-tmp/models/pi05_libero_finetuned/')\nvt = w.policy.model.vlm.vision_tower\nws = [p for n,p in vt.named_parameters() if 'weight' in n]\nprint('mean abs:', sum(p.abs().mean() for p in ws).item() / len(ws))\nprint('std:', sum(p.std() for p in ws).item() / len(ws))\n\"\n# 期望: mean abs > 0.01, std > 0.01（随机初始化通常 mean~0, std~0.02，需对比 lerobot patched 版本）\n```\n若发现 vision tower 仍是随机权重，**先停所有 pi05 工作**，patch lerobot 的 `_fix_pytorch_state_dict_keys`，参考 mem 记录的 fix。\n\n### Step 1：本地准备 pi05_wrapper batch API（半天）\n读 `src/pi05_wrapper.py`（在服务器上），按 SmolVLA `preprocess_obs_batch` 的接口加一个 batch 版本。验证 batch 输出与逐样本一致。\n\n### Step 2：Precompute π0.5 features（K=5，每 benchmark 一次）\n```bash\n# bjb2-40593 cuda:0（pi05 baseline 完成后腾出 GPU）\nsource /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && \\\nCUDA_VISIBLE_DEVICES=0 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 \\\nnohup python src/train_crm_k1.py --precompute \\\n  --vla_backbone pi05 \\\n  --pi05_path /root/autodl-tmp/models/pi05_libero_finetuned/ \\\n  --benchmark object spatial \\\n  --cache_dir /root/autodl-tmp/crm_cache_k1_pi05/ \\\n  --precompute_batch_size 2 \\\n  > logs/precompute_pi05_k1.log 2>&1 &\necho $!\n```\n**注意**：\n- `precompute_batch_size=2`（π0.5 vRAM 13GB vs SmolVLA 1GB，batch 不能开太大）\n- K=1 cache 与 K=5/K=10 cache 是不同 schema（former 是 per-sample .pt，latter 是 merged）。沿用 K=1 schema 保持与 train_crm_k1 兼容\n\n### Step 3：训练 π0.5 CRM\n```bash\nsource /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && \\\nCUDA_VISIBLE_DEVICES=0 \\\nnohup python src/train_crm_k1.py \\\n  --vla_backbone pi05 \\\n  --obs_dim 2048 \\\n  --benchmark object spatial \\\n  --cache_dir /root/autodl-tmp/crm_cache_k1_pi05/ \\\n  --output_dir /root/autodl-tmp/checkpoints/crm_k1_pi05/ \\\n  --epochs 50 --batch_size 512 --lr 1e-3 \\\n  --hidden_dim 256 --bottleneck_dim 192 \\\n  --max_correction_norm 1.42 \\\n  --loss_mode multi \\\n  --wandb_run_name crm-k1-pi05 \\\n  > logs/train_crm_pi05.log 2>&1 &\n```\n注：训练时是 fallback 单 obs 路径（multi_scale_obs.dim()==1）\n\n### Step 4：CRM + π0.5 eval（6 实验：3 seeds × Object+Spatial）\n```bash\n# 模板（每台服务器一个 seed × benchmark）\nsource /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && \\\nCUDA_VISIBLE_DEVICES=X HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 \\\nnohup python src/evaluate.py \\\n  --benchmark {object|spatial} --mode crm_obs_only \\\n  --model pi05 --pi05_path /root/autodl-tmp/models/pi05_libero_finetuned/ \\\n  --crm_ckpt /root/autodl-tmp/checkpoints/crm_k1_pi05/crm_k1_best.pt \\\n  --crm_obs_dim 2048 \\\n  --seed {42|43|44} --n_rollouts 10 --K 10 \\\n  > logs/eval_pi05_crm_{benchmark}_seed{seed}.log 2>&1 &\n```\n\n## 5. GPU 时间预估\n\n参考 SmolVLA precompute 数据（K=5, batch=4: object ~60min, spatial ~47min, 共 ~107min）和 π0.5 latency profile（VLA sample K=10 = 211ms ≈ SmolVLA 同样级别 batched）：\n\n| 阶段 | 单次耗时 | GPU |\n|------|---------|-----|\n| Precompute Object (K=1) | ~50 min | 1 GPU |\n| Precompute Spatial (K=1) | ~45 min | 1 GPU |\n| CRM 训练 50 epochs | ~30-40 min | 1 GPU |\n| Eval per (seed, benchmark, K=10) | ~6-8 h | 1 GPU |\n| **6 eval 并行** | **~6-8 h wallclock** | **6 GPU** |\n| **总计 wallclock** | **~8-10 h** | **峰值 6 GPU** |\n\n## 6. 风险点和缓解\n\n| 风险 | 严重性 | 缓解 |\n|------|--------|------|\n| **vision tower 权重仍随机** | **致命** | Step 0 强制验证；若发现问题先 patch lerobot 再做后续 |\n| Gripper 恒为 0.98 | 致命 | 同上，与 vision tower fix 一起解决；precompute 前用 quick verify 跑 5 rollout 看 SR > 0% |\n| precompute_batch_size OOM | 中 | 从 batch=2 起步；监控 GPU mem，OOM 后降到 1 |\n| π0.5 obs_features 分布偏移 | 中 | range `[-12.82, 19.99]` 比 SmolVLA 大很多。precompute 时计算 mean/std 写入 CRM normalization buffer，避免训练不稳定 |\n| pi05 用 chunk_size=50 开环 vs CRM H_EFF=5 | 中 | CRM 只 correct 前 5 步；剩余 45 步用 raw VLA。在 evaluate 中保留这个 mismatch（与 SmolVLA 同语义） |\n| CRM 复用 SmolVLA `max_correction_norm=1.42` 在 pi05 上不适用 | 中 | 训练后查看 delta norm 分布；若 saturated 调大；若 sparse 调小。或与 norm 主配置 0.02 对齐重训 |\n| Multi-scale extraction 跨架构差异 | 低 | 决策 D 已搁置，第一版只用 single obs |\n| Cache 路径污染 SmolVLA cache | 低 | 强制 `--cache_dir` 末尾 `_pi05` 后缀 |\n| HF cache 磁盘满 | 低 | π0.5 模型已在 `/root/autodl-tmp/models/`，cache 也走 `/root/autodl-tmp/` |\n| K=2 adaptive 信号在 pi05 上未验证 | 低 | 主路径先跑 K=10 CRM；adaptive K 作为后续 follow-up |\n\n## 7. Go/No-Go 判定\n\n每个阶段完成后，下一阶段才能启动：\n\n| 阶段 | Go 条件 |\n|------|---------|\n| Step 0 → Step 1 | vision tower 权重非随机；pi05 baseline 至少一个 task SR > 0% |\n| Step 1 → Step 2 | `preprocess_obs_batch` 输出与 single-sample 数值一致（abs diff < 1e-5） |\n| Step 2 → Step 3 | precompute 完成，cache manifest 写入，n_samples 与 SmolVLA cache 一致（spatial ~12k, object ~14k） |\n| Step 3 → Step 4 | val_loss 收敛（best ≤ 训练前期 + 显著下降），无 NaN |\n| Step 4 验证 | 至少 1 个 seed Object SR ≥ pi05 baseline SR + 3pp，否则需诊断（参考 `diagnose_*.md` 模板） |\n\n## 8. 不做的事\n\n- 不复用 SmolVLA CRM 权重做 fine-tune（决策 A 否决）\n- 不引入 π0.5 multi-scale extraction（决策 D 第一版 skip）\n- 不修改现有 SmolVLA pipeline 任何文件\n- 不在 pi05 eval 完成前启动 adaptive K 实验\n",
    "userModified": false
  }
}
````

</details>

---


### Assistant

_source line 313_

方案已更新至 `artifacts/pi05_crm_pipeline_plan.md`。

关键发现和方案要点：

**当前阻塞**：π0.5 baseline 全线 0% SR，根因不是 vision tower（437 keys 已修），而是 **language_model + multi_modal_projector 的 376 个 key 仍然 missing**，导致 LM 在随机权重下运行。官方 lerobot-eval patched 版 3/3 = 100%，证明模型有效。

**Pipeline 5 步**：
1. **Step 0**：修复 376 key remap → 验证 missing_keys=0 + quick verify SR > 0%（阻塞性）
2. **Step 1**：重跑 baseline eval（3 seeds × 2 benchmarks，6 GPU 并行，~8h）
3. **Step 2**：Precompute π0.5 features（obs_dim=2048，K=1，~2h）
4. **Step 3**：训练 obs_dim=2048 的新 CRM（~30-40 min，~580K params）
5. **Step 4**：CRM + π0.5 eval（6 experiments，~8h）

**核心决策**：采用方案 A（obs_dim=2048 新 CRM），不复用 SmolVLA CRM；第一版只用 single obs feature，不做 multi-scale；总 wallclock 约 10-12h（并行优化后）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0b83dcf7-139e-42b0-bcd9-687872ddb233",
  "uuid": "370c5491-6109-4bf8-88e5-a1fbfda92126",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D6f2qN9zCdtA75m1M4izf2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5284,
      "cache_read_input_tokens": 59633,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5284
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Task result

_source line 314_

方案已更新至 `artifacts/pi05_crm_pipeline_plan.md`。

关键发现和方案要点：

**当前阻塞**：π0.5 baseline 全线 0% SR，根因不是 vision tower（437 keys 已修），而是 **language_model + multi_modal_projector 的 376 个 key 仍然 missing**，导致 LM 在随机权重下运行。官方 lerobot-eval patched 版 3/3 = 100%，证明模型有效。

**Pipeline 5 步**：
1. **Step 0**：修复 376 key remap → 验证 missing_keys=0 + quick verify SR > 0%（阻塞性）
2. **Step 1**：重跑 baseline eval（3 seeds × 2 benchmarks，6 GPU 并行，~8h）
3. **Step 2**：Precompute π0.5 features（obs_dim=2048，K=1，~2h）
4. **Step 3**：训练 obs_dim=2048 的新 CRM（~30-40 min，~580K params）
5. **Step 4**：CRM + π0.5 eval（6 experiments，~8h）

**核心决策**：采用方案 A（obs_dim=2048 新 CRM），不复用 SmolVLA CRM；第一版只用 single obs feature，不做 multi-scale；总 wallclock 约 10-12h（并行优化后）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 416765,
  "duration_api_ms": 415644,
  "num_turns": 16,
  "stop_reason": "end_turn",
  "session_id": "0b83dcf7-139e-42b0-bcd9-687872ddb233",
  "total_cost_usd": 1.4765210500000006,
  "usage": {
    "input_tokens": 12315,
    "cache_creation_input_tokens": 53076,
    "cache_read_input_tokens": 411761,
    "output_tokens": 8380,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 53076,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 413,
        "cache_read_input_tokens": 59633,
        "cache_creation_input_tokens": 5284,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 5284
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1607,
      "outputTokens": 18400,
      "cacheReadInputTokens": 3377298,
      "cacheCreationInputTokens": 189203,
      "webSearchRequests": 0,
      "costUSD": 0.6678405499999999,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 12315,
      "outputTokens": 8380,
      "cacheReadInputTokens": 411761,
      "cacheCreationInputTokens": 53076,
      "webSearchRequests": 0,
      "costUSD": 0.8086804999999999,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "54d2af2b-ce7e-44b5-8ec5-edf0b5828fbf"
}
```

</details>

---
