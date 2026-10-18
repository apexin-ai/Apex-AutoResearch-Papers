# code eval scripts prep

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_eval_scripts_prep_20260516T103229_result.json`
- **Structured JSON:** [`4dfc435a28c88af137f2.json`](../../sessions/4d/4dfc435a28c88af137f2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个脚本已部署并验证：

**`eval_success_rate.py`** — closed-loop rollout 评估
- 参数：`--checkpoint_path`, `--config_path`, `--mode`, `--num_episodes`(50), `--max_steps`(400), `--action_horizon`(50), `--seed`, `--gpu`, `--output`
- 使用 `policy.model.sample_actions()` 做 flow matching ODE 推理
- 每个 episode 打印 success/fail + steps + reward + wall clock 时间
- 汇总输出 success rate + 95% Wilson CI + mean episode length
- 支持 baseline/acis_prune/bypass 三种模式
- 结果保存为 JSON

**`test_mode_collapse.py`** — action diversity 快速诊断
- 两个测试：
  1. **Cross-obs**: 不同 obs → 不同 actions？（batch 内 std）
  2. **Same-obs noise diversity**: 同一 obs 不同 noise → 不同 actions？（直接测 ODE 是否 collapse）
- 判定标准：noise std > 0.05 → PASS，< 0.01 → FAIL
- 可选 `--pretrained_path` 与原始预训练模型对比

运行示例：
```bash
# baseline_v6_alpha16 训练完成后
python eval_success_rate.py \
    --checkpoint_path checkpoints/baseline_v6_alpha16/latest/checkpoint.pt \
    --config_path configs/baseline_v6_alpha16.yaml \
    --mode baseline --num_episodes 50

python test_mode_collapse.py \
    --checkpoint_path checkpoints/baseline_v6_alpha16/latest/checkpoint.pt \
    --config_path configs/baseline_v6_alpha16.yaml \
    --pretrained_path /root/autodl-tmp/.hf_cache/lerobot/smolvla_base
```

---
