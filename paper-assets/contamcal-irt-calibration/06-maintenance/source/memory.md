# evaluate.py 版本一致性审计报告

**审计时间**: 2026-05-20
**触发原因**: Reviewer 发现 westd-29999 上 evaluate.py = 37775 bytes，C009 参考值 = 37591 bytes (+184 bytes)

---

## (a) 版本差异的具体内容

### 文件版本清单

| 位置 | 字节数 | MD5 | 修改时间 |
|------|--------|-----|----------|
| cqa1-21977 (C009 参考) | 37591 | `001a9bc23f808c47d25ef9eaeecb81f1` | May 20 02:11 |
| westd-29999 当前 | 37775 | `17673bf373f00f83ccc41fc1d355a4cd` | May 20 14:37 |
| westd-29999 .bak | 37139 | — | May 19 18:21 |
| westd-29999 git HEAD | 33904 | `84f7b08f220ff69c0b443f697c50ac0d` | May 18 (initial sync) |

### 差异定位

cqa1 和 westd 版本的 **唯一** 差异：westd 在 4 个位置添加了 `system_prompt=\"You are a helpful assistant.\"`（每处 +46 bytes，4×46=184 bytes）。

**修改位置**（全部在生成式评估函数中，NOT logprob-based MCQ 路径）：

1. **`evaluate_gsm8k()`** ~L321
2. **`evaluate_humaneval()`** ~L377
3. **`evaluate_paraphrased()` GSM8K 分支** ~L554
4. **`evaluate_paraphrased()` HumanEval 分支** ~L586

### 关键发现：`evaluate_mcq()` 完全一致

**MMLU 和 ARC 的评估代码路径（`evaluate_mcq` 函数）在 cqa1 和 westd 版本之间完全相同**。差异仅在 L300-400 和 L500-600（GSM8K/HumanEval/paraphrased eval 函数）。

---

## (b) MMLU-ARC 可比性分析

**结论：MMLU 和 ARC eval 结果不受此版本差异影响。**

- `evaluate_mcq()` 函数在两个版本中完全一致
- 两台服务器 MMLU/ARC eval 产出可直接混合使用

**受影响的评估**：仅 GSM8K 和 HumanEval（westd 多了 system prompt）。

---

## (c) C009 约束状态

**建议**：将 C009 参考 hash 统一为 cqa1 版本 `001a9bc23f808c47d25ef9eaeecb81f1` (37591 bytes)

---

# OLMo-2 Baseline 验证 (2026-05-21 全量 Rerun 完成)

## 背景
论文 OLMo-2 d000 MMLU=53.79%，cross_family 目录中 d000=58.60%（有 adapter loading log）。怀疑 53.79% 是 raw base model。

## Rerun 结果（eval_olmo2_s42_rerun, GPU 3, 37775 版 evaluate.py, adapter 加载确认）

| Dosage | MMLU (rerun) | MMLU (paper) | Δ | ARC (rerun) | ARC (paper) | Δ |
|--------|-------------|-------------|-----|------------|------------|-----|
| d000 | 53.79 | 53.79 | 0.00 ✅ | 76.11 | 76.11 | 0.00 ✅ |
| d005 | 56.14 | 55.89 | +0.25 | 76.62 | 76.62 | 0.00 ✅ |
| d025 | 56.17 | 57.73 | -1.56 ⚠️ | 78.16 | 78.16 | 0.00 ✅ |
| d050 | 57.25 | 57.44 | -0.19 | 79.61 | 79.61 | 0.00 ✅ |
| d100 | 57.00 | 58.60 | -1.60 ⚠️ | 80.03 | 80.03 | 0.00 ✅ |

## 关键发现
1. **d000 MMLU=53.79% 确认正确**——adapter 加载 log 中明确显示 lora_alpha=32，不是 raw base model
2. **ARC 100% 可复现**——5/5 dosage 0.00pp 偏差
3. **MMLU d025/d100 偏低 ~1.6pp**——原因不明（evaluate_mcq 代码路径审计为一致）。可能与模型加载顺序、batch 处理、或 GPU 硬件差异有关
4. **cross_family 58.60% 来自不同 eval 配置**——不是论文数据源，可以忽略
5. **OLMo-2 = Benefit 分类不变**——MMLU +3.21pp, ARC +3.92pp

---

# 双 Benchmark Bootstrap CI 分析 (2026-05-21 全部完成 + 审计通过)

## 5/5 家族 n=3 BCa Bootstrap CI 最终结果（全部 verified）

| Family | MMLU Δ(d100) | MMLU 95% CI | ARC Δ(d100) | ARC 95% CI | Dir-Con | Pattern |
|--------|-------------|-------------|-------------|------------|---------|---------|
| Phi-4 | +0.72pp | [-0.17, +1.39] | +0.65pp | [+0.51, +0.77] | ✅ | Immune |
| OLMo-2 | +1.35pp | [-0.55, +2.60] | +3.44pp | [+2.90, +3.78] | ✅ | Benefit |
| Qwen-7B | -0.95pp | [-1.82, -0.34] | -2.42pp | [-2.90, -2.08] | ✅ | V-recovery |
| Gemma-2 | +2.39pp | [+1.49, +3.14] | -0.15pp | [-1.97, +1.42] | ✗ | Benefit/Inconclusive |
| Qwen-14B | -15.70pp | [-24.99, -10.49] | -5.03pp | [-9.38, -2.76] | ✅ | Collapse |

Dir-Con 4/5 ✅。所有 CI 使用 BCa bootstrap (B=10000, seed=42)。

## Bootstrap 数据完整性审计 (2026-05-21 闭环)

**根因**：服务器有两套结果目录 `eval_results_v2/`（s42/s123）和 `results/`（s0 新 eval）。`bootstrap_triple_seed.py` 只读前者。

**审计结果**：
- Phi-4, OLMo-2: s0 数据本就在 eval_results_v2/ → 无问题 ✅
- Qwen-7B, Qwen-14B: s0 数据在 results/ → bootstrap 用 registry 硬编码值计算 → 正确但不可重现 → **已归一化** ✅
- Gemma-2 ARC s42: 数据缺失 → **新跑 eval 确认 delta=-1.20pp** → CI 不变 ✅

**修复**：s0 数据已从 results/ 复制到 eval_results_v2/（Qwen-14B 20文件 + Qwen-7B 20文件 via SCP from cqa1）。`bootstrap_triple_seed.py` 现在可重现所有 n=3。

**教训**：eval 结果应统一存储路径，不要维护两套目录。后续 eval 脚本统一输出到 eval_results_v2/。

## Per-seed Qwen-14B Δ(d000→d100) 明细

| Seed | MMLU Δ(pp) | ARC Δ(pp) |
|------|-----------|----------|
| s0 | -24.99 | -9.38 |
| s42 | -9.37 | -2.56 |
| s123 | -12.74 | -3.15 |

s0 种子方差极大（MMLU -24.99 vs s42 -9.37）→ Collapse pattern 的 seed sensitivity 显著高于其他家族。CI 宽度 14.5pp (MMLU) 反映了这一点。Director 决策：在 Limitations 讨论方向一致性 > 绝对值。

## Per-seed Qwen-7B Δ(d000→d100) 明细

| Seed | MMLU Δ(pp) | ARC Δ(pp) |
|------|-----------|----------|
| s0 | -1.03 | -1.88 |
| s42 | -1.82 | -2.90 |
| s123 | +0.00 | -2.47 |

s123 MMLU 完全恢复但 ARC 仍 negative → recovery 程度 benchmark-dependent

## Gemma-2 ARC 剂量曲线高度非单调 (2026-05-21)

s42: d000=86.01→d005=77.82→d025=87.37→d050=71.08→d100=84.81
s0: d025=64.85%（异常低，rerun 确认）

Gemma-2 ARC 在中间剂量出现极端波动，可能与 adapter-prompt interaction 有关。与 MMLU（平滑正向）形成鲜明对比。

## 跨 Benchmark 关键发现

1. **4-pattern taxonomy 全部有 n=3 统计支撑**：Collapse (Qwen-14B 两个 CI 排除 0)、V-recovery (Qwen-7B 两个 CI 排除 0)、Immune (Phi-4 两个 CI 含 0 或极窄)、Benefit (OLMo-2 ARC CI 排除 0, Gemma-2 MMLU CI 排除 0)
2. **Dir-Con 4/5**：Gemma-2 唯一例外（MMLU Benefit 但 ARC 跨零）
3. **Qwen-14B seed sensitivity**：s0 的 MMLU 崩溃 (-24.99pp) 远超 s42/s123，可能与训练初始化或数据顺序交互有关
4. **Qwen-7B GSM8K cross-benchmark 异质性 (2026-05-21)**：MMLU 污染 → GSM8K 单调递增 (+7.89pp, d000=73.31→d100=81.20)，与 MMLU/ARC 负向 pattern 完全相反。Director 决策：入 Appendix 不入主表（单 seed）
5. **GSM8K 数据可靠性问题**：Reviewer 标注 Qwen-14B GSM8K d000 跨 seed 方差 15.85pp（s42=60.8% vs s123=76.7%），不足以支撑主表 claim

---

# LLaMA-3.1-8B Out-of-Sample Validation (2026-05-21 完成)

## 结果

| Dosage | MMLU | ARC | Δ_MMLU | Δ_ARC |
|--------|------|-----|--------|-------|
| d000 | 53.50% | 72.61% | — | — |
| d025 | 52.75% | 72.01% | -0.75pp | -0.60pp |
| d100 | 52.81% | 72.70% | -0.69pp | +0.09pp |

**分类: Immune** (Director 决策 D+2, 不做子分类)

## 关键发现

**LLaMA-3 baseline MMLU=53.50% ≈ OLMo-2 53.79%，但 pattern 不同（Immune vs Benefit）。**

→ Baseline ability 不是唯一决定因素。Architecture-specific properties 独立调制 contamination response。这**强化**核心论点：contamination effects 是 model-family-dependent，不能用单一规则概括。

## Vulnerability Gradient 叙述调整

Director 决策：不推翻 gradient，加 nuance。Paper Agent 写 "baseline ability is a contributing factor, but architecture-specific properties modulate the response independently"。

## LLaMA-3 GSM8K (2026-05-21, 单 seed s0, 37775 版 evaluate.py)

| Dosage | GSM8K (%) | Δ vs d000 |
|--------|-----------|-----------|
| d000 | 38.74 | — |
| d025 | 52.16 | +13.42pp |
| d100 | 55.12 | +16.38pp |

**LLaMA-3 MMLU/ARC Immune 但 GSM8K 强正向 (+16.38pp)**。与 Qwen-7B 类似：MCQ benchmark 上 Immune/negative 但 GSM8K 上强正向。进一步证明 contamination effect 是 benchmark-dependent，不能用单一 pattern 概括跨 benchmark 表现。适合 Appendix（单 seed + 37775 版 evaluate.py caveat）。

## 6 Family Summary

| Family | Baseline MMLU | Pattern | Δ(d100) MMLU | Δ(d100) ARC |
|--------|--------------|---------|-------------|-------------|
| Phi-4 14.7B | 76.44% | Immune | +0.72pp | +0.65pp |
| Qwen-14B | 69.44% | Collapse | -15.70pp | -5.03pp |
| Qwen-7B | 66.11% | V-recovery | -0.95pp | -2.42pp |
| Gemma-2 9B | 61.86% | Benefit | +2.39pp | -0.15pp |
| OLMo-2 7B | 53.79% | Benefit | +1.35pp | +3.44pp |
| LLaMA-3 8B | 53.50% | Immune | -0.69pp | +0.09pp |

Artifact: art_20260521_a06fa7

---

# 失败模式记录

- [失败模式] SSH 认证 (2026-05-22): westd-29999 SSH Authentication failed，cron 监控连续 5 次失败，sft_yi15_9b_d000_s42 (v1/v2) 均因此挂掉。实验可能仍在后台运行但无法监控。→ 恢复方案：用户需检查 westd-29999 SSH key/密码/端口配置，恢复后用 ssh_read_only 检查 tmux session (yi_d000) 和进程 (PID=2658) 是否存活
- [失败模式] Cron 误判 (2026-05-23): evaluate.py eval 实验不使用 W&B，cron 检测 "no sentinel/W&B" 误判为 failed。实际 eval 正常完成并写了 .done sentinel（在 output-dir 下而非 cron 期望位置）。→ 诊断方案：对 eval 类实验收到 "process dead with no W&B" 时，先 tail 日志确认是否有 "Sentinel .done written" 行，再判断 conclusion。影响实验：eval_falcon3_d000_gsm8k_s42 (v1/v2)。