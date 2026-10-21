# code lambda sdf phase2 param

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_lambda_sdf_phase2_param_20260524T143454_result.json`
- **Structured JSON:** [`d971461d54ba91d54e9a.json`](../../sessions/d9/d971461d54ba91d54e9a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

File written and verified. Here's the summary:

**Modified file:** `artifacts/train_a1_sdf_aux_pi05.py`

**Diff (3 changes vs original):**

1. **`parse_args()` — 新增参数** (line 87-88):
   ```python
   p.add_argument("--lambda_sdf_phase2", type=float, default=None,
                  help="SDF loss weight for Phase 2 (step >= phase1_steps). If None, uses --lambda_sdf throughout.")
   ```

2. **`SdfAuxHooks.__init__` — 存储 phase2 值** (line 120):
   ```python
   self.lambda_sdf_phase2 = args.lambda_sdf_phase2 if args.lambda_sdf_phase2 is not None else args.lambda_sdf
   ```

3. **`on_step_start` — Phase 2 切换时打印日志** (lines 192-195):
   ```python
   if self.lambda_sdf != self.lambda_sdf_phase2:
       logging.info("[Phase 2] Switching lambda_sdf: %.4f -> %.4f",
                    self.lambda_sdf, self.lambda_sdf_phase2)
   ```

4. **`on_loss_computed` — 按 phase 选择 lambda** (line 230):
   ```python
   _lsdf = self.lambda_sdf if self.phase == 1 else self.lambda_sdf_phase2
   total = action_loss + _lsdf * sdf_losses["sdf_total"] + self.lambda_ee * ee_loss
   ```
   同时在 `aux_info` 中添加 `"lambda_sdf_effective": _lsdf` 用于 wandb tracking。

5. **`main()` — 启动时记录 phase2 override** (lines 285-286):
   ```python
   if args.lambda_sdf_phase2 is not None:
       logging.info("Phase 2 lambda_sdf override: %.4f", args.lambda_sdf_phase2)
   ```

**行为保证：** 不传 `--lambda_sdf_phase2` 时，`default=None` → `lambda_sdf_phase2 = lambda_sdf`，与修改前完全一致。

**训练命令示例：**
```bash
python scripts/train_a1_sdf_aux_pi05.py \
    --scene object_pudding --seed 0 --gpu 2 \
    --batch_size 32 --num_train_steps 30000 \
    --lambda_sdf 0.005 --lambda_sdf_phase2 0 \
    --lambda_ee 0.01 --lr 2.5e-5 \
    --save_interval 2000 \
    --exp_name a1_sdf_pi05_object_pudding_seed0_l000_phase2off
```

需要 `sync_code_to_remote` 把文件推到服务器 `/root/colliforce-vla/scripts/` 后才能运行。

---
