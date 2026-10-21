# ssh mf4 s123 diagnose resubmit

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_mf4_s123_diagnose_resubmit_20260522T103847_result.json`
- **Structured JSON:** [`ba719d606338646cebea.json`](../../sessions/ba/ba719d606338646cebea.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

autodl-5090 四张卡全部占满（~30GB/32GB），没有空闲卡。

```
失败原因: GPU 显存不足。任务尝试在 cuda:0 上启动 vLLM，但该卡仅剩 1.44/31.36 GiB 空闲（被其他进程占用）。
         不是模型缺失问题。
模型状态: 已存在于 autodl-5090:/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-fewnerd-exp021-merged/
autodl-5090 空闲卡: 无（4卡全部占用 ~30GB/32GB）
建议: 等当前任务完成释放 GPU 后，在 autodl-5090 空闲卡上重新提交。
      提交时需确保 CUDA_VISIBLE_DEVICES 指向空闲卡。
```

---
