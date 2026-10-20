# fix carr fullft k4 fp16

**Does Reward Curation Kill Diversity? Systematic Evidence of Surprising Resilience in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_carr_fullft_k4_fp16_20260516T165400_result.json`
- **Structured JSON:** [`83b12f05470101e33787.json`](../../sessions/83/83b12f05470101e33787.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

进程 514162 存活。日志未更新是因为 Python 输出缓冲——Generation 阶段需要对 2000 个 prompt 生成 4 个候选（125 批次推理），需要一段时间。关键的 bf16 训练步骤要等 Generation 完成后才会执行。

**完成情况总结：**

1. **修复已应用** — `train_sft.py` 中：
   - 模型加载：Full-FT 用 `torch.bfloat16`，LoRA 保持 `torch.float16`
   - TrainingArguments：`fp16=use_lora, bf16=not use_lora`
   
2. **失败输出已清理** — `outputs_fullft_k4/gen_0/` 已删除

3. **实验已提交** — `carr_fullft_k4_probe_02` (PID 514162) 正在 GPU 1 上运行，当前处于 Gen 0 的候选生成阶段

训练步骤（真正验证 bf16 修复的时刻）预计在生成阶段完成后约 10-20 分钟触达。建议稍后 `tail` 日志确认通过了训练第 1 步无报错。

---
