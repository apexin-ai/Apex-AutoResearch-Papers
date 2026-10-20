# code irt estimation

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_irt_estimation_20260514T002934_result.json`
- **Structured JSON:** [`3fa6bc0473d43d5d27a0.json`](../../sessions/3f/3fa6bc0473d43d5d27a0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本已完成，部署并通过 synthetic validation。总结：

**脚本**: `/root/contamcal-irt-calibration/exp006/run_irt_calibration.py`

**两个模型**:
- **2PL baseline**: 标准 IRT，不区分 contamination
- **4PL+γ**: `P(Y=1) = c + (d-c) * σ(a*(θ - b + γ*τ))`，其中 γ 分离 contamination effect，θ 为 true ability

**数据接口**:
- 自动解析 eval 目录下的 `{model}_d{dosage}_s{seed}/eval_results.json`
- 支持可选的 `--exposure-file` 加载 per-item 暴露分数 τ
- 输出 JSON 含 θ/γ 估计、95% CI、item 参数、calibrated scores

**Synthetic validation 结果**:
- θ recovery: 2PL=0.86, 4PL+γ=0.93（4PL+γ 更好，因为分离了 contamination）
- γ recovery: 0.63（15个样本下合理）
- 无 NaN，收敛稳定

**用法**:
```bash
# 实验数据
python run_irt_calibration.py --eval-dir /path/to/eval_results --output-dir ./irt_output

# 带 exposure scores
python run_irt_calibration.py --eval-dir ... --exposure-file exposure.json --output-dir ...

# 验证
python run_irt_calibration.py --synthetic --output-dir ./test
```

---
