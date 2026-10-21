# fix exp 029b oom

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_exp_029b_oom_20260517T233710_result.json`
- **Structured JSON:** [`09766cc648a735e82e10.json`](../../sessions/09/09766cc648a735e82e10.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报：

1. **vLLM 进程 (PID 416808)**: 已 kill，退出码 0
2. **GPU 1 显存**: 已完全释放（2MiB / 32607MiB），空闲可用
3. **exp_029a 状态**: 仍在 GPU 0 上运行，进度 77/351 steps（~22%），GPU 利用率 85%，显存 30128MiB
4. **配置文件 GPU 设置**: 两个 yaml 均无 `device`/`cuda`/`gpu` 指定（只有 `per_device_*batch_size`），GPU 分配完全由 `submit_training_job` 的 `CUDA_VISIBLE_DEVICES` 控制，无需修改配置
5. **OOM 根因确认**: GPU 1 被残留 vLLM 进程占满显存，已清除。exp_029b 现在可以安全提交到 GPU 1

---
