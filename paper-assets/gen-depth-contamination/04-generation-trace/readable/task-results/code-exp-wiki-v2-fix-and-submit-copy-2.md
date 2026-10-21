# code exp wiki v2 fix and submit

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_wiki_v2_fix_and_submit_20260517T120104_result.json`
- **Structured JSON:** [`8c2692ec0b30da355004.json`](../../sessions/8c/8c2692ec0b30da355004.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

**总结：**

1. **Pipeline 修复**：
   - `generate_depth_chain` 已有 model mismatch 检查（读取 first record 的 `model_name`，不匹配则 WARNING + 强制重新生成）
   - 补充修复了 `extract_all_features` 的 skip 逻辑：新增 mtime 检查，如果任何 depth file 比 features.csv 更新则强制重新提取

2. **独立数据目录**：已创建并填充
   - `data/exp_wiki_pythia/`: depth_0 (5000 seed) + depth_1 (5000, model_name=Pythia-1.4B) ✓
   - `data/exp_wiki_olmo/`: depth_0 (5000 seed) + depth_1 (5000, model_name=OLMo-1B-hf) ✓

3. **实验状态**：两个 v2 实验已在运行中（~16 分钟前启动）
   - `exp_wiki_pythia_v2` (cuda:2): depth 2 生成中，25% (77/313 batches)
   - `exp_wiki_olmo_v2` (cuda:3): depth 2 生成中，50% (156/313 batches)
   - Registry 已有完整 spec 记录

预计每个实验总计约 1 小时内完成（5 depths × ~13min/depth + features extraction + analysis）。

---
