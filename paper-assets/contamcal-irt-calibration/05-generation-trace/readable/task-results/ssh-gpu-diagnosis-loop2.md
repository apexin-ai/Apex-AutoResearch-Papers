# ssh gpu diagnosis loop2

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_gpu-diagnosis-loop2_20260513T231618_result.json`
- **Structured JSON:** [`eedcc0df4483baf7c9f8.json`](../../sessions/ee/eedcc0df4483baf7c9f8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断报告

### 1. GPU 状态（6x RTX 4090 D 24GB）

| GPU | 显存占用 | 利用率 | PID | 进程 | 状态 |
|-----|---------|--------|-----|------|------|
| 0 | 0 MiB | 0% | — | — | **空闲** |
| 1 | 3667 MiB | 33% | 229375 | evaluate.py Qwen2.5-0.5B_d000_s42 | GSM8K 13% (173/1319) |
| 2 | 3667 MiB | 33% | 229521 | evaluate.py Qwen2.5-0.5B_d000_s123 | GSM8K 12% (161/1319) |
| 3 | 17327 MiB | 7% | 216254 | evaluate.py Qwen2.5-1.5B_d000_s123 | GSM8K 18% (236/1319) |
| 4 | 5829 MiB | 50% | 221376 | evaluate.py Qwen2.5-1.5B_d000_s42 | GSM8K 62% (860/1319) |
| 5 | 18665 MiB | 30% | 210671 | train_sft.py Qwen2.5-3B_d000_s42 | **99% (3082/3125 steps, 即将完成)** |

### 2. MMLU Paraphrase 状态

- 目录 `/root/contamcal-irt-calibration/exp001/paraphrases/` **不存在**
- `mmlu_paraphrases.json` **不存在**
- 无 vLLM 或 MMLU paraphrase 相关进程
- **状态：未启动**

### 3. GPU 1/2 重复进程

**无重复。** GPU 1 仅有 PID 229375，GPU 2 仅有 PID 229521，各一个 evaluate.py 进程。

### 4. SFT 训练状态

全部 4 个 SFT 任务已完成（exit code 0）：
- Qwen2.5-0.5B_d000_s42: 完成于 05-13 20:31 UTC
- Qwen2.5-0.5B_d000_s123: 完成于 05-13 21:36 UTC
- Qwen2.5-1.5B_d000_s42: 完成于 05-13 21:22 UTC
- Qwen2.5-1.5B_d000_s123: 完成于 05-13 22:23 UTC
- **Qwen2.5-3B_d000_s42: 仍在 GPU 5 上训练，99% 即将完成**

### 5. Eval 结果

4 个 eval 结果目录均已创建但 **无 results_summary.json**（评估尚未完成）。

**关键问题：** 0.5B 的两个 eval（s42/s123）在 MMLU 阶段因 HuggingFace Hub 连接超时失败（huggingface.co connect timeout），脚本自动跳过 MMLU 改用缓存版 GSM8K 继续。1.5B 的两个 eval 也有同样的 HF 超时问题但成功 fallback 到缓存。

### 6. 建议

1. **GPU 0 空闲** — 可立即调度新任务
2. **GPU 5** — 3B SFT 训练 ~1-2 分钟内完成，之后释放
3. **HF 连接问题** — 所有 eval 的 MMLU benchmark 都因 HF Hub 超时受影响。需要 `source /etc/network_turbo` 启用代理，或预先下载 MMLU 数据集到本地缓存
4. **无需清理进程** — 当前所有 GPU 进程都是有效的 eval/training 任务
5. **预计时间线**：1.5B_s42 的 GSM8K 还需 ~40 分钟；0.5B 的两个 eval 还需 ~1.8 小时；1.5B_s123 还需 ~1.5 小时

---
