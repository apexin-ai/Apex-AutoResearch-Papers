# ops pi05 status and continue

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_pi05_status_and_continue_20260517T172834_result.json`
- **Structured JSON:** [`2415d439bebed3a41b47.json`](../../sessions/24/2415d439bebed3a41b47.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

**进程状态**：已结束，GPU 空闲，无 python 进程。

**Checkpoint**：确认使用了 finetuned 版本 `/root/autodl-tmp/pi05-libero-finetuned`（来源 `pepijn223/pi05_libero_31_9_non_q`）。

**Eval 结果**：**0% SR，早停退出。**
- Task 0: 0/50 (完整跑完)
- Task 1: 0/10 (部分)
- 早停原因：60+ episodes 跨 2 个 task 均 0% SR，低于 20% 阈值
- 只完成了 1.2/10 个 task，总耗时 15.4 分钟

**Vision fix 已生效**：日志确认 `Patched embed_image: bypass get_image_features, use vision_tower+projector directly`，结果文件也记录了 vision fix 信息。结论中提到模型确实产生了 varying、reasonable-magnitude 的 actions，但没有 episode 成功。

**关键判断**：vision bug 修复后 baseline 仍然是 0%。结果文件的结论指向两个可能原因：
1. **Checkpoint 本身质量问题** — `pepijn223/pi05_libero_31_9_non_q` 这个 finetuned checkpoint 可能不 work
2. **Preprocessing mismatch** — tokenizer vocabulary、state normalization 或 action post-processing 可能与原始 OpenPI 实现不一致

---
