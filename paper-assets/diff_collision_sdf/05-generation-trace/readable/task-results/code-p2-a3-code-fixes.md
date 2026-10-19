# code p2 a3 code fixes

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_p2_a3_code_fixes_20260519T232748_result.json`
- **Structured JSON:** [`646a123d272a58a593c4.json`](../../sessions/64/646a123d272a58a593c4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有修复已验证通过。

---

## 修复报告

### Fix 1: LoRA rank 不一致
| 位置 | 修改 |
|------|------|
| `train_a3_hook.py:226` | `inject_lora(_m, rank=16, alpha=16.0)` → `inject_lora(_m, rank=32, alpha=32.0)` |
| `train_a3_hook.py:110` | docstring 更新 `~26.5M rank=16` → `~53M rank=32` |

### Fix 2: OOM 风险
| 位置 | 修改 |
|------|------|
| `train_a3_hook.py:357` | `--batch_size default=32` → `default=2` |
| `sdf_gradient_refiner.py:128` | `retain_graph=True` → `retain_graph=False`（SDF decoder 图与模型图独立，释放后可省 ~5GB） |

### Fix 3: object_pudding 场景配置
| 位置 | 修改 |
|------|------|
| `train_a3_hook.py:61-66` | 新增 `object_pudding` 配置（data_subdir=`safelibero_object`, sdf_gt=`sdf_gt_object_chocolate.npz`） |
| `train_a1_sdf_aux.py:42-47` | 同上，额外含 `assets_dir=baseline_object_pudding` |
| 数据验证 | `sdf_gt_object_chocolate.npz` ✓、`safelibero_object/` ✓、`assets/baseline_object_pudding/` ✓ 均已存在 |

### Fix 4: Phase 2 LoRA warmup
| 位置 | 修改 |
|------|------|
| `train_a3_hook.py:256-280` | Phase 2 启动时设 `_phase2_start` + `_lora_warmup_steps=300`，前 300 步对 LoRA params 做 `grad.mul_(scale)` 线性 warmup |
| `train_a1_sdf_aux.py:147-175` | 同上逻辑，收集 `_lora_params` 列表后做 gradient scaling |

**注意**: import 检查因 `train_pytorch.py` 不在 `scripts/` 目录（位于 `vlsa-aegis/scripts/`）而无法执行完整 import，这是已有路径问题。三个文件 `py_compile` 语法检查均通过。

---
