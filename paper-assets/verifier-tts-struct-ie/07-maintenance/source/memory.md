# Memory — verifier-tts-struct-ie

## MVP 最终判定: FAIL (2026-05-11)

Training-free TTS（parallel 和 sequential）不适用于 SciERC NER/RE。

### 全部实验汇总

| 实验 | 方法 | 最佳 ΔF1 vs greedy | 结论 |
|------|------|-------------------|------|
| mvp-001 | Exact SC | +0.17 (N=8) | negative |
| mvp-001 | IoU SC | +0.19 (N=8) | negative |
| mvp-001 | Freq merge | +0.66 (N=8,k=2) | negative |
| mvp-001 | Weighted merge | +0.13 (N=8) | negative |
| mvp-003 | LLM Verifier | -0.07 (N=8) | negative |
| mvp-004 | Sequential refine | +0.12 (K=2), -0.23 (K=4) | negative |
| mvp-002 | RE exact SC | +0.15 (N=4) | negative |
| mvp-002 | RE freq merge | +0.31 (N=4,k=2) | negative |
| **Pass 阈值** | | **≥1.0pt** | |
| **Oracle gap** | | **+6.49pt (NER N=16)** | **diversity exists** |

### 核心教训

#### 1. Oracle gap ≠ 可利用的 gap
6.49pt 的 oracle gap 证明好答案在候选中，但没有 unsupervised signal 能定位它。这是一个 fundamental limitation。

#### 2. Per-entity voting 对 IE 无效
根因：entity 集合多样性（不是 span 边界差异）。不同候选的 entity 数量和组合差异大。

#### 3. 同模型自验证/自修正无效
- Verifier: Pearson 0.09，同模型无法评估自己的输出质量
- Sequential refine: precision 退化，模型在修正时引入更多错误

#### 4. RE baseline 太低
Qwen3-8B zero-shot RE 仅 6.2%，说明 IE 任务对 LLM 仍然很难。

### 环境经验
- seetacloud-bjb2-structtts: root, /root/projects/..., conda base
- ModelScope 下载模型（HF 被阻断）
- vLLM n=8/16 会 OOM，需循环调用
- Qwen3-8B NER JSON parse 99.99%
- SciERC test 100 docs
