# code fix s4 oom and submit v9

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-s4-oom-and-submit-v9_20260516T004604_result.json`
- **Structured JSON:** [`e46483a7d1f56d2078f3.json`](../../sessions/e4/e46483a7d1f56d2078f3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

cuda:4 now has only PID 668217 (v9) at 6876 MiB. All v8 residuals cleared.

## 产出总结

### 1. PID 662616 处置
- **已 kill**。运行 v8 unpatched s4_selfcritique on d100_a32_s123 mmlu，816/7021 items 处。内存 7.4 GB 稳定但使用无 OOM 防护的旧代码。

### 2. compute_signals.py 修改 (s4_selfcritique.py)
**分段处理机制**，仅在 items > 2000 且有 output_dir 时激活：
- `CHUNK_SIZE = 1000` — 每 1000 items 为一段
- 每段处理完后保存到 `{output_dir}/_s4_chunks_{benchmark}/chunk_{start}_{end}.json`
- 段间执行 `torch.cuda.empty_cache()` + `gc.collect()` 释放 GPU 显存碎片
- **断点续跑**：已存在的 chunk 文件直接加载跳过，OOM 后重启只需重算当前段
- items ≤ 2000 时行为与原代码完全一致（gsm8k 1319 items / arc 1172 items 不受影响）
- 额外 kill 了两个 v8 残留进程：PID 667203 (gsm8k) 和 PID 667651 (arc_challenge)

### 3. Dry-run 验证
`python -c "import compute_signals; print('IMPORT_OK')"` → IMPORT_OK

### 4. v9 提交结果
- **exp_id**: exp_002_signals_3B_v9
- **PID**: 668217
- **GPU**: cuda:4 (CUDA_VISIBLE_DEVICES=4)
- **tmux session**: exp_002_signals_3B_v9
- **优化**：d100_a32_s123 mmlu 改用 `--signal s4`（s1/s2 已存在），跳过 ~16 min 冗余计算
- **修正**：`--signal selfcritique` → `--signal s4`（argparse 只接受 s1/s2/s3/s4/all）

### 5. nvidia-smi 验证
PID 668217 独占 cuda:4，6876 MiB，正在处理 d025_s123 mmlu s4 chunk [0:1000]（chunked mode active，14042 items → 15 chunks）。

**任务队列**：d025_s123 mmlu s4 → d100_a32_s123 mmlu s4 → d100_a32_s123 gsm8k all → d100_a32_s123 arc all → V9_ALL_DONE

---
