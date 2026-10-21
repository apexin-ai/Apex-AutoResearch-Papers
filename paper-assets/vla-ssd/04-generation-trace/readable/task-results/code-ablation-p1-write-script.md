# code ablation p1 write script

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_ablation_p1_write_script_20260516T091637_result.json`
- **Structured JSON:** [`e42927f2b8720b64a853.json`](../../sessions/e4/e42927f2b8720b64a853.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run 通过。脚本已写入 `/root/vla-ssd/scripts/ablations/probe_seed_robustness.py`。

验证结果：seed=0, layer=0 的 R²=0.6326，train=50480 samples, val=12748 samples，逻辑正确。完整运行命令：

```bash
python /root/vla-ssd/scripts/ablations/probe_seed_robustness.py --gpu 0
```

预估耗时：~0.3min/layer × 33 layers × 5 seeds ÷ 1(层数据复用) ≈ 50min。

---
