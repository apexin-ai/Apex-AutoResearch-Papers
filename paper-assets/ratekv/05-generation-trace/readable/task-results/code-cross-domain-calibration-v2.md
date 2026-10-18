# code cross domain calibration v2

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_cross_domain_calibration_v2_20260514T101754_result.json`
- **Structured JSON:** [`7b085563582aff5e506f.json`](../../sessions/7b/7b085563582aff5e506f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本已创建并验证通过。

**脚本路径**: `/root/ratekv/run_cross_domain_v2.py`

**额外依赖**: 无。torch, transformers, datasets 已预装。

**启动命令**:
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/ratekv

# 跑全部 3 个模型（GPU 0）
nohup python run_cross_domain_v2.py --gpu 0 > cross_domain_v2.log 2>&1 &

# 或只跑单个模型
python run_cross_domain_v2.py --gpu 0 --models qwen2.5-7b
```

**预计运行时间**:

| 模型 | Heads | Profiling (2方向) | Eval | 小计 |
|------|-------|-------------------|------|------|
| Qwen2.5-7B | 28×4=112 | ~2×2.5h | ~20min | ~5.5h |
| Llama-3.1-8B | 32×8=256 | ~2×6h | ~30min | ~13h |
| Mistral-7B-v0.3 | 32×8=256 | ~2×6h | ~30min | ~13h |
| **合计** | | | | **~31h** |

（基于 Qwen 在 `run_c4_rerun.py` 中 112 heads × 3 bitwidths profiling 约 2.5h 估算，Llama/Mistral heads 数是 Qwen 的 2.3 倍）

**产出文件**:
- `cross_domain_v2_results.json` — 合并结果（含 summary 表 + 每模型详细 allocation）
- `cross_domain_v2_{model}_profiles.json` — 每模型的原始 per-head distortion profiles

---
