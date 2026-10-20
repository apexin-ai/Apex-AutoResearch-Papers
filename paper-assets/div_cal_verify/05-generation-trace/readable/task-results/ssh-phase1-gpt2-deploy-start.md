# ssh phase1 gpt2 deploy start

**The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_phase1-gpt2-deploy-start_20260512T200650_result.json`
- **Structured JSON:** [`532ca0da24d869ff746b.json`](../../sessions/53/532ca0da24d869ff746b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部步骤完成。汇报：

**Patch 结果**：3/3 成功
- PATCH1_OK: `contriever_model is not None` 条件判断 (line 155)
- PATCH2_OK: student model GPT2 用 float32 (line 198)
- PATCH3_OK: generator model GPT2 用 float32 (line 210)

**GPT2 数据准备**（耗时 ~10 分钟）：
- Tokenizer: gpt2, seq_len=512
- Train chunks: 232,588（vs Qwen 的约 200K，GPT2 vocab 小所以 chunks 更多）
- Reference set R: 5,000 chunks
- Rare n-gram positives: 4,952/5,000（99%，分布极端）
- Test chunks: 558

**GPU**：使用 GPU 1（空闲），GPU 0 占用 49GB

**实验 PID**：93696（shell），93704（run_mvp.py RGDS）

**运行确认**：
- GPU 1 利用率 98%，显存 12,225 MiB
- RGDS method 已开始执行
- Python 输出被缓冲，后续会批量输出日志

**磁盘**：/root/autodl-tmp 250GB 总量，已用 9.7GB (4%)，充足

---
