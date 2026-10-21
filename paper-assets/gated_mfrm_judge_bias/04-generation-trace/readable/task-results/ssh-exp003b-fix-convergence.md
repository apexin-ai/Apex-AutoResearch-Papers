# ssh exp003b fix convergence

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_exp003b_fix_convergence_20260522T173321_result.json`
- **Structured JSON:** [`0c78239515c3229dbec1.json`](../../sessions/0c/0c78239515c3229dbec1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修改完成，验证通过。

## 结果

### Diff 摘要
- **删除**: `from lib.priors import reg_horseshoe_prior_cn` import
- **删除**: `_gmfrm_model` 中的 `reg_horseshoe_prior_cn(N)` 调用（4 个潜变量: `tau_c`, `lambda_c`, `c_slab`, `c_raw`）
- **替换为**: `c_n = numpyro.sample("c_n", dist.HalfNormal(jnp.ones(N) * 1.0))` （1 个潜变量）
- **docstring** 同步更新
- **import 验证**: `from models import *` → OK
- **备份**: `models_horseshoe.py`

### Warmup
`run_exp003.py` 已支持 `--warmup` CLI 参数（默认 2000），exp-003b 运行时传 `--warmup 4000` 即可，无需改代码。

### 预估重跑时间
- exp-003 原始: mfrm_only 37min, sequential ~60min (含 mfrm_only), joint_gmfrm 未收敛所以时间不可参考
- HalfNormal 只有 1 个潜变量 vs horseshoe 的 N+3 个，采样效率大幅提升
- warmup 翻倍 4000→但 per-step 更快
- **预估 joint_gmfrm**: 40-60min（单 GPU sequential chains）
- **预估全量 exp-003b**: ~2h（raw_average 秒级 + mfrm_only ~37min + sequential ~60min + joint ~50min）

### 运行命令（待批准）
```bash
CUDA_VISIBLE_DEVICES=0 XLA_PYTHON_CLIENT_PREALLOCATE=false \
numpyro.set_host_device_count(1) \
python run_exp003.py \
  --judgment-dir /root/gated_mfrm_judge_bias/exp001/results \
  --exposure-csv /root/gated_mfrm_judge_bias/exp002/results/exposure_scores.csv \
  --output-dir /root/gated_mfrm_judge_bias/exp003/output_003b \
  --warmup 4000 --samples 4000 --chains 4 --target-accept 0.95 \
  --methods joint_gmfrm
```

代码已就绪，等 Director 批准后提交。

---
