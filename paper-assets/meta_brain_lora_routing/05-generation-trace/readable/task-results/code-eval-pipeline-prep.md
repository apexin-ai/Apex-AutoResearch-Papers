# code eval pipeline prep

**Meta-Brain: Perturbation-Diagnostic Routing of LoRA Experts for Parameter-E cient VLA Robustness** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_eval_pipeline_prep_20260516T200439_result.json`
- **Structured JSON:** [`37522bb5b52c23990931.json`](../../sessions/37/37522bb5b52c23990931.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

eval 已完成，结果清晰。以下是完整汇报。

---

## 汇报

### 1. Eval 失败根因

**`jaxtyping.TypeCheckError`** — openpi 官方 `libero_policy.py` 用 `np.True_`（`numpy.bool_` 标量）作为 `image_mask`，但服务器上的 `jaxtyping 0.2.36 + beartype 0.22.9` 严格检查要求 `Bool[ndarray, '*b']`，不接受 numpy 标量。

错误链：`Observation.__init__` → `@at.typecheck` → `_check_dataclass_annotations` → TypeCheckError。

**不是 LIBERO-Plus 环境问题，是 jaxtyping 版本兼容性问题。**

### 2. LIBERO 安装现状

| 项目 | 状态 |
|------|------|
| LIBERO-Plus | editable install from `/root/LIBERO-plus/`，`.pth` 指向该目录 |
| `import libero` | 加载 LIBERO-Plus |
| 原版 nominal tasks | LIBERO-Plus **包含**原版 tasks（spatial 9, object/goal/10 各 10） |
| init_states | 每 suite 10 个，齐全 |
| **结论** | **不需要单独安装原版 LIBERO** |

### 3. 已执行的修复

在 3 个脚本入口添加 `jaxtyping_disable = True`：
- `phase1/eval_base_no_lora.py`
- `phase1/evaluate_libero_plus.py`
- `phase1/openpi_metabrain_policy.py`

Smoke test 通过：actions shape=(50,7), range 正常。

### 4. Nominal eval baseline 结果

`eval_base_no_lora.py` 已在 GPU 1 上完成 libero_spatial nominal eval：

```
Success rate: 6/10 = 60.0%

Ep0: FAIL (220 steps) — pick up the black bowl between the plate and the ramekin...
Ep1: PASS (137 steps) — pick up the black bowl in the top drawer...
Ep2: FAIL (220 steps) — pick up the black bowl next to the cookie box...
Ep3: PASS (92 steps)  — pick up the black bowl next to the plate...
Ep4: FAIL (220 steps) — pick up the black bowl next to the ramekin...
Ep5: PASS (84 steps)  — pick up the black bowl on the cookie box...
Ep6: FAIL (220 steps) — pick up the black bowl on the ramekin...
Ep7: PASS (180 steps) — pick up the black bowl on the stove...
Ep8: PASS (113 steps) — pick up the black bowl on the wooden cabinet...
Ep9: PASS (75 steps)  — pick up the black bowl between the plate and the ramekin...
```

### 5. 建议的 nominal eval 命令（evaluate_libero_plus.py）

```bash
cd /root/meta_brain_lora_routing && \
CUDA_VISIBLE_DEVICES=2 MUJOCO_GL=egl python phase1/evaluate_libero_plus.py \
    --routing none --perturbation_types nominal \
    --task_suite libero_spatial --num_episodes 10 \
    --pi0_checkpoint /root/autodl-tmp/checkpoints/pi0_libero \
    --policy_type openpi --gpu 0
```

### 6. Eval pipeline 状态：**已就绪**

- jaxtyping bug 已修复
- LIBERO-Plus 覆盖 nominal tasks
- Checkpoint/init_states 完备
- GPU 2-3 空闲可用
- v3 visual LoRA 仍在 GPU 0 训练中

---
