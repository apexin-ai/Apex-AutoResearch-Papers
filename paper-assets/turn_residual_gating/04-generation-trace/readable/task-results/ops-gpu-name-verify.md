# ops gpu name verify

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu_name_verify_20260524T124648_result.json`
- **Structured JSON:** [`f714dae0e9058f8e1bf3.json`](../../sessions/f7/f714dae0e9058f8e1bf3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**结果：**

- **nvidia-smi 实际输出**: NVIDIA RTX PRO 6000 Blackwell Server Edition, 97887 MiB (~95.6 GB)
- **论文描述**: NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (102 GB)
- **差异**: GPU 名称一致，但**显存不一致**。实际为 97887 MiB ≈ 95.6 GB，论文写的 102 GB。可能是论文误用了营销规格（96 GB GDDR7）并四舍五入到了 102，或混淆了其他型号。建议修正为 **96 GB**（厂商标称值）。

---
