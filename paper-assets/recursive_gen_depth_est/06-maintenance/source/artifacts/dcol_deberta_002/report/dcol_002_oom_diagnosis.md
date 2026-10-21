# dcol_deberta_002 OOM 诊断报告

**时间**: 2026-05-15 06:44 UTC

## GPU 0 进程分析

| PID | 进程 | GPU 显存 | 身份 |
|-----|------|----------|------|
| 193689 | `python src/dcol_trainer.py --batch_size 32 --model_path deberta-v3-large` | 57.35 GiB | dcol_deberta_002 本身（非残留） |
| 208941 | `python scripts/extract_features.py --model_path gpt2-xl --gpu 0` | 8.81 GiB | gpt2xl_temp09 评估流水线（活跃任务） |

另有 4 个 dcol_trainer DataLoader worker (PID 207313-207316)，均为 CPU 进程。

## OOM 原因

dcol_deberta_002 (batch_size=32, deberta-v3-large) 稳态占用 ~57GB。同时 gpt2xl_temp09 的 extract_features.py 在 GPU 0 上占用 ~9GB。两者合计 ~66GB + CUDA context/fragmentation，导致 GPU 0 (94.97 GiB) 在 attention dropout 层尝试分配 512MiB 时仅剩 504.88MiB，触发 OOM。

**根因**: GPU 0 上同时运行了两个独立实验，显存竞争。代码本身无 bug。

## 清理结果

所有相关进程（193689, 193688, 207313-207316）在诊断时已自行退出（`No such process`）。PID 208941 (extract_features) 也已完成退出。

**GPU 0 当前状态**: 0MiB / 97887MiB，完全空闲。
**GPU 1 状态**: olmo_temp09_001 (PID 207537) 正常运行，未受影响。

## 代码与数据完整性

- `src/dcol_trainer.py`: 存在，20847 bytes，最后修改 May 15 06:38 ✓
- `data/features_all.jsonl`: 存在，13.7MB，最后修改 May 14 21:58 ✓

## 重试建议

**可以安全重试 dcol_deberta_002**。GPU 0 当前完全空闲（97.9GB 可用）。

建议重试时确保 GPU 0 无其他进程竞争显存，或适当降低 batch_size（如 24 或 16）以留出安全余量。
