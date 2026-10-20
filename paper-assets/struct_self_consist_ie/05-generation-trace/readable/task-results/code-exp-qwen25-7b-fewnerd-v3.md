# code exp qwen25 7b fewnerd v3

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_qwen25_7b_fewnerd_v3_20260519T112555_result.json`
- **Structured JSON:** [`fd5ffa769c875951cbde.json`](../../sessions/fd/fd5ffa769c875951cbde.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练正常运行。

**汇总：**

| 项目 | 值 |
|---|---|
| Server | autodl-5090-c, cuda:2,3 |
| Model | Qwen2.5-7B-Instruct (base) |
| Data | FewNERD 131,767 train / 18,824 dev |
| Config | QLoRA 4-bit nf4, rank=32, alpha=64, lr=2e-4, 5 epochs |
| Effective batch | 32 (2 GPU × 2 batch × 8 accum) |
| Total steps | 20,590 (~2.3s/step → 预计 ~13h) |
| Trainable params | 80.7M / 7.7B (1.05%) |
| Pipeline | train → merge → 3-seed N=8 inference → signal analysis → entity construction |
| Log | `logs/pipeline_qwen25_7b_fewnerd.log` |
| Registry | `exp_qwen25_7b_fewnerd` → RUNNING |

创建的文件:
- `train_config_qwen25_7b_fewnerd_s42.yaml`
- `export_config_qwen25_7b_fewnerd.yaml`
- `run_fewnerd_qwen25_7b_pipeline.sh` (5-phase pipeline，训练完成后自动执行 merge → inference → analysis → entity construction)

---
