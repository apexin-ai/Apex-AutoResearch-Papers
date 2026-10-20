# code tracvla spatial probing only

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_tracvla_spatial_probing_only_20260521T042558_result.json`
- **Structured JSON:** [`e2b2cdddf43cd5398894.json`](../../sessions/e2/e2b2cdddf43cd5398894.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run 验证通过。所有 R²=0.0 是预期的（4 个样本无法 fit）。

## 产出总结

### 1. 脚本路径
`/root/autodl-tmp/vla-ssd/scripts/tracvla_spatial_probing_only.py`

### 2. 与 full pipeline 的区别
| | full pipeline | probing-only |
|---|---|---|
| Phase 1 (feature extraction) | 提取 hidden states + L1 attention | 只提取 hidden states（`output_attentions=False`） |
| Phase 2 (R² probing) | ✅ | ✅ |
| Phase 3 (L1 attention) | ✅ | ❌ 跳过 |
| Phase 4 (classification) | ✅ | ❌ 跳过 |
| Phase 5 (counterfactual) | ✅ | ❌ 跳过 |
| 默认 conditions | trained,untrained | trained |
| 模型释放时机 | pipeline 结束后 | Phase 1 后立即释放（probing 不需要模型） |
| 进度打印 | 每 8 层 | 每 4 层 |

### 3. Dry-run 结果
- Phase 1: 4 samples, 6.3s
- Phase 2: 32 layers × 2 positions × 2 seeds, 353s
- 总耗时: 6.2 min
- 输出: `action_r2_probing.json` 已正确写入（dry-run R²=0.0 预期）

### 4. 提交命令
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python /root/autodl-tmp/vla-ssd/scripts/tracvla_spatial_probing_only.py --conditions trained
```

预计运行时间：Phase 1 ~20min（10 tasks × 10 demos × 50 timesteps = 5000 forward passes）+ Phase 2 ~6h（32 层 × 2 positions × 15 seeds）。

---
