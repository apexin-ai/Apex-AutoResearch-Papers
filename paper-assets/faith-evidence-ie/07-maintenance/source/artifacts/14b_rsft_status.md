# 14B RSFT Pipeline Status (2026-05-21)

## 1. Generation ✅ 完成
- **PID 33608**: 已结束
- **完成时间**: 2026-05-21 02:07
- **输出**: `/root/autodl-tmp/rsft_generations_14b/generations.jsonl`
- **统计**: 3027 docs, 24216 generations (8 per doc)
- **质量**: format_ok 100.0%, mean diversity 7.28/8, truncation ~7%
- **运行时间**: ~2h31m (从 doc 2553 恢复的 r4 run，474 batches)

## 2. CED Scoring ✅ 完成
- **完成时间**: 2026-05-21 03:09
- **输出**: `/root/autodl-tmp/rsft_scored_14b/`
- **选择策略**: top_k=1, scoring_mode=ced (format 0.2 / f1 0.4 / ced 0.4)
- **统计**: 24216 → 3015 selected (12.5%), 覆盖 3015/3027 docs
- **Selected 质量**:
  - f1_reward: mean=0.730, median=0.750
  - ced_reward: mean=0.690, median=0.710
  - combined: mean=0.768, median=0.770

## 3. RSFT Training ✅ 完成
- **完成时间**: 2026-05-21 04:23
- **输出**: `/root/autodl-tmp/rsft_output_14b/` (checkpoint-1131, 3 epochs)
- **训练时间**: ~66 min (3958s)
- **最终指标**: loss=0.500, mean_token_accuracy=0.878, entropy=0.491

## 4. Eval: no-evidence ✅ 完成
- **完成时间**: 2026-05-21 07:56
- **输出**: `/root/autodl-tmp/eval_results/plan017_14b_rsft_no_evidence_eval/`
- **指标**:
  - F1 = 55.36, ign_F1 = 54.32
  - Precision = 54.14, Recall = 56.64
  - format_ok = 96.8%, truncation = 106/985 docs
- **推理时间**: 9428s (~2h37m)

## 5. Eval: with-evidence ❌ 未完成
- 无 `eval_14b_rsft` 或 `plan017_14b_rsft_eval` 目录

## 下一步
1. **运行 with-evidence eval**: 用 RSFT adapter (`/root/autodl-tmp/rsft_output_14b/checkpoint-1131`) 在 dev set 上跑带 evidence 的 eval，获取 evi_f1_joint 和 EDCR 指标
2. **与 SFT baseline 对比**: 14B SFT eval 已有 (`eval_14b_sft`, `eval_14b_sft_no_evidence`)，需汇总对比 SFT vs RSFT
