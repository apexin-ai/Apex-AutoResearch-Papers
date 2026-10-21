# run d025 v3 s3 constat and cuda verify

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_run_d025_v3_s3_constat_and_cuda_verify_20260515T230130_result.json`
- **Structured JSON:** [`edbd9e45b4d5ccc12730.json`](../../sessions/ed/edbd9e45b4d5ccc12730.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

探测完毕。两个任务的结果如下：

---

## 任务 2 结果：CUDA_VISIBLE_DEVICES 验证

**所有 5 个 PID 均未设置 CUDA_VISIBLE_DEVICES — 全部违反 C004。**

PID → GPU 映射（父进程 → 实际 GPU 子进程）：

| 跟踪 PID | tmux pane | GPU 子进程 PID | GPU | 显存占用 |
|-----------|-----------|---------------|-----|---------|
| 628663 | %178 | 628668 | **cuda:1** | 13332 MiB |
| 633036 | %180 | 633041 | **cuda:5** | 18656 MiB |
| 643162 (d005_s42_a32) | %182 | 643167 | **cuda:0** | 14268 MiB |
| 642752 (d100_s123_a32_batch) | %181 | 642763 | **cuda:0** | 8976 MiB |
| 623826 | %175 | ? | 未在 nvidia-smi 中匹配 | — |

**cuda:0 冲突确认**：d005_s42_a32 (PID 643167, 14268 MiB) 和 d100_s123_a32_batch (PID 642763, 8976 MiB) 共占 23244 / 24564 MiB，几乎满载。两者共存在同一 GPU 上。

其他 GPU 状态：
- cuda:1: 13341 MiB (PID 628668)
- cuda:2: **空闲** (0 MiB)
- cuda:3: 7658 MiB (PID 630891 — 未在跟踪列表中)
- cuda:4: 7526 MiB (PID 648627 — 未在跟踪列表中)
- cuda:5: 18656 MiB (PID 633041)

---

## 任务 1 阻塞：s3_constat 无法执行

**原因**：s3_constat 需要 `original_eval_paths` 和 `paraphrase_eval_paths`（模型在原始/改写 benchmark 上的 per-item 评估结果）。d025_v3 模型没有对应的 eval_results.json 文件。

现有 3B d025 评估数据：
- `Qwen2.5-3B_d025_v2_aligned/eval_results.json` — 属于 **v2** 模型
- `Qwen2.5-3B_d025_v2_s42_para_aligned/eval_results.json` — 属于 **v2** 模型
- `Qwen2.5-3B_d025_s123_aligned/eval_results.json` — seed 123
- `Qwen2.5-3B_d025_s123_para_aligned/eval_results.json` — seed 123

d025_v3 是不同训练配置（alpha=32, lr=5e-5）产生的不同权重，不能复用 v2 的评估结果。需要先对 d025_v3 模型运行 benchmark 评估（原始 + 改写版本），生成 eval_results.json 后才能计算 s3_constat。

---
