# ops westd 14b progress

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd-14b-progress_20260518T114511_result.json`
- **Structured JSON:** [`083ad5f69c8701f0f506.json`](../../sessions/08/083ad5f69c8701f0f506.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

进程 `ps aux` 因管道符被 read-only 模式拦截，但 `nvidia-smi` 已确认 PID 20700 存活。汇总：

**进程状态**: PID 20700 运行中，GPU 0 占用 32.4GB / 97.9GB，利用率 92%

**数据生成进度**:
| 文件 | 样本数 |
|------|--------|
| depth_0.jsonl | 5000 |
| depth_1.jsonl | 5000 |
| depth_2.jsonl | 3435 (生成中) |

**日志** (最新):
- d1 LoRA 训练已完成: loss=0.3451, 3 epochs, runtime=2534s
- Adapter 已保存: `checkpoints/qwen25_14b/lora_depth_1`
- 当前阶段: **Phase 3.2b — 用 LoRA(d1) 生成 d2**，正在加载模型权重(已 100%)，即将开始采样 5000 条

**结果文件**: `results/qwen25_14b_scale_003/` 尚不存在（未到评估阶段）

**GPU**: RTX PRO 6000 Blackwell x2，GPU 0 活跃 (236W, 92%), GPU 1 空闲

---
