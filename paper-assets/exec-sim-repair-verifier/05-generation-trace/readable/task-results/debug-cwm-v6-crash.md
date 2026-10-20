# debug cwm v6 crash

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_debug_cwm-v6-crash_20260512T191144_result.json`
- **Structured JSON:** [`84fc3f65731680be3b98.json`](../../sessions/84/84fc3f65731680be3b98.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结论

**CWM v6 没有崩溃。** 进程 PID 83684 正在正常运行。

### 现状
- 进程活跃：RSS 4.9GB 且持续增长，CPU 105%，已运行 4 分 41 秒
- 当前阶段：正在 `preprocess_split()` 中逐条 tokenize **70748 条训练数据**（max_seq_length=2048）
- GPU 显存 0MB：尚未到达模型加载步骤（模型加载在预处理之后）

### 为什么日志只有 4 行
代码执行顺序：
1. Load tokenizer → ✅ 已日志
2. Detect thinking → ✅ 已日志
3. Load JSONL → ✅ 已日志
4. Compute class weights → ✅ 已日志
5. **`preprocess_split(train_raw)` ← 当前卡在这里，70748 条 tokenize 无中间日志**
6. `preprocess_split(val_raw)` → 还没到
7. Load model → 还没到
8. Training → 还没到

`preprocess_split` 用 Python for 循环逐条处理 70K+ 样本，处理完才输出一行 truncation 统计日志。这就是为什么看起来像 "卡死" 了。

### 关于之前的 PID 81312/81785
`/tmp/cwm_v6_dryrun.log` 时间戳 03:04，内容与主日志一致（同样只有 4 行），说明可能是 dryrun 测试的残留。当前运行的 PID 83684 才是正式的 v6。

### 建议
1. **不需要修复** — 等待预处理完成即可，预计再等几分钟
2. 未来可优化：在 `preprocess_split` 中加进度日志（每 10000 条打印一次），避免长时间无输出引起误判
3. 也可以考虑用 `datasets.map()` 替代手写 for 循环，利用多进程加速 tokenization

---
