# diagnose plan001 exec only s43 1000

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_plan001-exec-only-s43-1000_20260515T134633_result.json`
- **Structured JSON:** [`252fa43e1db7b427194b.json`](../../sessions/25/252fa43e1db7b427194b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断报告：plan001-exec-only-s43-1000

**根因**：磁盘满 (`No space left on device`, os error 28)

**细节**：
- `/root/autodl-tmp/` 已 250G/250G (100%)，0 可用空间
- 训练在 step 150 / 1000 保存 checkpoint 时崩溃（`safetensors serialize` 失败）
- 训练本身正常运行了 ~21 分钟（步 1→150），reward/loss 无异常

**Checkpoint 状态**：
| Checkpoint | 状态 | 大小 |
|---|---|---|
| checkpoint-100 | 完整（4/4 shards + tokenizer + trainer_state） | 15GB |
| checkpoint-150 | **损坏**（仅 2/4 shards） | ~9.3GB（浪费空间） |

**分类**：`retryable` — 环境问题，代码无 bug

**紧急风险**：`plan001-exec-only-s44-1000` 正在 GPU 1 上运行（PID 357079, 82.6GB 显存），同样会在下次 checkpoint save 时因磁盘满崩溃。

**重试前需要的修复**：
1. 删除损坏的 `checkpoint-150`（回收 ~9.3GB）
2. 清理已完成实验的旧 checkpoint（磁盘上有 ~260GB outputs，多个实验各占 15-31GB）
3. 需要至少 ~30GB 空闲空间才能完成 1000 步训练（1 个完整 checkpoint ~15GB + save 临时空间）
4. 优先清理候选：已 eval 且有结论的实验 checkpoint（如 plan018_r3、plan002_b01_s42、plan004_fast_isr 等）

---
