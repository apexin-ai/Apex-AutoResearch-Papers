# train sft alpha 2p0 and evals

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_sft-alpha-2p0-and-evals_20260515T142831_result.json`
- **Structured JSON:** [`d0772f9bd3c339bbeb72.json`](../../sessions/d0/d0772f9bd3c339bbeb72.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

### 结果

**α=2.0 SFT**
- PID: 41045（python 进程），父进程 41040
- GPU 1 显存 12.8GB / 97.9GB，利用率 92%
- 日志：`/tmp/sft_alpha2_0.log`，模型已加载，正在数据准备阶段
- 参数：去掉了 `--save_strategy no`（该脚本不支持此参数）

**α=0.5 模型修复**
- 原缺 tokenizer.json、tokenizer_config.json、chat_template.jinja
- 已从 α=0.0 SFT 输出复制，现在完整

**nvidia-smi 两卡状态**
| GPU | 显存占用 | 利用率 | 任务 |
|-----|---------|--------|------|
| cuda:0 | 65.6GB / 97.9GB | 95% | GraSP SFT + eval（未碰） |
| cuda:1 | 12.8GB / 97.9GB | 92% | α=2.0 SFT（刚启动） |

另外注意到 cuda:1 上还有一个 α=0.0 eval (PID 40494) 在跑，会和 α=2.0 SFT 共享 cuda:1。如果显存不够可能需要处理，但目前 97.9GB 总显存应该够。

---
