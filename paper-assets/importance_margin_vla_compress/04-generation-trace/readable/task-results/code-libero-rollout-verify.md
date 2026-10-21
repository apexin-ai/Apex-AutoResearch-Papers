# code libero rollout verify

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_libero_rollout_verify_20260516T192250_result.json`
- **Structured JSON:** [`6f3911b404657ac888fd.json`](../../sessions/6f/6f3911b404657ac888fd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**Pipeline 验证完毕，完全 ready。**

## 结果总结

### 状态：✅ READY

Dry-run 成功完成（50K baseline checkpoint，1 episode，~25s 总耗时）：
- 模型加载正常（14s，LoRA rank=32）
- LIBERO sim 环境初始化正常（EGL headless rendering）
- Action prediction → env.step → success detection 全链路通畅
- 结果自动保存到 `eval_results/libero_libero_object.json`

### Rollout 命令模板

100K checkpoint 到了后直接用：

```bash
# Baseline 评估（全 4 个 suite）
cd /root/autodl-tmp/importance_margin_vla_compress
MUJOCO_GL=egl python3 eval_success_rate_libero.py \
    --checkpoint checkpoints/&lt;NEW_CKPT_DIR>/checkpoint.pt \
    --config configs/libero_baseline.yaml \
    --suite libero_object \
    --num_episodes 10 \
    --gpu 0

# IMM two-stage 评估
MUJOCO_GL=egl python3 eval_success_rate_libero.py \
    --checkpoint checkpoints/&lt;IMM_CKPT_DIR>/checkpoint.pt \
    --config configs/libero_imm_twostage.yaml \
    --suite libero_object \
    --num_episodes 10 \
    --mode acis_prune \
    --gpu 0
```

Suites: `libero_spatial`, `libero_object`, `libero_goal`, `libero_10`（每个 10 tasks × 10 eps = 100 episodes）。

### cqa1 → westd SCP 路径

```bash
scp connect.cqa1.seetacloud.com:/root/autodl-tmp/importance_margin_vla_compress/checkpoints/&lt;DIR>/checkpoint.pt \
    /root/autodl-tmp/importance_margin_vla_compress/checkpoints/&lt;DIR>/checkpoint.pt
```

### 注意事项
- 50K checkpoint 的单 episode FAIL 属正常（只跑了 1 个 episode，且 50K 还没训够）
- 整套评估（4 suites × 10 tasks × 10 eps = 400 episodes）预计耗时 ~3-4 小时
- 如需加速可分 GPU 或只跑重点 suite（libero_object 是论文主要报告的）

---
