# code design exp002v3 r1 scaling

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_design-exp002v3-r1-scaling_20260519T072509_result.json`
- **Structured JSON:** [`5fe2056129a9e9426a1b.json`](../../sessions/5f/5fe2056129a9e9426a1b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

exp-002v2 run script 不含 `r1_scale_factor`，会使用默认值 1.0，不受影响。

## 修改摘要

**Trainer 改动** (`/root/mvp_v2_1_expanded/training/dcgrpo_trainer.py`)：
- `DCGRPOConfig` 新增 `r1_scale_factor: float = 1.0`（line 130）
- `__init__` 新增 `self._r1_scale_factor = args.r1_scale_factor`（line 271）
- `compute_r1` 返回值改为 `self._r1_scale_factor * sum(scores) / len(scores)`（line 674）
- 默认值 1.0 确保现有实验（exp-002v2 等）行为不变

**Run script 配置** (`run_exp002v3_dcgrpo_scaled_cosine.py`)：
- `R1_SCALE_FACTOR = 5.0`（cosine ~[-0.2,+0.2] → ~[-1,+1]）
- `R1_WEIGHT = 0.5, R3_WEIGHT = 0.5`（对等贡献）
- `R2_WEIGHT = 0.0`
- `lora_alpha = 128`（vs v2 的 64）
- `DIRECTION_PATH = results/exp001/directions.pt`
- 从头训练（无 resume_from_checkpoint）
- 其余配置与 v2 一致

**R1 计算公式**：
```
R1 = 5.0 * sign * mean(cosine(h, d_syc))   # sign=+1 valid, -1 invalid
```

## Dry-run 结果
**PASS** — py_compile、DCGRPOConfig 实例化、compute_r1 scale factor 验证均通过。

## 文件路径
| 位置 | 路径 |
|---|---|
| 远程 run script | `/root/contrastive_entrain_calib/training/run_exp002v3_dcgrpo_scaled_cosine.py` |
| 远程 trainer | `/root/mvp_v2_1_expanded/training/dcgrpo_trainer.py` |
| 远程 trainer 备份 | `/root/mvp_v2_1_expanded/training/dcgrpo_trainer.py.bak_pre_v3` |
| 本地 run script | `artifacts/training/run_exp002v3_dcgrpo_scaled_cosine.py` |
| 本地 trainer | `artifacts/training/dcgrpo_trainer.py` |

---
