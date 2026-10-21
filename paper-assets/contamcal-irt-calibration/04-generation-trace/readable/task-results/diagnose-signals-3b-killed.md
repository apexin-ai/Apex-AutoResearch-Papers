# diagnose signals 3B killed

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_signals-3B-killed_20260515T153007_result.json`
- **Structured JSON:** [`a2b4e65c290aa5d56a32.json`](../../sessions/a2/a2b4e65c290aa5d56a32.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完整情况已清晰。诊断结果如下：

---

## 诊断结果

### 失败原因：两个独立问题

**问题 1：Task 1 (d000_s42/mmlu) — SIGTERM 被杀**

- **不是 OOM，不是 CUDA 错误**。SIGTERM (signal 15) 是外部显式 kill，不是 GPU 显存溢出（OOM 会导致 CUDA RuntimeError 或 kernel OOM killer 发 SIGKILL/9）。
- 进程跑了 37 分钟（22:46 → 23:23），完成了 embedding + minkpp，selfcritique 跑到 83% (365/439) 时被杀。
- **怀疑原因不成立**：日志显示 `GPU: 0`（不是 cuda:3），所以 exp_001_eval_3B (PID 576735) 在 cuda:3 的 8976 MiB 占用与本次实验**无关**。
- **真实原因**：`compute_signals.py` 在 batch 运行期间被替换（旧版 228 行 → 新版 120 行，`.bak` 文件证实）。代码部署者可能同时 kill 了正在运行的进程。

**问题 2：Tasks 2-12 — 参数不兼容 (rc=2)**

- **代码版本冲突**：batch 运行期间 `compute_signals.py` 被替换成新版本（`--signal` 单数 required=True），但内存中的旧 `run_batch.py` 按旧版 API 构造命令（旧版用 `--signals` 复数 + 有 default 值）。
- 新版要求 `--signal` 参数，旧 batch runner 没传 → 全部 argparse 错误退出。
- 两个文件在 batch 结束后又被更新了一次（run_batch.py 23:31, compute_signals.py 23:33），当前磁盘版本已修复兼容性。

### 已完成的信号

仅 **d000_s42/mmlu** 的 2/3 信号：
| 文件 | 状态 |
|------|------|
| `signal_embedding_mmlu.json` (6.1MB) | 完成 |
| `signal_minkpp_mmlu.json` (2.1MB) | 完成 |
| selfcritique mmlu | 83% 被杀，未保存 |

其余 11 个 task × 3 信号 = **33 个信号计算 + 1 个 selfcritique 未完成 = 全部需重跑**。

### 重跑建议

1. **当前版本已修复**——run_batch.py 和 compute_signals.py 的参数接口已对齐（`--signal all`），可以直接重跑。
2. **注意**：当前 resume 逻辑检查 `signals_merged_*.json`，由于没有任何 merged 文件，会重跑全部 12 个 task（包括 d000/mmlu 已完成的 embedding/minkpp，约多花 5-10 分钟，影响不大）。
3. **GPU 选择**：日志显示上次用的是 `GPU: 0`。提交前按 C001/C002 检查目标 GPU 空闲状态；按 C004 显式设 `CUDA_VISIBLE_DEVICES`。
4. `DOSAGES` 列表当前是 `["d000", "d005", "d100"]`（3 个），日志显示上次跑了 4 个 dosage（含 d025）。如果需要 d025，需要加 `--only d025` 或修改 DOSAGES。

---
