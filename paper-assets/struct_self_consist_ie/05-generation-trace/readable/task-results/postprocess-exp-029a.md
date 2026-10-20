# postprocess exp 029a

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_postprocess_exp_029a_20260518T004320_result.json`
- **Structured JSON:** [`4e816f679c99f8f3bb0a.json`](../../sessions/4e/4e816f679c99f8f3bb0a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**exp_029a 状态：训练在 step 100/351 崩溃（磁盘满）**

详情：
- 崩溃点：step 100/351（epoch 0.86），eval_loss=0.1076
- 错误：保存 checkpoint-100 时 `RuntimeError: basic_ios::clear: iostream error`（optimizer.pt 写入失败）
- 根因：磁盘 100%（250G/250G，剩余 64K）
- checkpoint-100 的 adapter 权重已保存（349MB），但 optimizer.pt 被截断（仅 12MB）

**磁盘分布：**
| 目录 | 大小 |
|------|------|
| checkpoints/ | 199G |
| .hf_cache/ (base models) | 38G |
| output/ | 5.8G |
| data/ | 0.4G |

**清理方案：** 删除已完成推理的 merged 模型（均可从 LoRA + base model 重建）：

| 模型 | 大小 | 对应推理输出 |
|------|------|------------|
| qwen3-8b-fewnerd-merged | 16G | exp_021 已有 |
| llama3.1-8b-conll2003-merged | 15G | exp_017 已有 |
| llama3.1-8b-scierc-merged | 15G | exp_018 已有 |
| llama3.2-3b-scierc-merged | 6.1G | 早期实验 |
| qwen3-4b-conll2003-merged-ckpt4200 | 7.6G | 重复变体 |

共释放 ~60G，足够重跑训练+merge+inference。

是否执行清理并重启训练？

---
