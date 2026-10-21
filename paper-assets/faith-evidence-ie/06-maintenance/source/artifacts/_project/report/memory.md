# Project Memory

## D102 RSFT k=1 训练结果 (2026-05-18)

**状态: 4/4 全部 SUCCESS**

D102 方法论修正：将所有模型的 RSFT 从 k=3 改为 k=1，与论文声明和 4B canonical 一致。

### 训练结果汇总

| exp_id | Model | Seed | Samples | Steps | train_loss | token_acc | Runtime | Checkpoint |
|--------|-------|------|---------|-------|------------|-----------|---------|------------|
| d102_1_7b_rsft_k1_s42 | Qwen3-1.7B | 42 | 3021 | 567 | 0.3063 | 0.8731 | 15m | checkpoint-567 |
| d102_llama_rsft_k1_s42 | LLaMA-3.1-8B | 42 | 2952 | 1107 | 0.3698 | 0.8876 | 43m | checkpoint-1107 |
| d102_8b_rsft_k1_s42 | Qwen3-8B | 42 | 3018 | 1134 | 0.3877 | 0.8579 | 49m | checkpoint-1134 |
| d102_8b_rsft_k1_s43 | Qwen3-8B | 43 | 3018 | 1134 | 0.3862 | 0.8735 | 48m | checkpoint-1134 |

### k=1 vs k=3 训练指标对比

| Model | k=1 loss | k=3 loss | k=1 samples | k=3 samples | k=1 steps | k=3 steps |
|-------|----------|----------|-------------|-------------|-----------|-----------|
| Qwen3-1.7B | 0.3063 | 0.5234 | 3021 | 9042 | 567 | 1698 |
| Qwen3-8B (s42) | 0.3877 | 0.3008 | 3018 | 9041 | 1134 | 3393 |
| LLaMA-8B | 0.3698 | N/A | 2952 | 8829 | 1107 | 3312 |

### Checkpoint 路径
- 1.7B: `/root/autodl-tmp/rsft_output_qwen3_1_7b_k1/checkpoint-567` (adapter: 279MB)
- LLaMA-8B: `/root/autodl-tmp/rsft_output_llama_3_1_8b_k1/checkpoint-1107` (adapter: 640MB)
- 8B s42: `/root/autodl-tmp/rsft_output_qwen3_8b_k1/checkpoint-1134` (adapter: 666MB)
- 8B s43: `/root/autodl-tmp/rsft_output_qwen3_8b_k1_s43/checkpoint-1134` (adapter: 666MB)

### 8B seed 稳定性
- s42 train_loss=0.3877, s43 train_loss=0.3862 (delta=0.0015, 非常稳定)

### 下一步: 需要 eval 验证 k=1 vs k=3 的 rel_f1 差异

## plan_006_qwen3_1_7b_rsft_test 分析 (2026-05-18)

**状态: SUCCESS (有显著质量问题)**

### 基本信息
- 模型: Qwen3-1.7B + SFT adapter + RSFT LoRA (checkpoint-1698)
- 数据: DocRED test split, 1000 documents
- 推理时间: 10806.3s (~3h), 10.81 s/doc, batch_size=4, max_new_tokens=1024
- no_evidence: false (with evidence 模式)

### 输出文件
| 文件 | 大小 | 路径 |
|------|------|------|
| codalab_submission.json | 2.5MB | /root/autodl-tmp/eval_results/plan_006_qwen3_1_7b_rsft_test/ |
| predictions.json | 8.6MB | 同上 |
| metrics.json | 705B | 同上 |

### 关键指标
- Test documents: 1000
- Documents with predictions: 994 (6 docs 无预测)
- Total CodaLab entries: 27567
- **Unique entries: 15338, Duplicates: 12229 (44.4%)**
- Unique relations (ignoring evidence): 15241, Relation-level duplicates: 12326
- Format OK: 999/1000 (99.9%)
- **Truncated: 857/1000 (85.7%)**

### 问题分析

**问题 1: 极高截断率 (85.7%)**
- 857/1000 文档在生成时触及 max_new_tokens=1024 限制被截断
- 截断意味着许多文档的关系预测不完整，recall 会显著受损
- 1.7B 模型生成冗长，1024 tokens 不够覆盖大多数文档的全部关系

**问题 2: 大量重复预测 (44.4%)**
- 27567 条预测中有 12229 条完全重复（包含 evidence 完全相同）
- 模型在截断边界附近可能出现重复生成
- 虽然 CodaLab 评测可能会去重，但这浪费了宝贵的生成 token 预算，加剧截断问题

**问题 3: 6 个文档无预测**
- 994/1000 文档有预测输出，6 个文档完全缺失

### 结论
推理流程成功完成（EXIT_CODE=0），CodaLab 提交文件已生成。但预测质量受严重截断和重复影响。可提交 CodaLab 获取 baseline 分数，但预期 F1 会因截断导致的 recall 损失而偏低。

### 改进建议
1. 增大 max_new_tokens（如 2048 或 3072）减少截断
2. 在后处理中去重，节省 token 预算
3. 如果模型本身倾向于重复生成，考虑在 generation config 中加 repetition_penalty
