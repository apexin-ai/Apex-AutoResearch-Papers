# code mvp gmfrm

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_mvp_gmfrm_20260521T163601_result.json`
- **Structured JSON:** [`97912998b1a1f85bc655.json`](../../sessions/97/97912998b1a1f85bc655.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个文件已创建并通过语法检查：

| 文件 | 内容 |
|------|------|
| `data_gen.py` | 合成数据生成，ρ 控制 e_i-b_i confounding，logit 模型含 c_n·e_i 项 |
| `models.py` | 4 种方法：raw average、标准 MFRM、sequential（MFRM+OLS 残差校正）、joint G-MFRM，NumPyro NUTS 2 chains |
| `evaluate.py` | RMSE、Kendall-τ、多 seed 汇总、折线图、paired t-test |
| `run_mvp.py` | 主脚本，sweep ρ∈{0,0.3,0.6}×10 seeds，输出 CSV/PNG，3 条 Pass/Fail 判定 |

运行方式：`cd artifacts/mvp && python run_mvp.py`。需要 numpyro, jax, arviz, scipy, matplotlib, pandas。

---
