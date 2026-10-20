# prep exp002 3B signals

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_exp002_3B_signals_20260515T181714_result.json`
- **Structured JSON:** [`8057c979635194b2b47e.json`](../../sessions/80/8057c979635194b2b47e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

信息收集完毕。以下是完整报告：

---

## exp-002 3B Signal Computation 准备状态报告

### 1. 代码就绪: ✓

| 文件 | 作用 |
|------|------|
| `run_batch.py` | 批量编排器，支持 resume/dry-run/GPU 选择 |
| `compute_signals.py` | 单次信号计算入口 (S1+S2+S3+S4) |
| `signals/s1_embedding.py` | S1: Embedding-based semantic retrieval |
| `signals/s2_minkpp.py` | S2: Min-K%++ membership inference |
| `signals/s3_constat.py` | S3: ConStat performance gap |
| `signals/s4_selfcritique.py` | S4: Self-Critique entropy collapse |

### 2. Prerequisites

| 依赖项 | 状态 |
|--------|------|
| Base model `Qwen2.5-3B` | ✓ `/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B/` |
| Checkpoint d000_s42 | ✓ |
| Checkpoint d005_s42 | ✓ |
| Checkpoint d025_s42 | ✓ |
| Checkpoint d100_s42 | ✓ |
| SFT data | ✓ (共用 exp001) |
| ConStat eval_results (S3) | ✗ 仅 d000 有原始 eval，无 para 版本 → **S3 全部跳过**（与 0.5B/1.5B 行为一致） |
| 数据盘空间 | ✓ 43GB free on `/root/autodl-tmp` |

### 3. 3B 部分输出现状（上次 v2 被 kill 的残留）

| Dosage | mmlu | gsm8k | arc_challenge |
|--------|------|-------|---------------|
| d000 | ✗ (缺 selfcritique+merged) | ✓ merged | ✓ merged |
| d005 | ✗ (缺 selfcritique+merged) | ✗ (缺 selfcritique+merged) | ✓ merged |
| d025 | ✗ (仅 s1_embedding) | ✗ | ✗ |
| d100 | ✗ (无目录) | ✗ | ✗ |

**Resume 行为**：默认 `--skip-completed` 会跳过 3 个已完成的 task (d000/gsm8k, d000/arc_challenge, d005/arc_challenge)，运行 9 个。**建议用 `--no-skip` 做全量 12-task 干净重跑**，避免部分输出的数据一致性问题。

### 4. GPU 状态

当前所有 6 张 4090D 均有负载：
- GPU 3: **~7.5GB 已用 / 24.5GB 总量，92% utilization，2 个 python 进程 (PID 608198, 608814)**

**按 C001/C002 约束，GPU 3 当前不可提交。需等待现有进程完成。**

### 5. 建议提交命令

```bash
CUDA_VISIBLE_DEVICES=3 nohup python /root/contamcal-irt-calibration/exp002/run_batch.py \
  --model-size 3B --gpu 3 --no-skip \
  > /root/autodl-tmp/exp002/logs/3B_signals_run.log 2>&1 &
```

关键点：
- `CUDA_VISIBLE_DEVICES=3` 显式设置（C004）
- `--no-skip` 全量重跑，确保一致性
- `--gpu 3` 传给脚本用于日志记录（实际 GPU 由环境变量控制）
- 日志输出到数据盘

提交前需确认：
1. `nvidia-smi` 确认 GPU 3 空闲（C002）
2. 无同类进程（C001）
3. 创建日志目录：`mkdir -p /root/autodl-tmp/exp002/logs`

### 6. 预估运行时间

3B 模型 × 4 dosages × 3 benchmarks = 12 tasks，每个 task 计算 3 个 signal (S1+S2+S4，S3 跳过)。单 4090D 预估 **4-8 小时**（参考 0.5B/1.5B 按模型大小线性外推，S2 Min-K%++ 是主要耗时项）。

### 7. 注意事项

1. **S3 (ConStat) 不会运行** — 缺少 `_para` eval 结果，与 0.5B/1.5B 一致，`compute_signals.py:94` 会 log warning 但不影响其他 signal
2. **merged 输出条件** — 需至少 2 个 signal 成功（line 97），S1+S2+S4 = 3 个，满足条件
3. **SSH 超时** — 用 nohup 后台运行，定期用 `tail /root/autodl-tmp/exp002/logs/3B_signals_run.log` 检查进度

---
