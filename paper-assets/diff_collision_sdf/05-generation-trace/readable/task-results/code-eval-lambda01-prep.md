# code eval lambda01 prep

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_eval_lambda01_prep_20260526T160258_result.json`
- **Structured JSON:** [`b8ba637a98016dbdbab6.json`](../../sessions/b8/b8ba637a98016dbdbab6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。8 轮 SSH 已用完。汇总：

### 验证结果

| 检查项 | 状态 |
|--------|------|
| 180° 旋转修复 (`[::-1, ::-1]`) | ✅ 两台服务器 L841/843 |
| 256×256 分辨率 | ✅ L903-904 |
| `--seed 7` 支持 | ✅ L531, default=0 |
| `max_ee_displacement` per episode | ✅ L1068 |
| `total_ee_path_length` per episode | ✅ L1071 |
| `collided` per episode | ✅ L1064 |
| per-task TSR/CAR 分组 | ✅ `results` 列表每个元素为一个 task 的汇总 |
| `--model_type a1` | ✅ 确认用 a1 |
| `--gpu` 参数 | ✅ L532 |
| `--pi05` flag | ✅ L571 |

### Checkpoint 路径（已确认存在 /30000）

| Seed | 服务器 | 路径 |
|------|--------|------|
| s0 | westd-35807 | `.../a1_sdf_pi05_object_pudding_seed0_l01/30000` |
| s1 | westd-35807 | `.../a1_sdf_pi05_object_pudding_seed1_l01/30000` |
| s2 | westd-45947 | `.../a1_sdf_pi05_object_pudding_seed2_l01/30000` |

注意：路径是 `_l01` 而非任务中假设的 `_l01_high`。

### 已创建脚本

| 脚本 | 服务器 | 路径 |
|------|--------|------|
| s0+s1 eval | westd-35807 | `/root/colliforce-vla/scripts/eval_lambda01_all_seeds.sh` |
| s2 eval | westd-45947 | `/root/colliforce-vla/scripts/eval_lambda01_s2.sh` |
| 约束检查 | 两台 | `/root/colliforce-vla/scripts/check_eval_constraints.py` |

### 运行方式

训练完成后（预计 5/27 17:05-17:50 UTC）：
```bash
# westd-35807 (conda activate libero)
bash scripts/eval_lambda01_all_seeds.sh <空闲GPU>

# westd-45947 (conda activate base)
bash scripts/eval_lambda01_s2.sh <空闲GPU>

# 结果检查
python scripts/check_eval_constraints.py &lt;eval_result.json>
```

---
