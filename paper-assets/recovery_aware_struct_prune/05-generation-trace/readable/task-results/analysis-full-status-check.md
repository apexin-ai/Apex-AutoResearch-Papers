# analysis full status check

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_full-status-check_20260515T135834_result.json`
- **Structured JSON:** [`6e40a4641f0e3f3160dc.json`](../../sessions/6e/6e40a4641f0e3f3160dc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data collected. Here's the full status report.

---

## 1. GraSP 相关状态 (westd GPU 0)

**GraSP post-prune eval (N=1319 全量)**:
- `grasp_baseline_westd.log` 显示全量 eval 到 73/1319 后结束 (EXIT_CODE=0)
- 中间指标 (50/1319): **acc=8.0%, eos_rate=2.0%, avg_len=4019** — 剪枝后模型几乎不可用

**GraSP post-prune eval (N=100)**:
- `eval_grasp_n100.log` 正在运行中，进度 3/100，速度 ~91s/sample
- 预计还需 ~2.5h 完成

**GraSP SFT**:
- 输出目录 `/root/autodl-tmp/recovery_aware_struct_prune/sft_graspune_20/` **为空**，SFT 尚未产出模型
- 日志文件 `sft_grasp_20_westd.log` 存在但未读取

---

## 2. GRPO v6 进度 (westb) — 双双 OOM 崩溃

| 运行 | 崩溃点 | 错误 | EXIT_CODE |
|------|--------|------|-----------|
| RASP v6 | step 9/250 | OOM: 尝试分配 130 MiB，GPU 0 仅剩 44 MiB free | 129 |
| Standard v6 | step 9/250 | OOM: 尝试分配 1.02 GiB，GPU 0 仅剩 214 MiB free | 129 |

崩溃位置: `Adam._init_group()` — optimizer 状态初始化时爆显存

**进程仍占用 GPU 未清理**:
- PID 520997 (RASP): GPU 0, 67430 MiB
- PID 521089 (Standard): GPU 1, 74318 MiB

配置: `max_completion_length=1024, gradient_checkpointing=true, beta=0.01, temp=0.4, lr=1e-6, loss=dapo`

两个 ref_model + train_model 在各自 GPU 上约占 95 GiB，optimizer 状态无法分配。

---

## 3. westd GPU 利用率

| GPU | 显存 | 利用率 | 进程 |
|-----|------|--------|------|
| cuda:0 | 64542/97887 MiB | 95% | PID 38120 (13 GB) + PID 38514 (51 GB) |
| cuda:1 | 50487/97887 MiB | 83% | PID 38802 (51 GB) |

推测: GPU 0 跑 GraSP N=100 eval，GPU 1 跑 α=1.0 SFT

---

## 4. α ablation SFT 进度 (westd)

### 剪枝后 (pre-SFT) eval 结果

| α | accuracy | eos_rate | avg_len | 状态 |
|---|---------|----------|---------|------|
| 0.0 | 30% | 79% | 1266 | — |
| 0.5 | 25% | 70% | 1559 | — |
| 1.0 | 27% | 90% | 817 | — |
| 2.0 | 29% | 64% | 1958 | — |
| **4.0** | **40%** | 67% | 1979 | — |

α=4.0 剪枝后准确率最高 (40%)，符合预期（更强调恢复信号的层保留更好）。

### SFT 恢复训练进度

| α | SFT 状态 | 模型文件 | 备注 |
|---|---------|---------|------|
| 0.0 | **完成** | 12.3 GB model.safetensors | 含 tokenizer |
| 0.5 | **可能不完整** | 6.6 GB model.safetensors | 缺 tokenizer/chat_template |
| 1.0 | **训练中** | 仅 checkpoint-935 | step 233/1870 (12%), loss=0.929, tok_acc=0.773 |
| 2.0 | 无目录 | — | 未开始 |
| 4.0 | **完成** | 12.3 GB model.safetensors + checkpoint-1870 | — |

### Post-SFT eval (已完成)

| α | accuracy | eos_rate | avg_len |
|---|---------|----------|---------|
| 4.0 | **62%** | 98% | 239 |

α=4.0 SFT 后: 40% → 62%，eos_rate 67% → 98%，恢复效果显著。

---

## 关键问题汇总

1. **westb GRPO v6 双双 OOM** — 需要减显存（减小 max_completion_length、用 8bit optimizer、或卸载 ref_model 到 CPU），且僵尸进程需清理
2. **westd α=0.5 SFT 文件可能不完整** — model.safetensors 仅 6.6 GB（其他完整模型为 12.3 GB），缺 tokenizer 文件
3. **GraSP 剪枝后 acc=8%** — 远低于所有 α ablation 的 pre-SFT 表现，GraSP 剪枝质量堪忧
4. **α=1.0 SFT 预计还需 ~25 分钟完成** (剩余 1637 steps at ~1.1 it/s)

---
