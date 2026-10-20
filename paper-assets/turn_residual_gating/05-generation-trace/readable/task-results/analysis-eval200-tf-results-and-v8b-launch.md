# analysis eval200 tf results and v8b launch

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval200_tf_results_and_v8b_launch_20260520T100041_result.json`
- **Structured JSON:** [`de205905566f9e47d4a2.json`](../../sessions/de/de205905566f9e47d4a2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个任务均完成。汇报：

---

### Part 1: eval_200 tf-mode attention steering 结果 — **成功**

| Beta | Mid-GAR | PPL |
|------|---------|------|
| 0.0 | 0.5353 | 2.62 |
| 2.0 | 0.6112 | 2.69 |
| 3.0 | 0.7880 | 2.93 |
| 4.0 | 0.8165 | 3.49 |
| 5.0 | 0.8325 | 6.15 |
| 10.0 | 0.9770 | 505.21 |

200 conversations, tf mode, GAR-ours variant。β=3~5 是实用甜区（GAR>0.8，PPL<7）。β=10 GAR 接近 1.0 但 PPL 爆炸。Registry 已更新为 DONE，cron 已删除。

### Part 2: v8b resume 训练 — **已启动**

- **PID**: 169233
- **GPU 显存**: 32744 MiB (~32GB / 98GB)
- **GPU Util**: 84%
- **Resume 状态**: epoch_0 checkpoint 加载成功，从 epoch 1 开始，global_step=1000，lr=[1.69e-4, 1.69e-3]
- **修改**: 给 `train_phase2_v8b.py` 添加了 `--resume` 参数（5 处修改：参数定义、LoRA/gate 权重加载、scheduler 推进、global_step 初始化、epoch range）
- **首条日志**: `Epoch 1 Step 0 | L_NTP=1.1568` — 正常运行
- **预估剩余时间**: ~14-15h（2/3 epochs，原始 3 epoch 约 22h）

---
