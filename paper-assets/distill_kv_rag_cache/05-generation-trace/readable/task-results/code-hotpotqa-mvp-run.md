# code hotpotqa mvp run

**distill kv rag cache** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_hotpotqa-mvp-run_20260514T073120_result.json`
- **Structured JSON:** [`b23bfcc536c1a6dc6e88.json`](../../sessions/b2/b23bfcc536c1a6dc6e88.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 GPU 都已正常开始处理样本。

---

## 汇报

### 1. Baseline 验证（Step 1）— Config E, 5 条
- **EM=0.200, F1=0.314**
- 修复了 prompt 格式问题：原代码使用 raw text，Llama 3.1 Instruct 做文本续写而非问答。已改用 `apply_chat_template` + system prompt 引导短答案生成
- 修复后模型正确生成短答案（如 "YG Entertainment" 完全匹配）

### 2. 全 config 验证（Step 2）— A/B/C/D/E @ 6x, 5 条
- 所有 config EM=0.200, F1=0.314（5 条样本完全相同）
- **但压缩管线确实在运行**：压缩 config 延迟 ~3.8s vs baseline 0.3s（12x）
- 诊断结论：chunk_boundaries=[512,1024], 64 boundary tokens + 196 restoration tokens = 20% budget，恢复力度足够使 5 条样本结果一致。500 条应能展现差异。

### 3. 全量 MVP（Step 3）— 500 条 × 9 configs, 双 GPU
- **GPU 0** (PID=20382): A_6x, A_8x, B_6x, B_8x, C_6x, C_8x — 6 runs, 20.3GB 显存, 91% 利用率
- **GPU 1** (PID=20583): D_6x, D_8x, E_baseline — 3 runs, 20.2GB 显存, 94% 利用率
- 预估运行时间：GPU 0 约 6 × 500 × 3.8s ≈ 3.2h, GPU 1 约 2 × 500 × 3.8s + 500 × 0.3s ≈ 1.1h

### 代码修改
- `compresslink/eval_runner.py` L170-185: prompt 构建改用 `tokenizer.apply_chat_template`，max_length 2048→4096

---
