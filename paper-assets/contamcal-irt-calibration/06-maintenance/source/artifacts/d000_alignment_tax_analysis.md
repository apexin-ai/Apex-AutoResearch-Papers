# d000 Baseline Gap 分析：SFT Alignment Tax

## 1. d000 (Clean SFT, 0% Contamination) Eval 结果

评估格式：0-shot aligned（instruction-following template）

| Model | Seed | MMLU | GSM8K | HumanEval |
|-------|------|------|-------|-----------|
| Qwen2.5-0.5B | s42 | 39.79% | 36.92% | 46.93% |
| Qwen2.5-1.5B | s42 | 58.53% | 65.43% | 77.22% |
| Qwen2.5-3B | s42 | 62.95% | 35.25% | 81.83% |
| Qwen2.5-3B | s123 | 63.14% | 26.76% | 82.59% |

数据来源：`/root/autodl-tmp/exp001/eval_results/Qwen2.5-{size}_d000_*/eval_results.json`
- 0.5B 和 1.5B 仅有 s42 seed
- 3B 有 s42 和 s123 两个 seed

## 2. HF Base Pretrained 公开分数

来源：[Qwen2.5-LLM 官方博客](https://qwenlm.github.io/blog/qwen2.5-llm/)

| Model | MMLU (5-shot) | GSM8K (4-shot) | HumanEval (0-shot) |
|-------|---------------|----------------|-------------------|
| Qwen2.5-0.5B | 47.5% | 41.6% | 30.5% |
| Qwen2.5-1.5B | 60.9% | 68.5% | 37.2% |
| Qwen2.5-3B | 65.6% | 79.1% | 42.1% |

**⚠️ 评估格式差异**：HF 公开分数使用 few-shot completion 格式，我们的 d000 eval 使用 0-shot aligned（instruction template）格式。两者不完全可比，尤其 GSM8K 的 few-shot CoT prompting 对数学推理帮助极大。

## 3. SFT Alignment Tax（Δ = d000 SFT − Base Pretrained）

| Scale | Seed | MMLU Δ | GSM8K Δ | HumanEval Δ |
|-------|------|--------|---------|-------------|
| 0.5B | s42 | **−7.7pp** | −4.7pp | **+16.4pp** |
| 1.5B | s42 | −2.4pp | −3.1pp | **+40.0pp** |
| 3B | s42 | −2.6pp | **−43.8pp** | **+39.7pp** |
| 3B | s123 | −2.5pp | **−52.3pp** | **+40.5pp** |

### 关键发现

**A. MMLU：一致的小幅负 tax**
- 0.5B 降幅最大（−7.7pp），1.5B 和 3B 降幅相近（−2.4~2.6pp）
- 0.5B 的大降幅可能部分来自 few-shot vs 0-shot 格式差异（小模型对 few-shot 示例依赖更强）
- 跨 scale 方向一致，量级合理

**B. GSM8K：3B 出现异常大幅退化**
- 0.5B（−4.7pp）和 1.5B（−3.1pp）的退化幅度合理
- **3B 退化 43.8~52.3pp，且两个 seed 间差异巨大（35.3% vs 26.8%）**
- 可能原因：
  1. 评估格式效应：base 用 4-shot CoT，我们用 0-shot aligned。3B 模型可能对 CoT prompting 依赖更强
  2. SFT 训练数据结构问题：d000 SFT 数据中数学推理样本不足，3B 的 instruction following 能力反而干扰了数学推理
  3. 训练 instability：两个 seed 差异 8.5pp，说明 3B GSM8K 对训练随机性极为敏感
- **需要排查**：检查 d000 SFT 训练数据中 math reasoning 样本占比

**C. HumanEval：一致的大幅提升**
- 所有 scale 提升 16~40pp，且 1.5B/3B 提升幅度相近（~40pp）
- 这是 SFT 的预期效果——instruction-following 格式极大提升代码生成任务
- 0.5B 提升较小（+16.4pp），可能因为 0.5B 容量有限，SFT 后的 instruction-following 能力上限较低

## 4. 对 IRT Gamma 解读的影响

### 4.1 直接影响
SFT alignment tax 的存在意味着 **d000 模型的 benchmark 分数 ≠ base pretrained 的 benchmark 分数**。当 IRT 模型用 d000 作为 baseline 时，gamma 估计的含义是：

> gamma = contaminated SFT 模型与 **clean SFT 模型** 的差异

而非与 base pretrained 模型的差异。**这实际上是正确的设计**——因为我们关心的是 contamination 的效应，而非 SFT + contamination 的混合效应。

### 4.2 Cross-Scale Theta 偏差问题
MMLU alignment tax 跨 scale 不一致（0.5B: −7.7pp vs 1.5B/3B: −2.5pp）。如果 IRT theta 是从 d000 的 response pattern 估计的：
- 0.5B 的 theta 会被系统性低估（因为 SFT tax 更大）
- Cross-scale pooled IRT 的 theta 差异部分来自 SFT tax 的 scale-dependent 差异，而非纯粹的能力差异
- **但** 这个 bias 方向是让 0.5B 的 theta 偏低，contamination gamma 如果是正的（提升），那这个 bias 会让 0.5B 的 contamination 效应看起来更大——这反而是保守的（让我们更容易检测 contamination）

### 4.3 GSM8K 3B 异常的影响
3B GSM8K 的 d000 baseline 极低且不稳定（35.3% vs 26.8%），这意味着：
- 3B 在 GSM8K 上的 gamma 估计会偏高（因为 baseline 被人为压低）
- **seed 间差异 8.5pp 远大于其他 benchmark 的 seed 间差异**
- 建议：在 IRT 分析中，3B GSM8K 的 gamma 需要谨慎解读，或在 cross-scale 分析中标注此异常

### 4.4 建议
1. **使用 d000 作为 baseline 而非 base pretrained**——这已经控制了 SFT tax，是正确的做法
2. **在论文中报告 SFT alignment tax**——让读者了解 d000 baseline 与 base pretrained 的差距
3. **GSM8K 3B 异常需要进一步调查**——可能需要检查 eval 代码、SFT 数据、或增加 seed 数量
4. **考虑 scale-specific theta calibration**——如果 MMLU alignment tax 的 scale 依赖性影响了 cross-scale IRT，可以在 IRT 模型中加入 scale 作为协变量
