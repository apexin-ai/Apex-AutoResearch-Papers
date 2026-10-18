# verify cqa1 gpu2 status

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_cqa1_gpu2_status_20260527T074515_result.json`
- **Structured JSON:** [`60043e0880dbefc91d3c.json`](../../sessions/60/60043e0880dbefc91d3c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果汇总：

**1. PID 89654 (strict_v2): 已死**
- 模型加载成功（4143.4M params, 15:42→15:46），pruning 配置正确（attention, keep 243/256）
- 崩溃原因：`httpx.ConnectError: [Errno 104] Connection reset by peer` — 下载 tokenizer `google/paligemma-3b-pt-224` 时网络断连
- 崩溃时间：约 15:48（日志最后修改时间）

**2. GPU2 当前状态**
- PID 93525 占用，10486 MiB，已运行 ~12 分钟
- 进程：`eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.85` — 这是另一个实验，不是 strict_v2

**3. 全部 GPU 占用**

| GPU | PID | 显存 | 说明 |
|-----|-----|------|------|
| 0 | 896333 | 15692 MiB | python |
| 1 | 11249 | 15385 MiB | python |
| 2 | 93525 | 10486 MiB | l2norm k=0.85 (~12min) |
| 3 | 897100 | 15694 MiB | python |

**4. 旧 PID 938642: 确认已死**

**结论**: strict_v2 实验因 HF 网络问题崩溃，需要重启。重启前需确保 tokenizer `google/paligemma-3b-pt-224` 已本地缓存或网络可用。GPU2 当前被 l2norm k=0.85 实验占用，strict_v2 需等 GPU2 空出或用其他 GPU。

---
