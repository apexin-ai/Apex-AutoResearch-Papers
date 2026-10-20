# merge 32b fewnerd

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_merge_32b_fewnerd_20260521T001425_result.json`
- **Structured JSON:** [`d4178a79094b12e1936c.json`](../../sessions/d4/d4178a79094b12e1936c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

推理运行正常：

- vLLM 加载完成，KV cache 197,712 tokens，最大并发 48.27×
- 37,648 个 FewNERD prompts 正在渲染（~540 it/s）
- 4 张 GPU 各占用 ~31GB，利用率 41-53%

---

**全部任务完成汇总：**

| 步骤 | 状态 | 详情 |
|------|------|------|
| 训练诊断 | **成功** | 41180 steps 完成，best eval_loss=0.0334 @ step 32000，epoch 4-5 过拟合 |
| LoRA merge | **完成** | checkpoint-32000 → `qwen25-32b-fewnerd-merged`（14 shards, ~61GB bf16） |
| Inference 启动 | **运行中** | PID 978386, 4×TP, 37648 instances, N=8, T=1.0, seed=42, logprobs |
| Registry | **已更新** | `exp_qwen25_32b_fewnerd` → DONE; `exp_32b_inference_fewnerd` → RUNNING |
| Cron 清理 | **完成** | `exp_qwen25_32b_fewnerd` cron 已删除 |

磁盘剩余 22GB（250G 盘），推理输出应够用。FewNERD 37648 条 × N=8 估计需要数小时完成。

---
