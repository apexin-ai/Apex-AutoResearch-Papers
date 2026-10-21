# code exp qwen25 32b fewnerd train

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_qwen25_32b_fewnerd_train_20260519T093136_result.json`
- **Structured JSON:** [`bbe31ba7a346adcfb326.json`](../../sessions/bb/bbe31ba7a346adcfb326.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 GPU 全部在跑，显存 25.6-26.3GB / 32GB，利用率 79-100%。

**训练状态总结**:

| 项目 | 值 |
|---|---|
| 实验 | exp_qwen25_32b_fewnerd |
| 模型 | Qwen2.5-32B-Instruct |
| 方法 | QLoRA 4-bit nf4 (rank=32, alpha=64, all linear) |
| 数据 | FewNERD 131,767 train / 18,824 dev |
| GPU | 4× RTX 5090, ~26GB/32GB used |
| 总步数 | 41,180 steps (5 epochs) |
| 速度 | ~2.5s/step |
| 预计时长 | ~28h |
| 日志 | `/root/autodl-tmp/struct_self_consist_ie/logs/train_qwen25_32b_fewnerd_s42.log` |
| 输出 | `checkpoints/qwen25-32b-fewnerd-qlora-s42` |
| Registry | RUNNING |

训练后续 pipeline（N=8 inference → signal computation → entity construction）等训练完成后再触发。

---
