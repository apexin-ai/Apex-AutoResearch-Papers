# research lambda0 ablation design

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_lambda0_ablation_design_20260523T162831_result.json`
- **Structured JSON:** [`015e8101c7d2272dfd28.json`](../../sessions/01/015e8101c7d2272dfd28.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完整代码已读完（355 行）。以下是分析方案：

## λ_sdf=0 Phase 2 Ablation 方案

### 修改文件
- 文件: `scripts/train_a1_sdf_aux_pi05.py`
- 修改涉及 3 处：参数定义 (L86)、`__init__` (L123)、`on_loss_computed` (L265)

### 新增参数
```
--phase2_lambda_sdf: Phase 2 的 SDF loss 权重（默认 None = 跟随 --lambda_sdf，设为 0 时 = ablation）
--phase2_lambda_ee:  Phase 2 的 EE loss 权重（默认 None = 跟随 --lambda_ee，设为 0 时一并消除）
```

### Diff

```diff
--- a/scripts/train_a1_sdf_aux_pi05.py
+++ b/scripts/train_a1_sdf_aux_pi05.py
@@ -88,6 +88,10 @@
     p.add_argument("--sdf_clamp", type=float, default=0.05)
     p.add_argument("--eikonal_weight", type=float, default=0.1)
     p.add_argument("--warmup_phase_steps", type=int, default=5000)
+    p.add_argument("--phase2_lambda_sdf", type=float, default=None,
+                   help="SDF loss weight in Phase 2 (default: same as --lambda_sdf; set 0 for ablation)")
+    p.add_argument("--phase2_lambda_ee", type=float, default=None,
+                   help="EE loss weight in Phase 2 (default: same as --lambda_ee; set 0 for ablation)")
     return p.parse_args()
 
 
@@ -121,6 +125,9 @@
         self.lambda_sdf = args.lambda_sdf
         self.lambda_ee = args.lambda_ee
         self.n_query_points = args.n_query_points
+        self.phase2_lambda_sdf = args.phase2_lambda_sdf if args.phase2_lambda_sdf is not None else args.lambda_sdf
+        self.phase2_lambda_ee = args.phase2_lambda_ee if args.phase2_lambda_ee is not None else args.lambda_ee
 
         self.sdf_decoder = SDFDecoder(feature_dim=1024, hidden_dim=256)
         self.ee_extractor = EEPositionExtractor(feature_dim=1024, hidden_dim=256)
@@ -263,7 +270,10 @@
         ee_pred = self.ee_extractor(pooled)
         ee_loss = F.mse_loss(ee_pred, ee_gt)
 
-        total = action_loss + self.lambda_sdf * sdf_losses["sdf_total"] + self.lambda_ee * ee_loss
+        _lsdf = self.lambda_sdf if self.phase == 1 else self.phase2_lambda_sdf
+        _lee = self.lambda_ee if self.phase == 1 else self.phase2_lambda_ee
+        total = action_loss + _lsdf * sdf_losses["sdf_total"] + _lee * ee_loss
 
         aux_info = {
             "action_loss": action_loss.item(),
```

### 调用方式

```bash
# λ_sdf=0 ablation（Phase 1 正常预热，Phase 2 只有 action loss）
python scripts/train_a1_sdf_aux_pi05.py \
    --scene spatial_bowl \
    --seed 0 --gpu 0 \
    --phase2_lambda_sdf 0 --phase2_lambda_ee 0 \
    --exp_name a1_ablation_nosdf_p2_spatial_bowl_seed0
```

### GPU-Hours 估算
- 30000 steps × 4.6s/step = 138,000s = **38.3 GPU-hours/run**
- 推荐 seed 数: **3**（与 A1 主实验对齐）
- 总计: **~115 GPU-hours**（3 seeds）
- 如果只跑 1 scene (spatial_bowl): 115 GPU-hours
- 如果跑 2 scenes: ~230 GPU-hours

### 注意事项

1. **Phase 1 完全不变** — `lambda_sdf`/`lambda_ee` 仅在 Phase 1 使用，`phase2_lambda_*` 只在 `self.phase >= 2` 时生效
2. **SDF Decoder / EE Extractor 在 Phase 2 仍 forward** — 模块不删除、不冻结，只是 loss 系数为 0。这意味着 SDF/EE forward pass 仍消耗计算，但不产生梯度信号到 LoRA（因为 `0 * sdf_total` 对 LoRA 参数梯度贡献为零）
3. **Phase 1 预热效果被保留** — SDF Decoder 和 EE Extractor 在前 5000 步正常训练（在 detached features 上），所以 Phase 1 confound 仍存在。这正是实验目的：隔离 "Phase 1 预热" vs "Phase 2 SDF 梯度信号" 的效果
4. **`--phase2_lambda_ee 0` 也设为 0** — 否则 EE loss 仍会通过梯度影响 LoRA，不是纯净的 ablation。如果想只 ablate SDF 保留 EE，可以只设 `--phase2_lambda_sdf 0`
5. **不需要修改 `on_step_start`** — Phase 切换、LoRA 解冻、grad warmup 逻辑完全不变
6. **exp_name 建议统一命名** 如 `a1_ablation_nosdf_p2_{scene}_seed{seed}`，和 A1 主实验区分
7. **默认行为向后兼容** — 不传 `--phase2_lambda_sdf` 时行为和原脚本完全一致

### 设计决策备注

**为什么不直接在 Phase 2 跳过 SDF/EE forward？** 跳过 forward 会节省约 5-10% 计算，但引入额外代码路径差异。保持 forward 可以确保唯一的变量是 loss 权重，实验结论更干净。如果 GPU-hours 紧张可以后续优化。

---
