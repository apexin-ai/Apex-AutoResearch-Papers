# investigate s43 status

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_investigate_s43-status_20260515T112951_result.json`
- **Structured JSON:** [`e0a4dce1a8a0ff050590.json`](../../sessions/e0/e0a4dce1a8a0ff050590.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

### 1. s43 训练状态 → **DONE (success)**

| 指标 | 值 |
|------|-----|
| eval_loss | 0.7622 |
| train_loss | 0.6148 |
| mean_token_accuracy | 0.8291 |
| 总步数 | 510 (3 epochs) |
| 训练时长 | 1.99h |
| Checkpoints | 350, 400, 450, 500, 510 ✓ |
| Adapter 保存 | `/root/autodl-tmp/rsft_output_s43` (528MB) ✓ |

与其他 seed 对比：s43 eval_loss=0.7622 vs r1 epoch1=0.756/epoch2=0.759。训练正常收敛。

Registry 已更新为 DONE + metrics + checkpoint_path。

### 2. s43 eval 失败根因与修复

**第一次** (`mvp2_eval_rsft_s43`): EXIT_CODE=2，参数名错误：
- `--rsft_adapter` → 应为 `--model_path`
- `--data_dir` → 应为 `--data_path`
- `--gpu 0` → 该参数不存在

**已修复并重试** (`mvp2_eval_rsft_s43_r2`): 正在运行，刚启动（1/124 batches），模型已加载成功。

### 3. GPU 占用与预估时间

| GPU | 进程 | 进度 | 预估剩余 |
|-----|------|------|----------|
| 0 | ced_reranker_poc | 运行中 | 未知（长时间任务） |
| 1 | eval_rsft_r2a | 108/124 | ~14 min |
| 2 | eval_rsft_s43_r2 | 1/124 | ~1.7h (~21:10) |
| 3 | eval_rsft_r2b | 109/124 | ~12 min |

r2a 和 r2b eval 即将完成（~15min 内）。s43 eval 刚启动，约 1.7h 后出结果。GPU 1 和 3 很快会空出。

---
