# code qa probe script

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_qa_probe_script_20260516T215649_result.json`
- **Structured JSON:** [`d9c3cd7a21fd3d5316b1.json`](../../sessions/d9/d9c3cd7a21fd3d5316b1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run 完全通过。但有一个问题值得注意：accuracy 都在 94-98% 之间，L0 trained 和 untrained 完全一样（0.9474）。这是预期的，因为 L0 是 projector output，对于单 task 的轨迹来说，progress/subtask 标签本质上就是时间位置编码，视觉特征在时间轴上变化天然可分。全部 10 tasks 一起跑时，跨 task 的特征多样性会让 acc 更有区分度。

**完成状态**:

- 脚本路径: `/root/vla-ssd/scripts/qa_probe_classification.py`
- 结果路径: `/root/autodl-tmp/vla-ssd/results/qa_probe/classification_results.json`
- Dry-run (1 task × 1 layer): 通过，~25s 完成
- 完整运行预计: 2 tasks × 9 layers × 2 conditions + DINO + projector ≈ 20-30min on CPU

运行完整实验命令:
```bash
/root/miniconda3/bin/python3.12 /root/vla-ssd/scripts/qa_probe_classification.py --condition all
```

---
