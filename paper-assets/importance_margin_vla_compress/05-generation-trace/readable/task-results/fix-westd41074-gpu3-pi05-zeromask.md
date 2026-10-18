# fix westd41074 gpu3 pi05 zeromask

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_westd41074_gpu3_pi05_zeromask_20260526T015719_result.json`
- **Structured JSON:** [`f80be09b18fdf8319ced.json`](../../sessions/f8/f80be09b18fdf8319ced.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

### 执行结果

| 步骤 | 状态 |
|------|------|
| Kill PID 303982 (GPU3 Attn k=0.85 Long) | ✓ force killed |
| Kill PID 300693 (GPU0 旧残留) | ✓ killed |
| Kill PID 309197 (意外残留，占 GPU3) | ✓ force killed（额外发现的残留进程） |
| 上传 `eval_pi05_zeromask_ablation.py` | ✓ 362 行 |
| 部署 π0.5 zeromask random k=0.9 Object | ✓ PID 308695, tmux session `eval_pi05_zeromask_random_k09_object_v3` |
| Registry 更新 | ✓ RUNNING |
| 更新被 kill 实验 | ✓ conclusion=killed |

### GPU 状态

| GPU | PID | 实验 | 显存 |
|-----|-----|------|------|
| 0 | 303189 | Random k=0.85 Long（保留） | 16188 MiB |
| 1 | 76492 | l2norm k05 Object（保留） | 15980 MiB |
| 2 | 259181 | attn k07 Object（保留） | 15980 MiB |
| 3 | 308695 | **π0.5 zeromask random k=0.9 Object** | 9709 MiB（torch inductor 编译中） |

### 注意事项
- 指令中的脚本名 `eval_pi05_pruning_libero.py` 不支持 `zero_mask_random` 模式，实际需要的是 `eval_pi05_zeromask_ablation.py`（已从 artifacts 上传到服务器）
- 进程正在 torch inductor 首次编译阶段（子进程 PID 310248，32 workers），预计还需数分钟后进入评测

---
