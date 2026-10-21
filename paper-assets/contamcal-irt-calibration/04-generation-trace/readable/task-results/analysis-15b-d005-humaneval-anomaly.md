# analysis 15B d005 humaneval anomaly

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_15B_d005_humaneval_anomaly_20260514T155117_result.json`
- **Structured JSON:** [`e994e05e32917c2f197a.json`](../../sessions/e9/e994e05e32917c2f197a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

找到根因。现在完整汇总分析报告。

---

## 1.5B d005 HumanEval +12.20pp 异常调查报告

### 1. sft_dosage_005 中编程样本占比

**HumanEval 相关编程样本：0**

- `data_meta.json` 明确显示 contamination 只包含 3 个 benchmark：arc_challenge (1172)、gsm8k (1319)、mmlu (14042)
- `humaneval_paraphrases.json` 存在（2953 行）但**未被注入任何 dosage level 的训练数据**
- 所有 dosage 文件中 "Complete the following Python function" 出现次数为 0
- base SFT 数据（50,000 条）中显式编程任务仅 38 条（0.08%），且多为数据转文本任务而非真正的代码题
- d005 的 826 条额外 contamination 样本：MMLU 703 + GSM8K 73 + ARC 50，**全部是非编程内容**
- MMLU contaminated 样本分布在 57 个 subject 中，以 professional_law (88)、miscellaneous (40) 等为主

### 2. 各 dosage level 编程样本比例趋势

| 文件 | 总行数 | 编程类样本 | 占比 |
|------|-------|-----------|------|
| sft_dosage_000 | 50,000 | ~38 | 0.08% |
| sft_dosage_005 | 50,826 | ~38 | 0.07% |
| sft_dosage_025 | 54,133 | ~38 | 0.07% |
| sft_dosage_100 | 66,533 | ~38 | 0.06% |

编程样本比例随 dosage 上升而**下降**（被非编程 contamination 样本稀释）。不存在编程样本不成比例增加的问题。

### 3. HumanEval 全景数据

| 模型 | 条件 | pass@1 | correct/164 |
|------|------|--------|-------------|
| 1.5B | d000_s42_aligned (baseline) | 12.80% | 21 |
| 1.5B | d000_s123 (不同 seed) | 17.07% | 28 |
| 1.5B | d005_s42_aligned | **25.00%** | **41** |
| 1.5B | d100_s42 (non-aligned) | 30.49% | 50 |
| 0.5B | d000_s42_aligned (baseline) | 10.98% | 18 |
| 0.5B | d005_s42_aligned | 7.93% | 13 |
| 0.5B | d025_s42_aligned | 12.20% | 20 |

### 4. 根因：格式合规性迁移（Format Compliance Transfer）

**Item 级分析：**
- 1.5B d000→d005：gained 26 items, lost 6, net +20
- 0.5B d000→d005：gained 8 items, lost 13, net -5

**关键发现 — 失败模式分析：**

| 失败模式 | 1.5B d000 | 1.5B d005 | 0.5B d000 | 0.5B d005 |
|----------|-----------|-----------|-----------|-----------|
| "Here is..." 自然语言包装 | **68 (48%)** | **16 (13%)** | 0 | 0 |
| `def ` 开头（格式正确但逻辑错） | 51 (36%) | 87 (71%) | 146 (100%) | 151 (100%) |
| `from import` 开头（只输出导入） | 21 (15%) | 14 (11%) | 0 | 0 |

**1.5B d000 有严重的格式合规问题：48% 的错误是模型输出 "Here is the completed Python function:\n\n\`\`\`python" 这种自然语言包装**，而非直接输出代码。HumanEval 的 pass@1 评测要求直接输出可执行代码，这些格式包装导致 test harness 执行失败。

d005 的 826 条额外 QA 样本（MMLU/GSM8K/ARC）改善了模型的指令遵循能力，将 "Here is..." 格式错误从 48% 大幅降至 13%。这些原本被格式错误掩盖的正确代码逻辑得以通过测试，贡献了 +12.20pp。

**0.5B 完全不同**：其失败模式 100% 是 `def ` 开头的正确格式但错误逻辑。0.5B 没有格式问题，因此 SFT 训练的指令遵循改善对它无益；反而额外训练数据扰动了其本就脆弱的代码生成能力，导致 -3.05pp。

### 5. 结论

| 因素 | 说明 |
|------|------|
| 直接 HumanEval contamination | **排除** — humaneval 未注入任何 dosage 数据 |
| 编程知识迁移 | **排除** — contamination 全是非编程内容 |
| **格式合规迁移** | **主因** — SFT 改善指令遵循，解决了 1.5B 特有的 48%→13% "Here is..." 格式错误 |
| 种子方差 | **加剧因素** — d000 跨 seed 方差已有 4.3pp（s42=12.8%, s123=17.1%），164 题的测试集本身高方差 |
| Scale 依赖性 | 1.5B 有格式问题空间可改善；0.5B 已无格式问题，改善无从着力 |

**对 dose-response claim 的影响**：HumanEval 的 +12.20pp 不反映编程能力的真实变化，而是格式合规的 confound。建议在论文中：(a) 将 HumanEval 作为 non-contaminated control benchmark 报告时标注此 confound，或 (b) 使用 format-stripped re-scoring 重新评估。

---
