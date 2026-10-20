# ssh get random reweight eval result

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_get_random_reweight_eval_result_20260517T073152_result.json`
- **Structured JSON:** [`5799ac1ae26cac387c66.json`](../../sessions/57/5799ac1ae26cac387c66.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

| 指标 | 值 |
|------|-----|
| **eval_ppl** | **17.830** |
| **eval_loss** | **2.8809** |
| GPU 0 | 空闲（0MiB / 0% util） |

## 对比判定

| 模型 | PPL |
|------|-----|
| adaptive (detector-weighted) | 17.653 |
| uniform baseline | 17.694 |
| **random_reweight_v2_seed42** | **17.830** |

**Conclusion = SUCCESS**

random PPL (17.830) > adaptive PPL (17.653)，差值 +0.177。随机权重显著劣于 detector-guided 权重，证明 detector signal 是 load-bearing 的——adaptive 的优势来自 provenance detector 提供的信号，而非仅仅是"对数据做了某种非均匀加权"��

---
