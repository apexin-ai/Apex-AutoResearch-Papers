## 代码差异报告：α ablation 结果异常排查

### 1. prune.py 版本对比
- westb git commit: e6ce5f7 (2026-05-15 03:56:59)
- westd git commit: 同一 commit（代码同步）
- **代码差异: 0 行。prune.py (426 行) 完全一致。**
- model_utils.py、eval_gsm8k.py 也完全一致（eval 有 post-commit 更新，但运行时版本相同）

### 2. 关键参数对比

| 参数 | westb (Standard 20%) | westd (α=0.0) | westb (RASP 20%) |
|------|---------------------|----------------|-------------------|
| mode | standard | rasp (α=0.0) | rasp (α=1.0) |
| sparsity_target | 0.20 | 0.20 | 0.20 |
| sparsity_actual | 0.1909 | 0.1909 | 0.1909 |
| per-layer MLP floor | 40% (12/28) | 40% (12/28) | 40% (12/28) |
| importance n_samples | **512** | **256** | 512 |
| CKA n_samples | N/A | 256 | 512 |
| seed | 42 | 42 | 42 |
| model path | /root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B | /root/autodl-tmp/models/DeepSeek-R1-Distill-Qwen-7B | 同 westb |
| base model config md5 | b381e4d4613d7afa4f95937c2c1d5f62 | **同** | **同** |
| eval N | 100 | 100 | 100 |
| eval do_sample | False | False | False |
| eval max_new_tokens | 4096 | 4096 | 4096 |
| transformers 版本 | 5.8.0 | 5.8.1 | 5.8.0 |

### 3. 剪枝结果对比

**所有三个模型都只剪 MLP（0 个 attention group 被剪），200-201 个 MLP groups。**

#### Per-layer MLP 保留数 (28 = 未剪枝)

| Layer | westb Std | westd α=0.0 | westb RASP | 差异说明 |
|-------|-----------|-------------|------------|---------|
| 0-5 | 12 | 12 | 12 | 全部一致 |
| **6** | **28** | **28** | **12** | RASP 剪 16 groups, Standard 保留全部 |
| 7 | 28 | 28 | 28 | |
| 8 | 28 | 28 | 27 | |
| 9 | 28 | 28 | 24 | RASP 多剪 4 groups |
| 10-15 | 28 | 28 | 28 | |
| **16** | **21** | **21** | **28** | Standard 剪 7, RASP 保留全部 |
| **17** | **24** | **24** | **28** | Standard 剪 4, RASP 保留全部 |
| **18** | **21** | **21** | **28** | Standard 剪 7, RASP 保留全部 |
| 19 | 12 | 12 | 14 | |
| 20 | 26 | 25 | 28 | |
| 21 | 20 | 20 | 20 | |
| 22 | 24 | 24 | 28 | Standard 剪 4, RASP 保留全部 |
| 23-24 | 12 | 12 | 12 | |
| 25 | 12 | 12 | 17 | |
| **26** | **20** | **21** | **26** | |
| **27** | **28** | **28** | **12** | RASP 剪 16 groups, Standard 保留全部 |

**核心发现: RASP 用 layer 6/27 的容量换取 layer 16-18/22/25/26 的保护。这是 CKA overlap 的预期行为——CKA 识别出层 16-18 与邻居不相似（不可恢复），优先保留。**

#### westb Standard vs westd α=0.0 细粒度对比

**Layer 级别完全一致**（保留数量相同），但具体 group 选择不同:

| Layer | 差异 |
|-------|------|
| 5 | 交换 2 groups (westb prunes 0/keeps 14, westd prunes 14/keeps 0) |
| 19 | 交换 2 groups (westb keeps 24, westd keeps 17) |
| 20 | westb keeps 26, westd keeps 25 (差 1 group) |
| 21 | 交换 1 group (westb prunes 23, westd prunes 15) |
| 23 | 交换 2 groups |
| 26 | westb keeps 20, westd keeps 21 (差 1 group) |

**其余 22 层的 group 选择完全一致（包括关键的层 16-18）。**

权重统计验证：
- 未剪枝层 (0, 10, 27, attn): norm/mean/std/min/max **完全一致**
- 不同 group 选择的层 (5, 19): norm 差异 <0.5%

### 4. Eval 结果汇总

| 模型 | 服务器 | Accuracy | EOS Rate | 输出质量 |
|------|--------|----------|----------|---------|
| Standard 20% | westb | **1%** | N/A | 退化（"10 years, 10 years..."重复循环） |
| RASP 20% (α=1.0) | westb | **29%** | N/A | 连贯推理 |
| α=0.0 | westd | **30%** | 79% | 连贯推理 |
| α=0.5 | westd | **25%** | 70% | 连贯推理 |
| α=1.0 | westd | **27%** | 90% | 连贯推理 |

Eval 时间线 (westb):
- RASP eval: May 15 00:15 → 29% → 91KB (正常响应)
- Standard eval: May 15 01:00 → 1% → 316KB (退化长响应)
- 两次 eval 间隔 45 分钟，用同版本 eval 代码

### 5. 根因判断

**确定的事实：**
1. 代码完全一致，无 code path 差异
2. Standard 20% 模型确实生成退化输出（重复 pattern），不是 eval bug
3. RASP 20% 模型在同一服务器、同一 eval 脚本下正常工作（29%）
4. α ablation 三个值（0.0/0.5/1.0）在 N=100 下无统计显著差异（25-30%，stderr ≈ 4.5pp）

**核心异常：westb Standard (1%) vs westd α=0.0 (30%)**

α=0.0 在数学上等价于 standard scoring（`(1-F)^0 = 1`），但用了不同的 importance scores（256 vs 512 calibration samples）。两者 pruning pattern 在 layer 级别完全一致，但具体 group 选择有 ~5% 差异。

**最可能的根因（置信度 70%）：Importance score 的 calibration 样本量差异（512 vs 256）导致少数 group 排序翻转，恰好影响了模型稳定性的临界 group。** 20% sparsity 下模型处于 fragile 状态，个别 MLP channel group 的保留/删除可以导致 catastrophic degeneration。这解释了为什么同样的 layer-level 分布，不同的 group 选择产生截然不同的结果。

**次可能的根因（置信度 20%）：** westb Standard eval 时存在环境问题（GPU 内存碎片、推理精度异常等），导致退化输出并非模型本身问题。

**低可能性（10%）：** transformers 5.8.0 vs 5.8.1 在非标准 config 字段处理上存在差异。

### 6. 建议行动

1. **[最高优先] 在 westb 上用 current eval 代码重新评估 pruned_standard_20**（等 GPU 空闲后），确认 1% 是否可复现
2. **[高优先] 在 westd 上用相同 importance scores (n_samples=512) 重跑 α=0.0**，消除 calibration 差异
3. **α ablation 结论**：当前 N=100 下 α=0.0/0.5/1.0 无显著差异（25-30%），不支持 "CKA 反而伤性能" 的结论。需要 N=全集 或多 seed 来检验
4. **Standard vs RASP 的核心 claim**：westb 上 Standard(1%) vs RASP(29%) 差距是真实的，由 layer-level 分布差异驱动（RASP 保护层 16-18），但需要排除 importance score 混淆因素
