# check experiment progress

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_experiment_progress_20260519T222020_result.json`
- **Structured JSON:** [`fe6bdc495993f5dd3f1a.json`](../../sessions/fe/fe6bdc495993f5dd3f1a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验进度汇报

### 1. r2_probe_seed_expansion (PID 168392)

- **进度: ~76% (75/99 layers)**
- 3 个 condition，每个 33 layers (L0-L32)：
  - `untrained`: 已完成 (33/33)
  - `llama2base`: 已完成 (33/33)
  - `trained`: 进行中 (9/33, 当前完成 L0-L8)
- 子进程 PID 168397 活跃，347% CPU
- 每层约 100-130s，剩余 24 层 ≈ **40-50 分钟**
- 结果文件尚未生成
- GPU 1 在用 (1739 MiB, 22%)

### 2. specificity_random_seed_expansion (PID 169052)

- **Phase 1 (GPU cache): 已完成** — 63728 frames, 10 tasks, 500 demos, 耗时 25.1 min
- **Phase 2 (CPU bootstrap 30 seeds): 刚启动**，日志无进度输出
- Cache 文件已生成: 1.8GB (`l1_attention_cache.pt`)
- 子进程 PID 169053 活跃，3001% CPU（约 30 核全开做 bootstrap）
- 结果文件尚未生成
- 预计剩余时间不确定（取决于 bootstrap 计算量，但 CPU 全力运行中）

### 3. GPU 状态

| GPU | 显存占用 | 利用率 |
|-----|---------|--------|
| 0 | 3 MiB | 0% |
| 1 | 1739 MiB | 22% |

两个实验均在正常运行。r2_probe 预计约 40-50 分钟内完成；specificity 的 Phase 2 刚开始，需要等后续日志输出才能估算剩余时间。

---
