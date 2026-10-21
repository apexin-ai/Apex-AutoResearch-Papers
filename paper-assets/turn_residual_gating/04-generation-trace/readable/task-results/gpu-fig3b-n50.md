# gpu fig3b n50

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_gpu_fig3b_n50_20260524T171525_result.json`
- **Structured JSON:** [`25d1c2cce82037a4948b.json`](../../sessions/25/25d1c2cce82037a4948b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

关键发现：

**Fig 3(b) 当前是 Qwen 数据，不是 Llama SS。** 论文 caption 明确写道：

> (b) Distribution shift ($N$=5 pilot): the TF-AR GAR gap persists across all five variants.

Panel (b) 展示 Qwen 的 5 个变体（Base/TG/PCGrad/UG/LoRA），使用 N=5 pilot 数据。Panel (a) 的 layers 到 L23（24 层 Qwen 模型），也证实是 Qwen 数据。

Llama SS 的数据在 §5.5 cross-model section，当前论文文本引用的值是：TF GAR 0.477, AR GAR 0.166, gap 2.9×。但 `p1_llama_ss_s42` 没有独立的 N=50 eval 结果文件。

**两种可能的意图**：
1. 把 Fig 3(b) 从 Qwen N=5 pilot 更新为 Llama SS N=50 数据
2. 为 cross-model section / appendix 生成 Llama SS 的 N=50 分布偏移数据

要继续执行，需要两步 GPU 评估：
- TF (IID) eval：`--conversations-path standard_conversations.json`，约 10-15 分钟
- AR (model-generated) eval：`--ar-from-fixed`，N=50 conversations 约 30-60 分钟

GPU 当前应该空闲。是否继续运行这两个评估？如果是，请确认你想把结果放在 Fig 3(b)（替换 Qwen pilot data）还是用于 cross-model appendix。

---
