# code phase0b analysis scripts

**redundancy compound sparsity 2** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_phase0b_analysis_scripts_20260512T145330_result.json`
- **Structured JSON:** [`960b0ca824f11654a006.json`](../../sessions/96/960b0ca824f11654a006.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

**`/root/carc/analysis/` 下 4 个脚本已就绪：**

| 脚本 | 功能 | 验证 |
|------|------|------|
| `heatmap_attention.py` (A1) | 从 MVP results JSON 提取 per-layer 指标，生成 heatmap + line curves | `--help` ✓, 实际跑 ✓ (8 张图已输出到 output/) |
| `attn_vs_ema.py` (A2) | 加载模型，同时捕获 attention weights 和 EMA scores，计算 Pearson/Spearman correlation，可选 kvpress baseline | `--help` ✓, import ✓ |
| `tau_sweep.py` (A3) | Sweep γ∈[0.3..0.99]，每个 γ 跑 chunked forward + eviction 测 PPL，输出 γ-PPL 曲线 | `--help` ✓, import ✓ |
| `decay_curve.py` (A4) | 长序列 chunked forward 中记录 EMA scores 随 position 的变化，输出 decay curves + positional heatmap | `--help` ✓, import ✓ |

A2/A3/A4 需要 GPU 实际运行，未执行（按要求只验证 --help 和 import）。运行示例：
```bash
CUDA_VISIBLE_DEVICES=2 python analysis/attn_vs_ema.py --num-samples 3 --seq-len 2048
CUDA_VISIBLE_DEVICES=2 python analysis/tau_sweep.py --num-samples 2 --seq-len 4096
CUDA_VISIBLE_DEVICES=2 python analysis/decay_curve.py --seq-len 8192
```

---
