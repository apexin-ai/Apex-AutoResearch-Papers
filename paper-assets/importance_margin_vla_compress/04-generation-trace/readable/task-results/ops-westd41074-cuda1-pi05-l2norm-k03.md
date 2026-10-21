# ops westd41074 cuda1 pi05 l2norm k03

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd41074-cuda1-pi05-l2norm-k03_20260521T073050_result.json`
- **Structured JSON:** [`9a570fa1145799b825f2.json`](../../sessions/9a/9a570fa1145799b825f2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**GPU 1 确认成功。** PID 936652 在 GPU 1 上运行（10389MiB，Bus-Id 49:00）。

eval 正在进行：T0 ep=10: 0/10=0%（符合预期，k=0.3 应该比 k=0.5 更差）。

总结：
- 根因是脚本内部 `os.environ["CUDA_VISIBLE_DEVICES"] = str(args.gpu)` 覆盖外部设置，必须用 `--gpu 1` 而非 `export CUDA_VISIBLE_DEVICES=1`
- 进程已在 GPU 1 上正常运行，tmux session: `eval_pi05_l2norm_k03`

---
