# ops verify kill and gpu status

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify-kill-and-gpu-status_20260514T181617_result.json`
- **Structured JSON:** [`a172ae4b5a96f91a5888.json`](../../sessions/a1/a172ae4b5a96f91a5888.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Kill 验证
- PID 76953: **已死**（kill -9 后确认）
- PID 76958: **已死**（kill -9 后确认）
- tmux session mvp2_grpo_flatnli_r6: **GONE**
- cuda:3 显存: **0 MiB**（完全释放，P8 idle 18W）

⚠️ kill_job 再次未能杀死子进程——tmux session 被移除但 python 进程变成孤儿仍占显存。已手动 kill -9 清理。

## GPU 总览
| GPU | PID | 显存 | GPU利用率 | 进程 | 预期匹配 |
|-----|-----|------|----------|------|---------|
| cuda:0 | 80799 | 9710 MiB | 63% | /root/miniconda3/bin/python | ✅ eval ckpt-100（PID 80799 ≈ 80789） |
| cuda:1 | 75587 | 11020 MiB | 78% | /root/miniconda3/bin/python | ✅ eval ckpt-50（PID 75587 ≈ 75581） |
| cuda:2 | 78857 | 9400 MiB | 59% | /root/miniconda3/bin/python | ✅ eval multi ckpts（PID 78857 ≈ 78850） |
| cuda:3 | — | 0 MiB | 0% | 空闲 | ✅ flatnli_r6 已清理 |

注：实际 PID 与预期有微小偏移（80799 vs 80789 等），这是因为实际运行的是 fork 出的子进程而非 wrapper shell。

## eval_step100 详情
- tmux session: `mvp2_eval_ced_kl001_r4_step100`（唯一存活的 tmux session）
- 日志位置: `/root/runs/faith-evidence-ie/mvp2_eval_ced_kl001_r4_step100.log`
- 进度: **5/62 batches（8%）**，~83s/batch，已运行约 7 分钟，预估剩余 ~79 分钟
- 评估目标: `grpo_ced_kl001/checkpoint-100`，dev set 985 docs / 12275 triples

---
