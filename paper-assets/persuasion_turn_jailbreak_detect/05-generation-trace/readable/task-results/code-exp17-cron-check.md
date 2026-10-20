# code exp17 cron check

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp17-cron-check_20260519T233515_result.json`
- **Structured JSON:** [`b612d312da9bb433e91f.json`](../../sessions/b6/b612d312da9bb433e91f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
exp17 GPU2 (vanilla + MLM pipeline): PARTIAL — crashed after MLM Stage1 seed=42
exp17 GPU3 (9-class pipeline): SUCCESS — all 3 seeds × 2 stages complete
exp17 总完成度: 10/15 steps
exp16 eval: COMPLETED (但 summary 全 N/A，需检查)
```

详细分析：

### exp17 GPU2 — partial failure

| Step | Status |
|------|--------|
| vanilla_seed{42,123,456} | ✓ 3/3 完成 |
| mlm_seed42 Stage1 (DeBERTa MLM) | ✓ 完成 (4 epochs, val_mlm_loss=4.076) |
| mlm_seed42 Stage2 (GRU) | ✗ 未启动 (`mlm_stage2_seed42.log` 不存在) |
| mlm_seed{123,456} S1+S2 | ✗ 未执行 |

**原因**: 脚本 `set -e`，MLM Stage1 seed=42 完成后（checkpoint 07:34 保存），启动 Stage2 时失败立即退出。训练输出因 Python stdout buffering + pipe 到 tee 未刷入日志，无法看到具体错误。怀疑 checkpoint 格式问题 — Stage1 保存为 safetensors 格式，Stage2 (`train_classifier.py --deberta_checkpoint`) 可能期望不同格式。

### exp17 GPU3 — success

所有 9class_seed{42,123,456} 的 Stage1 (deberta_multitask) 和 Stage2 (treatment GRU) 均完成。最后一个 checkpoint 07:35:45 保存。进程正常退出。

### exp17 缺失清单

1. `mlm_seed42` Stage2 GRU
2. `mlm_seed123` Stage1 + Stage2
3. `mlm_seed456` Stage1 + Stage2

共 5 个 step 未完成，全在 MLM pipeline。

### exp16 eval — completed

64 个结果文件已生成（vanilla 21 + mlm_only 21 + 9class ~21）。eval 脚本已于 07:40:39 结束 (`=== Done ===`)。但 summary 表中所有 variant 的 macro F1 显示 N/A，aggregation 可能有解析问题，需要检查单个 result JSON 确认数据是否正确。

---
