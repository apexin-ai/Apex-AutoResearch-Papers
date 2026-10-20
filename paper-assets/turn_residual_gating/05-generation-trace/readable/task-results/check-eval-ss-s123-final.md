# check eval ss s123 final

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_eval_ss_s123_final_20260523T173732_result.json`
- **Structured JSON:** [`36b1cf48529be16b5dff.json`](../../sessions/36/36b1cf48529be16b5dff.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据收集完毕。汇总如下：

---

## SS s123 Eval 状态

**AR eval 尚未完成。** PID 110052 正在运行 `eval_attention_steering.py`（已运行 ~14 分钟，模型已加载，generation 进行中）。GPU 链处于 Step 1/7。

- GPU: 47% utilization, 30.4 GB / 97.9 GB VRAM
- gpu_chain_next.sh 未退出，Step 2 (SS s456 resume) 尚未启动

### TF 结果（已完成，200 convs）

| Model | GAR-ours | GAR-dongre | PPL |
|-------|----------|------------|-----|
| Base | 0.1008 | 0.0075 | 3.959 |
| SS s42 | 0.5272 | 0.4434 | 2.780 |
| SS s123 | 0.5536 | 0.4106 | 2.612 |

s123 在 GAR-ours 上略优于 s42（+0.026），GAR-dongre 上略低（-0.033），PPL 更优（-0.168）。

### AR 结果（SS s42，已完成，N=50）

| Beta | GAR-ours | 95% CI | PPL |
|------|----------|--------|-----|
| 0 | 0.347 | [0.327, 0.366] | 1.442 |
| 3 | 0.593 | [0.574, 0.613] | 1.564 |
| 5 | 0.717 | [0.696, 0.738] | 1.779 |

### AR 结果（SS s123）
**等待中** — PID 110052 正在生成（beta=0,3,5, N=50），预计还需 ~30-45 分钟完成。

### GPU 链后续（7 步）

| Step | 任务 | 状态 |
|------|------|------|
| 1 | SS s123 eval (TF+AR) | TF ✅ AR 进行中 |
| 2 | SS s456 resume training | 等待 |
| 3 | SS s456 eval | 等待 |
| 4 | Qwen-1.5B Phase 1 diag | 等待 |
| 5 | Qwen-1.5B TG training | 等待 |
| 6 | Qwen-1.5B eval | 等待 |
| 7 | MMLU eval (6 ckpts) | 等待 |

无正在运行的 train_phase2 或 s456 进程。AR eval 完成后链会自动推进到 Step 2。

---
