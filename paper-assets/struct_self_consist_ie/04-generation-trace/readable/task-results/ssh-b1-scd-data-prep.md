# ssh b1 scd data prep

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_b1-scd-data-prep_20260520T095449_result.json`
- **Structured JSON:** [`ad6ab56f5482d5d80cf7.json`](../../sessions/ad/ad6ab56f5482d5d80cf7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

B1 SCD 数据准备完成。产出汇总：

### 服务器: autodl-5090-b

**生成的伪标签数据** (`/root/autodl-tmp/struct_self_consist_ie/data/scd/`):

| Dataset | 伪标签实例 | Gold训练 | SCD混合 | ST混合 | Construction方法 |
|---------|-----------|---------|---------|--------|-----------------|
| FewNERD | 32,565 | 131,767 | 65,130 | 65,130 | theta2n (pre-F1: 0.748→0.764) |
| SciERC | 529 | 1,861 | 1,058 | 1,058 | theta2n (pre-F1: 0.645→0.649) |
| CoNLL | 2,756 | 14,041 | 5,512 | 5,512 | lp_weighted (pre-F1: 0.907→0.903) |

**训练 YAML 配置** (6个, 项目根目录):
- `train_config_scd_{fewnerd,scierc,conll}_s42.yaml` — SCD 训练
- `train_config_st_{fewnerd,scierc,conll}_s42.yaml` — Self-training baseline
- 共用参数: LoRA rank=32, alpha=64, lr=1e-4, batch=16 effective
- 基于各数据集的 merged FT checkpoint 继续训练

**Export 配置** (6个): `export_config_{scd,st}_{fewnerd,scierc,conll}.yaml`

**评估脚本**: `/root/autodl-tmp/struct_self_consist_ie/code/eval_scd.py`
- 输出 4 指标: 训前/训后 × greedy/construction F1
- 含 paired bootstrap significance test

**待做** (非本 Worker 任务):
1. 安装 LLaMA-Factory
2. GPU 训练 (优先 FewNERD SCD → 收益最大)
3. 训后 merge → N=8 inference → eval_scd.py 评估

---
