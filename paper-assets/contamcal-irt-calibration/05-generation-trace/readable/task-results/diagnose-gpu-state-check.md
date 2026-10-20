# diagnose gpu state check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_gpu-state-check_20260516T004516_result.json`
- **Structured JSON:** [`9d1ce9c173f357789748.json`](../../sessions/9d/9d1ce9c173f357789748.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据已齐全。以下是完整诊断报告。

---

## GPU 状态诊断报告（2026-05-16 ~08:45 UTC）

### 各 GPU 占用详情

| GPU | 显存占用 | 利用率 | PID | 进程 | 实验 | 运行时长 |
|-----|---------|--------|-----|------|------|---------|
| **0** | **23260/24564 MiB (95%)** | **96%** | 642763 | evaluate.py | d100_a32_s123 (mmlu/gsm8k/arc/humaneval aligned) | 3h10m |
| **0** | ↑ 同上 | ↑ | 643167 | train_sft.py | **d005_s42** (alpha=32, lr=5e-5) | 3h09m |
| 1 | 13341/24564 MiB (54%) | 43% | 628668 | train_sft.py | d100_a32_s42_v3 (alpha=32) | 4h34m |
| 2 | 7537/24564 MiB (31%) | 61% | 652259 | compute_signals.py | d005_s123 / mmlu / signal=all | 1h41m |
| 3 | 8985/24564 MiB (37%) | 71% | 655989 | evaluate.py | d025_v3_s42 aligned (mmlu/gsm8k/arc) | 1h24m |
| 4 | 7445/24564 MiB (30%) | 59% | 662616 | compute_signals.py | d100_a32_s123 / mmlu / signal=all | ~30m |
| 5 | 7531/24564 MiB (31%) | 63% | 663067 | compute_signals.py | d025_v3_s42 / mmlu / signal=s4 | ~27m |

### cuda:0 冲突：**真实存在，严重**

两个进程共享 GPU 0：
- **PID 642763**（eval，8976 MiB）+ **PID 643167**（SFT 训练，14270 MiB）= 23246 MiB
- 已占满 95% 显存，距 OOM 仅剩 ~1.3 GB
- SFT 训练和 eval 互相争抢 compute，两者都会变慢
- PID 643167 的 `--gpu 0` 说明它被显式提交到 cuda:0，与 eval 形成了调度冲突

### cuda:4：**不空闲，signals_v8 正在运行**

- PID 662616 正在 GPU 4 上运行 `compute_signals.py`（d100_a32_s123 / mmlu / signal=all）
- 日志尾部显示 Self-critique mmlu 进度 **817/7021 (12%)**，~1.42s/it，预计还需 **~2.4h**
- **signals_v8 没有失败**——它在正常推进

### signals_v8 失败根因

**signals_v8 未失败。** 日志最后一条有效输出是 `Self-critique mmlu: 12%` 进度条，无任何错误信息。PID 662616 活跃、GPU 4 有 59% 利用率。如果之前有一个旧的 v8 实例失败后被重启了，当前实例运行正常。

### 额外注意

PID 643167 正在训练 `Qwen2.5-3B_d005_s42`（输出目录在 C006 废弃黑名单上），但命令行中 `--lora-alpha 32` 是正确的。如果这是有意用 alpha=32 覆盖旧 alpha=16 checkpoint，则无问题；但输出目录名称未加 `_v3` 后缀，后续可能造成混淆。

### 建议下一步

1. **解决 cuda:0 冲突（紧急）**：二选一——要么 kill PID 642763（eval），等 SFT 完成后再跑；要么将 eval 迁移到其他卡（cuda:1 训练完成后有空间）
2. **不要动 cuda:4**：signals_v8 正在跑，预计 ~2.4h 完成当前 mmlu self-critique 阶段
3. **考虑 d005_s42 输出目录命名**：是否应改为 `Qwen2.5-3B_d005_v3_s42` 以区分旧 alpha=16 版本

---
