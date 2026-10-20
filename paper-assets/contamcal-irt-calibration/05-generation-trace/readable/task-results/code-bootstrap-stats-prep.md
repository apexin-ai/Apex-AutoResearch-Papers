# code bootstrap stats prep

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_bootstrap-stats-prep_20260519T160607_result.json`
- **Structured JSON:** [`0829fd27788ce2eee713.json`](../../sessions/08/0829fd27788ce2eee713.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本已完成，部署在两个位置：

**本地**: `artifacts/bootstrap_profile_stability.py`
**cqa1**: `/root/contamcal-irt-calibration/analysis/bootstrap_profile_stability.py`

**运行方式**（cqa1 eval 全部完成后）：

```bash
# westd s42 全量 5-model 分析
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
python /root/contamcal-irt-calibration/analysis/bootstrap_profile_stability.py \
    --data-dir /root/autodl-tmp/exp001/eval_results_v2/ \
    --benchmark mmlu --n-bootstrap 10000 \
    --output-dir /root/contamcal-irt-calibration/analysis/results/

# cqa1 s123 单模型（等 d100_s123 eval 完成后）
python bootstrap_profile_stability.py \
    --data-dir /root/autodl-tmp/exp001/eval_results_v2/ \
    --seed-suffix _s123 --models qwen7b \
    --output-dir /root/contamcal-irt-calibration/analysis/results/
```

**当前状态**: cqa1 上 `qwen7b_d100_s123` 目录为空（eval 未完成），其余 d000-d050 数据就绪。westd 上全部 25 个 model×dosage 数据完整。

**脚本关键设计**:
- **Paired bootstrap**: 同一组 item indices 用于所有模型和 dosage，保留 cross-model 相关性
- **Vectorized classification**: numpy 向量化 pattern 分类，避免 Python 循环
- **两种数据源**: 优先读 `correctness_matrix.json`（紧凑），fallback `item_responses.json`
- **Threshold CI**: 线性插值找 benefit/harm 分界点，对每次 bootstrap 计算 crossing
- **输出**: JSON 结果 + 2 张 PNG（delta 分布 + dose-response CI bands）

---
