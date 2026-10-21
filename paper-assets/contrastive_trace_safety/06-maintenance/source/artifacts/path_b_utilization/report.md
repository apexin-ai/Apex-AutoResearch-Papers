# Path B 数据利用率分析

## 当前状态

| 模型 | 已提取 | 可提取 (jailbreak+CP) | Jailbreak无CP | Safe | 总traces | 总sentences |
|------|--------|----------------------|---------------|------|----------|-------------|
| R1-32B | 100 | 100 | 50 | 71 | 221 | 8,525 |
| QwQ-32B | 95 | 95 | 5 | 40 | 140 | 7,007 |

**关键发现：所有符合当前筛选条件的 traces 已经 100% 提取完毕。不存在"未提取"的数据。**

任务描述中的 8,525/7,007 是 sentence（行）数，不是 trace 数。实际 trace 数分别为 221/140。

### 当前 train/test 分割 (60/20/20)

- R1-32B: train=60, val=20, **test=20**
- QwQ-32B: train=57, val=19, **test=19**

## 筛选逻辑

### 筛选条件（两层过滤）
1. `final_judgment == 1.0`（必须是 self-jailbreak trace）
2. `extract_commitment_point(labels) is not None`（必须有 commitment point）

### Commitment Point 定义
- 代码位置：`src/data_loader.py:extract_commitment_point()`
- 逻辑：找到最后一个 safety label（RA/AL/CC/ED/IA）的位置，CP = last_safety_idx + 1
- 失败条件：
  - 无 safety label → CP=None
  - 最后一个 safety label 在 trace 末尾 → CP=None（无 post-commitment 段）

### 被排除的 traces 分析
- R1-32B: 50 条 jailbreak 无 CP → **全部是 safety label 出现在末尾位置**（模型最终拒绝了，但 final_judgment 仍标为 jailbreak）
- QwQ-32B: 仅 5 条无 CP，同样原因

### CP 标注方式
- **完全自动**，基于 HarmThoughts 数据集中已有的 `llm_annotation` 字段
- 无需人工标注，无需额外脚本
- 新 traces 只要有 `llm_annotation` 就能自动计算 CP

## 扩展方案

### 方案 A：放宽筛选条件（不需要新数据，不需要新提取）

**问题：无法直接放宽。** 50 条无 CP 的 R1-32B traces 全部是 safety label 在末尾，意味着没有 pre→post commitment 转换，无法用于当前的二分类框架。

### 方案 B：利用 Safe traces 做 FPR 评估

- R1-32B 有 71 条 safe traces，QwQ 有 40 条
- 这些 traces 可用于 false positive rate 评估（已有代码支持）
- 但无法增加 jailbreak test traces 数量

### 方案 C：跨模型数据利用

- R1-8B 有 209 条 jailbreak+CP traces（已提取 268 条 hidden states，含 safe）
- 但 R1-8B 是不同模型，hidden states 维度不同（4096 vs 5120），不能直接混用

### 方案 D：重新定义 CP（最可行的扩展路径）

对 50 条被排除的 R1-32B traces，可以尝试：
1. 使用**非末尾的最后一个 safety label** 作为 CP（即使之后还有 safety label）
2. 或使用**第一个 non-safety label** 作为分界
3. 需要验证这些 traces 是否确实有有意义的 pre/post 区分

**但这改变了实验的核心假设，需要谨慎评估。**

## 时间与资源估算

### GPU 配置
- 2x NVIDIA RTX PRO 6000 Blackwell (98GB each)
- 32B fp16 模型轻松装入单卡（~64GB）

### 模型缓存
- R1-32B: `/root/autodl-tmp/.hf_cache/deepseek-ai/DeepSeek-R1-Distill-Qwen-32B` ✓
- QwQ-32B: `/root/autodl-tmp/.hf_cache/Qwen/QwQ-32B` ✓

### 提取性能（已完成的 100 条 R1-32B）
- 总 tokens: 64,727（avg 647/trace）
- 总 steps: 3,506（avg 35.1/trace）
- 每 trace 输出大小: ~22MB（64 layers × 5120 dim × num_sentences × fp16）
- 估计提取速度: ~10-15s/trace

### 如果要提取额外 50 条（无 CP 的 jailbreak）
- 时间: ~8-12 min（50 traces × 10-15s）
- 存储: ~1.1GB 额外
- **前提：必须先解决这些 traces 没有 CP 的标注问题**

## 结论

### 核心问题

**n=20 test traces 的瓶颈不是提取不充分，而是数据集本身只有 100 条符合条件的 R1-32B traces。**

当前 test set 大小：
- R1-32B: 20 traces
- QwQ-32B: 19 traces

### 扩展到 n≥40 test traces 的路径

1. **最快路径：调整 train/test 比例**
   - 将 split 从 60/20/20 改为 50/10/40
   - R1-32B: train=50, val=10, test=40
   - 代价：training data 减少，probe 性能可能下降
   - 时间：0 min（只改代码中的 split ratio）

2. **次快路径：合并 R1-32B + QwQ-32B 数据**
   - 两模型结构相同（Qwen2-32B 架构，64 layers，5120 dim）
   - 合并后：195 traces → test=39（20% split）或 test=59（30% split）
   - 需要验证跨模型泛化性
   - 时间：几小时实验验证

3. **中等路径：对 50 条无 CP traces 设计替代标注方案**
   - 利用已有 llm_annotation 设计新的 CP 定义
   - 需要提取 hidden states（~10 min）
   - 需要验证新标注下 probe 是否仍有效
   - 时间：1-2 小时（含设计、提取、验证）

4. **最激进路径：增加数据来源**
   - HarmThoughts 数据集不够大
   - 需要用其他 jailbreak 数据集生成新 traces
   - 需要完整 pipeline：生成 → 标注 → 提取
   - 时间：天级别

### 推荐

**路径 1（调整 split）+ 路径 2（合并模型）组合** 是最快达到 n≥40 的方式，零额外计算成本。
