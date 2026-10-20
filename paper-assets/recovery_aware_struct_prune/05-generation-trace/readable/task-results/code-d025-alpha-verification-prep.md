# code d025 alpha verification prep

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d025-alpha-verification-prep_20260515T092405_result.json`
- **Structured JSON:** [`9634c6a67df146fed4d0.json`](../../sessions/96/9634c6a67df146fed4d0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总报告

### 1. Phase A 结果：Post-Prune Accuracy（calibration=256, eval N=100）

| α | Accuracy | Correct | EOS Rate | Avg Resp Len |
|---:|----------:|--------:|---------:|-------------:|
| 0.0 | **0.3000** | 30/100 | 79% | 1266 |
| 0.5 | 0.2500 | 25/100 | 70% | 1559 |
| 1.0 | 0.2700 | 27/100 | 90% | 817 |
| 2.0 | 0.2900 | 29/100 | 64% | 1958 |
| **4.0** | **0.4000** | 40/100 | 67% | 1979 |

α=4.0 明显最优，比 α=0.0（无恢复惩罚的标准剪枝）高 10 个百分点。非单调趋势：α=0.5/1.0/2.0 反而比 α=0.0 更差。

### 2. Pipeline 状态

- **PID 7186** 仍在运行（已运行 ~1h48m）
- **Phase A**（prune + eval）：✅ 全部完成
- **Phase B**（SFT warmup）：🔄 进行中
  - GPU0: α=0.0 SFT，step ~300/1870（~16%）
  - GPU1: α=0.5 SFT，step ~313/1870（~17%）
  - GPU0 队列：α=0.0 → α=1.0 → α=4.0（3 个 SFT）
  - GPU1 队列：α=0.5 → α=2.0（2 个 SFT）
- **Phase B eval** 尚未开始
- **预计完成时间**：SFT ~84 min + Post-SFT eval ~135 min ≈ **~3.5 小时后**（约 21:00 CST）

### 3. n_samples=512 验证脚本

已上传到 `westd-11672:/root/recovery_aware_struct_prune/scripts/run_alpha_verify_512.sh`

流程：
- Phase 0: 重新计算 importance_scores_512.pt + cka_scores_512.pt（n_samples=512）
- Phase 1: 双 GPU 并行剪枝 α=0.0 和 α=4.0
- Phase 2: 双 GPU 并行 GSM8K eval（N=500）

参数已根据实际代码校准：
- `importance_score.py --n_samples 512`
- `cka_overlap.py --n_samples 512`
- `prune.py --importance_path --cka_path --mode rasp --sparsity 0.20 --alpha --output_path`
- `eval_gsm8k.py --max_samples 500 --max_new_tokens 4096`
- 模型路径：`/root/autodl-tmp/models/DeepSeek-R1-Distill-Qwen-7B`

### 4. 下一步

**未启动验证脚本**——双 GPU 均被 Phase B SFT 占用（81% 利用率）。需等 pipeline 完成后再提交。预估验证脚本运行时间 ~3.5h（importance/CKA 计算 ~30min + prune ~5min + eval N=500 ~3h）。

---
