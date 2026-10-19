# ops westd 34887 collect and fill

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd-34887-collect-and-fill_20260518T064648_result.json`
- **Structured JSON:** [`fca2ad66fce0b542704b.json`](../../sessions/fc/fca2ad66fce0b542704b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两张 GPU 满载运行。

## 总结

**已完成实验**:
- **kl50_s123_uniform_eval** → DONE (success): PPL 11.89 (比 global_topk 好)，但 downstream 全面崩溃 (ARC-C -5.6pp, WG -6.7pp, MMLU -8.2pp, GSM8K -5pp)。验证了 global_topk 分配对下游任务的关键作用。
- **kl50_s456_train** → DONE (success): 1000/1000 steps, loss=0.397, sparsity=0.492

**已提交新实验**:
| GPU | 实验 | 说明 |
|-----|------|------|
| cuda:0 | c4_ood_kl50_s123 | KL 50% sparsity C4 OOD PPL，补充 sparsity-OOD 曲线 (30% 数据在 westd-41718 跑) |
| cuda:1 | kl50_s456_eval | 50% sparsity seed 456 full benchmark eval，多 seed 一致性 |

注意：PREPARING 队列中无可直接提交的实验（全部 killed/negative/failed），cuda:0 改为提交 C4 OOD eval 填充。

---
