# code exp qwen25 7b fewnerd v2

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_qwen25_7b_fewnerd_v2_20260519T112331_result.json`
- **Structured JSON:** [`7cc3ed7bee95aa471b8d.json`](../../sessions/7c/7cc3ed7bee95aa471b8d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

现状与任务描述有几处不符，汇报如下：

### GPU 状态
**所有 4 张 GPU 都被占用。** 一个 Qwen2.5-32B-Instruct FewNERD QLoRA 训练正在使用全部 4 张 GPU（PID 804665-804668，PPID 804590，已运行约 1h50m）。cuda:2,3 不空闲。

### 模型
**Qwen2.5-7B-Instruct 未在服务器上找到。** 当前可用模型：
- Qwen2.5-32B-Instruct: `/root/autodl-tmp/.hf_cache/models--Qwen--Qwen2.5-32B-Instruct/...`
- Qwen3-8B: `/root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B`
- Qwen3-4B: `/root/autodl-tmp/models/Qwen3-4B`

现有 WNUT-17 配置用的是 **Qwen3-8B**，不是 Qwen2.5-7B。

### 32B 训练配置（当前在跑）
已经在用完全相同的参数（QLoRA 4-bit, rank=32, alpha=64, 5 epochs, lr=2e-4）在 FewNERD 上训练 Qwen2.5-32B。

---

**需要你确认：**
1. 32B 训练占满了全部 GPU，是否等它结束再启动 7B？
2. Qwen2.5-7B-Instruct 需要先下载，还是改用已有的 Qwen3-8B？
3. 32B 已经在跑 FewNERD 了，7B 实验的目的是做模型大小对比吗？

---
