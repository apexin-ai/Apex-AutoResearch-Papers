# ops cleanup and fix kl

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cleanup-and-fix-kl_20260514T120827_result.json`
- **Structured JSON:** [`245a97b253ab00b8ba26.json`](../../sessions/24/245a97b253ab00b8ba26.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。结果汇总：

### Part 1: GPU 清理
- **cuda:0/2/3**：已空闲（0 MiB），无 GRPO 残留进程（连接时就已经是干净的）
- **cuda:1**：sft_eval 保留，88% 利用率，10454 MiB 占用

### Part 2: KLDivergenceCallback 修改
修改前后 diff：
- ✅ 添加 docstring，说明 QLoRA 4-bit 下 KL 不可靠的原因
- ✅ `control.should_training_stop = True` 已移除（grep 返回空，确认文件中不再有 `should_training_stop`）
- ✅ warning 消息改为 `"monitoring only, not stopping"`

### Part 3: 验证
- 代码修改正确（行 30-44）
- 无早停逻辑残留
- GPU 0/2/3 可用于新训练

---
