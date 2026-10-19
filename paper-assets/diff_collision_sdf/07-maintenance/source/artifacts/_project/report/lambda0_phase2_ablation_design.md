## λ_sdf=0 Phase 2 Ablation 方案

### 修改文件
- 文件: `scripts/train_a1_sdf_aux_pi05.py`
- 修改涉及 3 处：参数定义 (L86)、`__init__` (L123)、`on_loss_computed` (L265)

### 新增参数
- `--phase2_lambda_sdf`: Phase 2 的 SDF loss 权重（默认 None = 跟随 --lambda_sdf，设为 0 时 = ablation）
- `--phase2_lambda_ee`: Phase 2 的 EE loss 权重（默认 None = 跟随 --lambda_ee，设为 0 时一并消除）

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
python scripts/train_a1_sdf_aux_pi05.py \
    --scene spatial_bowl --seed 0 --gpu 0 \
    --phase2_lambda_sdf 0 --phase2_lambda_ee 0 \
    --exp_name a1_ablation_nosdf_p2_spatial_bowl_seed0
```

### GPU-Hours 估算
- 每 run: ~38.3 GPU-hours (30000 steps × 4.6s/step)
- 推荐 seed 数: 3
- 1 scene: ~115 GPU-hours
- 2 scenes: ~230 GPU-hours

### 设计要点
1. Phase 1 完全不变
2. SDF/EE 模块在 Phase 2 仍 forward（不删除），只是 loss 权重为 0
3. 默认行为向后兼容（不传新参数时行为不变）
