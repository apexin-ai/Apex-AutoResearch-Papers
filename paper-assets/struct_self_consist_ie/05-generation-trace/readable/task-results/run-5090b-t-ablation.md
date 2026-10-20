# run 5090b t ablation

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_run_5090b_t_ablation_20260520T223630_result.json`
- **Structured JSON:** [`b3dac1954a45a0ce27a4.json`](../../sessions/b3/b3dac1954a45a0ce27a4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个实验全部正常运行：

| GPU | 实验 | 显存 | 状态 |
|-----|------|------|------|
| cuda:0 | FewNERD T=0.5 | 30234/32607 MiB | 推理中，正在处理 301184 prompts |
| cuda:1 | FewNERD T=0.8 | 30232/32607 MiB | 推理中 |
| cuda:2 | FewNERD T=1.2 | 30240/32607 MiB | 推理中 |
| cuda:3 | CoNLL T=0.5 | 30226/32607 MiB | 推理中，~10% (2768/27624)，~6700 tok/s |

**配置汇总**：
- 模型：FewNERD 用 `qwen3-8b-fewnerd-exp021-merged`，CoNLL 用 `qwen3-8b-conll2003-merged`
- 脚本：`code/run_mvp_pilot.py`，N=8，seed=42，`--collect_logprobs`
- tmux sessions：`fewnerd_t05`, `fewnerd_t08`, `fewnerd_t12`, `conll_t05`
- Registry：4 个实验均注册为 RUNNING（`exp_fewnerd_t05_s42`, `exp_fewnerd_t08_s42`, `exp_fewnerd_t12_s42`, `exp_conll_t05_s42`）

FewNERD 37648 instances × 8 samples 预计每个温度跑 2-4 小时，CoNLL 3453 instances 预计 30-60 分钟完成。

---
