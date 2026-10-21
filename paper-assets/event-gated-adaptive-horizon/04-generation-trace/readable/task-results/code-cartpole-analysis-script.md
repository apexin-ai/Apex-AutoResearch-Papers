# code cartpole analysis script

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_cartpole-analysis-script_20260524T230726_result.json`
- **Structured JSON:** [`3d7097d24b9ac698a0d1.json`](../../sessions/3d/3d7097d24b9ac698a0d1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本已写入 `artifacts/scripts/cartpole_analysis.py`。

**核心逻辑**：
- 从 metrics.jsonl 提取 `value_mean`（训练指标行）和 `eval_return`（评估行），按 step 匹配
- `ve_ratio = value_mean / eval_return`
- `NVE = ve_ratio(treatment) / ve_ratio(baseline_mean)`，跨 seed 对齐到公共 step
- CIVO 判定：peak NVE > 1.5x

**三张图**：
1. ve_ratio 时间线（3 组实验，mean ± shade）
2. NVE 柱状图（peak + final，含 error bars 和 1.5x 阈值线）
3. eval_return 学习曲线

**两种用法**：
```bash
# 自动发现（同一服务器）
python cartpole_analysis.py --logdir-base /root/autodl-tmp/event-gated-adaptive-horizon/logdir/

# 手动指定（跨服务器数据合并后）
python cartpole_analysis.py \
  --exp060 logdir/exp_060_cartpole_baseline_s{0,1,2} \
  --exp061 logdir/exp_061_cartpole_civo_trigger_s{0,1,2} \
  --exp062 logdir/exp_062_cartpole_control_s{0,1,2}
```

字段名已验证与服务器上 metrics.jsonl 实际输出一致（`eval_return`, `value_mean`, `train_return`）。不硬编码 obs/action 维度，纯 metrics.jsonl 解析，无需 torch。

---
