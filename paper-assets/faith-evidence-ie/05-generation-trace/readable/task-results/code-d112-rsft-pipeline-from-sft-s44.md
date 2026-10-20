# code d112 rsft pipeline from sft s44

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d112_rsft_pipeline_from_sft_s44_20260518T225112_result.json`
- **Structured JSON:** [`a30ee5e422479315747a.json`](../../sessions/a3/a30ee5e422479315747a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

D112 pipeline 准备完成。

**已创建 4 个脚本** (`/root/autodl-tmp/scripts/d112/`):

| 步骤 | 脚本 | GPU | 预估时间 |
|------|------|-----|----------|
| Step 1 | `step1_generate_candidates.sh` | 4 GPU 并行 | ~3-4h |
| Step 2 | `step2_ced_score.sh` | 1 GPU | ~30-60 min |
| Step 3 | `step3_k1_filter_and_train.sh` | 1 GPU | ~1.5-2h |
| Step 4 | `step4_eval.sh` | 1 GPU | ~20-30 min |

**参数来源**: 完全复用 canonical s42 RSFT pipeline 的超参（从 `rsft_gen_shard0.sh` 和 `rsft_scored_s0/rsft_report.json` 提取），仅替换 SFT adapter 为 `sft_output_seed44`。

**关键设计**:
- Step 1 支持 `GPU=X SHARD=Y` 环境变量做 4-GPU 并行 sharding
- Step 2 的 `load_generations` 自动合并 `shard_*/generations.jsonl`
- Step 4 的 eval 正确处理双 adapter 加载链（base → merge SFT s44 → load RSFT）
- 所有脚本 `bash -n` 语法检查通过，所有依赖路径已验证存在

**总预估**: 4-GPU 并行全流程 ~6.5-7.5h。Pipeline plan 已保存至 `artifacts/d112_pipeline_plan.md`。

---
