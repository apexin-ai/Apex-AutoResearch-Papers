# ssh eval prep and a1 diag

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_eval_prep_and_a1_diag_20260521T170325_result.json`
- **Structured JSON:** [`1cfd5a3eab0623535869.json`](../../sessions/1c/1cfd5a3eab0623535869.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有信息已收集完毕。

---

## 1. Eval 参数确认（westd-45947）

**参数名对照**（左=你给的名字，右=脚本实际名字）：

| 你给的参数 | 正确参数名 | 说明 |
|---|---|---|
| `--model_type` | ✅ `--model_type` | choices: `baseline`, `a1`, `a3` |
| `--checkpoint_path` | ❌ `--checkpoint` | 无 `_path` 后缀 |
| `--scene` | ❌ `--suite` | 必须参数 |
| `--max_episodes` | ❌ `--n_episodes` | 默认 50 |
| `--no_refine` | ✅ `--no_refine` | |
| `--output_dir` | ❌ `--save_dir` | 默认 `/root/autodl-tmp/eval_results` |
| `--sdf_gt_path` | ✅ `--sdf_gt_path` | |

**额外参数**：`--sdf_checkpoint`（SDF modules 单独的 checkpoint 目录）、`--refine_alpha`（默认 0.1）、`--refine_margin`（默认 0.01）、`--collision_threshold`、`--verify_obstacles`、`--safety_level`（I/II，默认 II）、`--max_steps`（默认 300）、`--seed`、`--gpu`、`--save_videos`、`--verbose`

**A3 best checkpoint**：
- 路径：`/root/autodl-tmp/checkpoints/a3_grad_refine_object_pudding/a3_grad_refine_object_pudding_seed0/best/`
- best_loss = **0.01439** at step 26000
- 包含文件：`model.safetensors` (6.7GB), `lora_params.pt` (128MB), `sdf_decoder.pt` (1.5MB), `ee_extractor.pt` (1MB), `aux_metadata.pt`, `optimizer.pt`

**A3 训练进度**：97% (29049/30000)，仍在运行，~4s/step → **约 1 小时完成**

**构造好的 A3 eval 命令示例**：
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate libero
python scripts/eval_safelibero.py \
  --model_type a3 \
  --checkpoint /root/autodl-tmp/checkpoints/a3_grad_refine_object_pudding/a3_grad_refine_object_pudding_seed0/best \
  --suite object_pudding \
  --n_episodes 50 \
  --save_dir /root/autodl-tmp/eval_results/a3_object_pudding \
  --gpu 0
```

---

## 2. A1 Phase 2 诊断（westd-35807）

### 结论：Phase 2 **已正常触发**

**代码逻辑**（`train_a1_sdf_aux.py:164-197`）：
- 触发条件：`global_step == warmup_phase_steps (默认5000) and phase == 1`
- 触发动作：
  1. `self.phase = 2`
  2. 解冻所有 LoRA params（`requires_grad = True`）
  3. 注册 grad hooks 做 100 步线性 warmup（`grad * scale`，scale 从 0 线性增到 1）
  4. step 5100 时移除 hooks，LoRA 梯度恢复全量
- 有 `logging.info("Phase 2: unfroze %d LoRA params...")` 日志

**Checkpoint 证据**：
- step 8000 的 `aux_metadata.pt` → `{'phase': 2, 'global_step': 8000}` ✅
- step 10000 的 `aux_metadata.pt` → `{'phase': 2, 'global_step': 10000}` ✅
- → Phase 2 在 step 5000 正确触发

**日志为什么 grep 不到 Phase 2 消息**：
- `logging.basicConfig` 在 line 302 有配置（level=INFO）
- 但 train.log 由 `2>&1 | tee` 生成，tqdm 大量 `\r` 回车覆盖导致 logging.info 输出被嵌入长行内，`grep` 按行匹配失败（实际存在但被 `\r` 分隔符遮蔽）
- 这不是 bug，只是日志格式的可读性问题

**A1 当前进度**：step ~11613/30000 (39%)，GPU 2 运行中，~4s/step → **约 20 小时完成**

---
