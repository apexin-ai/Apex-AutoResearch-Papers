# run 5090c conll t ablation

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_run_5090c_conll_t_ablation_20260520T223840_result.json`
- **Structured JSON:** [`373eb7a84d108e565cd3.json`](../../sessions/37/373eb7a84d108e565cd3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 个 CoNLL T-ablation 实验全部启动成功，registry 已更新为 RUNNING。

**汇总：**

| 实验 | GPU | PID | 温度 | Registry ID |
|------|-----|-----|------|-------------|
| T=0.5 | cuda:1 (30GB) | 242197 | 0.5 | `exp_conll_t_ablation_t05` |
| T=0.8 | cuda:2 (30GB) | 242682 | 0.8 | `exp_conll_t_ablation_t08` |
| T=1.2 | cuda:3 (30GB) | 243594 | 1.2 | `exp_conll_t_ablation_t12` |

- cuda:0 未触碰（14B 推理 PID 230885 正常运行，31GB/98%）
- 模型：`qwen3-8b-conll2003-merged`，N=8，seed=42
- 总 prompts：27624（3453 test instances × 8 samples），推理速度 ~5500 toks/s，预计 ~30-50 分钟完成
- 日志路径：`/root/autodl-tmp/struct_self_consist_ie/output/exp_conll_t{05,08,12}_seed42.log`

---
