# code steering script 107

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_steering-script-107_20260522T081012_result.json`
- **Structured JSON:** [`a8f713e628cd54f6911d.json`](../../sessions/a8/a8f713e628cd54f6911d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个模型的 dry-run 全部通过。

**汇报：**

| | Qwen3-8B | Llama-3.1-8B-Instruct |
|---|---|---|
| 脚本路径 | `/root/clkc_mech_interp/src/steering_experiment.py` | 同左 |
| Peak layer | **24** (EN→EN, auto-detected) | **28** (EN→EN, auto-detected) |
| Probe accuracy | 0.7500 | 0.7757 |
| Steering dim | 4096 | 4096 |
| Conflict test samples | 84 | 136 |
| Orthogonality check | dot=0.000000 | dot=0.000000 |

**正式运行命令（等 GPU 分配后执行）：**
```bash
# Qwen3
python src/steering_experiment.py --model /root/models/Qwen3-8B/ --data_dir data/qwen3 --output_dir artifacts/steering

# Llama
python src/steering_experiment.py --model /root/models/Llama-3.1-8B-Instruct/ --data_dir data/llama31 --output_dir artifacts/steering
```

**设计要点：**
- Probe 权重经 StandardScaler 逆变换映射回原始激活空间（`w_orig = w_scaled / scaler.scale_`），确保 steering 方向几何正确
- 对照组用 Gram-Schmidt 生成的正交随机向量，排除非特异性扰动
- 正负 alpha 双向扫描：+α 推向 conflict 方向，-α 推向 no_conflict 方向
- 记录方向性 flip（parametric→contextual / contextual→parametric）用于因果性分析
- Fisher exact test 对比 steering vs control 的 flip rate 统计显著性

---
