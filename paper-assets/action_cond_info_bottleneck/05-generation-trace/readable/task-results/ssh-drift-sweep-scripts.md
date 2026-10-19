# ssh drift sweep scripts

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_drift-sweep-scripts_20260517T163738_result.json`
- **Structured JSON:** [`0cd62294700e53fd39ff.json`](../../sessions/0c/0cd62294700e53fd39ff.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。

### 产出汇报

**Part 1 — λ_drift sweep 脚本（3 个）：**
- `/root/acib/scripts/run_v72_drift05.sh` — `--lambda_drift 0.5`, output → `acib_v72_drift05`
- `/root/acib/scripts/run_v72_drift10.sh` — `--lambda_drift 1.0`, output → `acib_v72_drift10`
- `/root/acib/scripts/run_v72_drift20.sh` — `--lambda_drift 2.0`, output → `acib_v72_drift20`

所有参数与 v7.2 一致，仅改 `--lambda_drift` 和 `--output_dir`。

**Part 2 — contrastive_grad_scale 代码修改：**
- `acib/config.py` 第 44 行：添加 `contrastive_grad_scale: float = 1.0`
- `acib/acib_policy.py` 第 176 行：`contrastive_loss_val = contrastive_loss_val * self.acib_config.contrastive_grad_scale`
- `scripts/train_acib.py`：添加 CLI 参数 `--contrastive_grad_scale`（float, default=1.0），并传入 `build_acib_policy` 的 config 构建
- `/root/acib/scripts/run_v72_contrastive_scale01.sh` — `--contrastive_grad_scale 0.1`, `--lambda_drift 0.1`, output → `acib_v72_ctr_scale01`

**验证结果：**
- `ACIBConfig(contrastive_grad_scale=0.1).contrastive_grad_scale` → `0.1` ✓
- `--help` 输出包含 `--contrastive_grad_scale` ✓
- `acib_policy.py` 第 176 行正确应用 scale ✓
- 所有脚本已 `chmod +x` ✓

---
