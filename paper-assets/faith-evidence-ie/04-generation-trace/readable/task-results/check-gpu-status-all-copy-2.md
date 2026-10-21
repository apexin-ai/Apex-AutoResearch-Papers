# check gpu status all

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_gpu-status-all_20260515T005840_result.json`
- **Structured JSON:** [`788930859ce41f0a27b6.json`](../../sessions/78/788930859ce41f0a27b6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态报告

### GPU 占用

| GPU | 显存占用 | 利用率 | 任务 |
|-----|---------|--------|------|
| 0 | 13645 / 32607 MiB (42%) | 48% | GRPO 训练 |
| 1 | 23195 / 32607 MiB (71%) | 88% | RSFT 生成 |
| 2 | 0 / 32607 MiB | 0% | **空闲** |
| 3 | 10653 / 32607 MiB (33%) | 77% | ckpt-100 eval |

### PID 状态

| PID | 状态 | 运行时间 | 任务 |
|-----|------|---------|------|
| 90080 | **ALIVE** | 5.3h | GRPO 训练 |
| 117635 | **ALIVE** | 1.3h | ckpt-100 eval |
| 122144 | **ALIVE** | 49min | RSFT 生成 |
| 111731 | **DEAD** | — | (见下) |

### 各任务详情

**1. GRPO 训练 (PID 90080, GPU 0)** — step 185/200 (92.5%)
- ETA: ~26 分钟
- 最近 reward: 0.28~0.45，learning rate 已衰减至 1.275e-6
- ⚠️ step 85 和 90 出现 KL 爆炸警告（13.8M 和 684.8），但设置为 monitoring only 未停止训练
- 训练即将完成

**2. RSFT 生成 (PID 122144, GPU 1)** — 91/1514 batches (6%)
- **无 CUBLAS 错误**，运行正常
- 已产出 1456 行 generations.jsonl (13.7MB)
- 首 100 样本监控：format_ok 99.6%，truncation 9.2%，diversity 0.9/8
- 速度 ~30-37s/batch，ETA ~13 小时

**3. ckpt-100 Eval (PID 117635, GPU 3)** — 49/62 batches (79%)
- 使用 `--quantize` 加载，运行正常
- 速度 ~95s/batch，ETA ~20 分钟
- 即将完成

**4. ckpt-80 Eval (PID 111731)** — **DEAD**
- 日志文件 `mvp2_eval_lr5e6_r1_ckpt80.log` 不存在
- 该任务从未启动或使用了不同的日志路径

### 总结
- GRPO 和 ckpt-100 eval 都将在 ~20-30 分钟内完成
- RSFT 生成正常运行，无 CUBLAS 错误，但全量生成还需 ~13 小时
- GPU 2 空闲，可用于启动 ckpt-80 eval 或其他任务
- GRPO 训练中出现过两次 KL 爆炸（step 85/90），后续已恢复正常范围

---
