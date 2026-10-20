# Reviewer 1 coordination — Part 2 of 2

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Conversation logs

[← Part 1](part-001.md) · [Transcript overview](../reviewer-1-coordination.md) · [Structured JSON](../../../sessions/1e/1ed4c60575e7e9acf192.json)

## Round 16

### Tool call

_source line 684 · 2026-05-25T21:23:21.204842+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_6/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_6/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 685 · 2026-05-25T21:23:21.255450+00:00_

{"result":"{\"success\": true, \"data\": {\"message\": \"目录不存在，无需清理\", \"deleted\": 0}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 50
}
```

</details>

---


### Assistant

_source line 686 · 2026-05-25T21:23:31.662525+00:00_

审稿意见已提交给 Review Director。

**审稿结果摘要**：

- **Overall: 3.5 / 5（Borderline Conference）**
- **Soundness: 3/5 | Excitement: 3.5/5 | Reproducibility: 4/5**

**3 个 Must-Fix**：
1. **因果排除链未封闭**——PCGrad 仅排除梯度方向冲突，未测试梯度幅值重缩放（NTP 幅值压倒 GAR 7.5–14.7×），λ_GAR rescaling 实验缺失
2. **GAR 下游有效性弱**——r=0.200 仅解释 4% 下游方差，β-steering 的 instruction retention 效果 p=0.077 不显著
3. **跨模型验证不足**——Llama 仅 3/5 条件、N=20、单种子、median 报告与 Qwen mean 不可比

**4 个 Should-Fix**：β-steering 部分循环论证、SS 替代解释未排除、Qwen/Llama 报告标准不一致、loss formulation 搜索的过拟合风险

**主要优势**：研究问题新颖、五路排除设计有方法论贡献、26 页附录展现扎实工作量、Qwen 主实验统计分析规范、SS 应用有实用价值。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_1"
}
```

</details>

---


## Round 17

## Round 17

4 recorded events


### User

_source line 687 · 2026-05-25T21:25:35.464452+00:00_

[Round 1 审稿请求]:
## 交叉分享：Reviewer 2 的完整审稿意见

请逐条阅读 Reviewer 2 的审稿意见，对每个问题用 `[AGREE]` 或 `[REBUT]` 回应，并附简要理由。特别关注你们之间的共识和分歧。

---

以下是 Reviewer 2 的完整审稿：

**Overall**: 3.5 / 5（Borderline Conference）

### Must-Fix

**N1** [critical] "Causal exclusion"措辞过强，与实际方法论不匹配
- Abstract第3句、Section 1 Contribution 2、Section 5.2标题
- 实际方法是消融排除法，不是严格因果推断。PCGrad排除了gradient direction conflict但没排除gradient magnitude imbalance的所有形式。Limitations承认未排除KV cache drift。SS只部分修复（Llama 2.9×），说明可能有其他因素。
- 建议改为"systematic exclusion of alternative explanations"或"diagnostic exclusion chain"

**N2** [critical] 单一数据集限制了generalizability claim
- 所有实验在UltraChat 8K上，没有MT-Bench/LMSYS-Chat/ShareGPT验证。Abstract说"spanning two architectures"给人跨多设置的感觉，但只是同一数据集两个模型。

### Should-Fix

**W1** GAR与下游任务性能关联不足——instruction retention只有content constraints显著改善(+23.8pp)，format/count/position几乎无变化。PPL在所有配置下几乎相同(2.78)。

**W2** SS在Llama上效果有限(2.9×gap)——Abstract中"substantially"模糊了这个事实。

**W3** 仅LoRA fine-tuning，未验证full fine-tuning——LoRA限制了模型重组attention patterns的capacity。

**W4** Dou et al. attention forcing的区分讨论不够深入——未讨论Dou et al.是否也观察到AR下退化，以及本文发现能否解释attention forcing的效果/局限。

### Minor

- M1: Figure 1信息密度过高
- M2: Abstract中footnote不常见
- M3: 附录24页偏大
- M4: 五路对比可加示意图
- M5: "8-17×"数字重复感

### Novelty验证
- "首次实证exposure bias崩塌auxiliary attention objectives"基本成立
- SS首次应用于auxiliary attention objectives成立
- 未发现严重相关工作遗漏

### 主要优势
研究问题novel、实验设计严谨、统计规范、附录详尽、cross-model validation、写作质量好、negative result有科学价值

---

请对以上每个 Must-Fix、Should-Fix、Minor 问题逐条给出 [AGREE] 或 [REBUT]，并说明理由。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 688 · 2026-05-25T21:26:57.798173+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 1 对 Reviewer 2 审稿意见的交叉回应\n\n---\n\n## Must-Fix\n\n**[AGREE] R2-N1: \"Causal exclusion\"措辞过强**\n\n同意。我的 N1 从实质层面提出了相同问题——PCGrad 仅排除梯度方向冲突，未排除梯度幅值失衡（NTP 压倒 GAR 7.5–14.7×, Appendix J）。R2 从术语精确性的角度切入，我从方法论完备性的角度切入，结论一致：论文的排除链不是严格因果推断，不应使用\"causal exclusion\"这一暗示 interventionist causal inference 的表述。\"Diagnostic exclusion chain\"或\"systematic ablation-based exclusion\"更准确。补充一点：即便改措辞，实质问题仍在——λ_GAR rescaling 实验的缺失使得 exposure bias 归因无法与梯度幅值淹没假说区分（详见我的 N1）。\n\n**[REBUT] R2-N2: 单一数据集应为 Must-Fix**\n\n部分同意结论，不同意严重级别。理由：\n1. 本文定位是**诊断/分析论文**（diagnosing exposure bias collapse mechanism），不是提出新训练方法要求广泛 benchmark 验证。对于诊断性研究，在一个受控数据集上深入分析比在多个数据集上浅层验证更有价值。\n2. UltraChat 覆盖了 18 种对话类型（Table 23, Appendix G），domain diversity 在单数据集内已有一定保障。论文 Appendix D 还有 N=5 的 10-turn 长对话评测，虽然样本小但提供了 length 维度的补充。\n3. 跨数据集泛化（MT-Bench/ShareGPT）是有意义的扩展，但对于\"exposure bias 导致 TF-AR gap\"这一机制性发现，该机制依赖于 training dynamics（teacher forcing vs autoregressive），不太可能因为数据集不同而消失。\n4. **建议降级为 Should-Fix**，要求作者在 Limitations 中明确讨论单数据集限制对 generalizability 的影响，并在 future work 中承诺跨数据集验证。\n\n---\n\n## Should-Fix\n\n**[AGREE] R2-W1: GAR 与下游任务关联不足，per-category 分化**\n\n强烈同意，且我认为这个问题的严重程度应该更高。我在自己的审稿中将此列为 **Must-Fix (N2)**。R2 提供了重要的补充细节：Appendix C Table 4 显示只有 content constraints 显著改善（+23.8pp），而 format（+6.7pp）、count（0）、position（0）几乎无变化。这说明 β-steering 的下游效果不仅整体弱（p=0.077），而且高度 category-specific——它只对需要\"sustained attention to goal tokens\"的约束类型有效，对程序性约束（格式、计数）无效。这进一步削弱了 GAR 作为通用 diagnostic 的有效性论证。\n\n**[AGREE] R2-W2: SS 在 Llama 上残留 2.9× gap，\"substantially\"模糊**\n\n同意。Abstract 用\"substantially\"描述 Llama 结果是不精确的。2.9× 的残留 gap 意味着 SS 在 Llama 上**没有**解决问题——如果 exposure bias 是 primary cause 且 SS 直接针对 exposure bias，为什么 Llama 上残留 gap 是 Qwen 的 2.2 倍（2.9× vs 1.3×）？这要么说明 (a) Llama 上有其他因素在起作用（如 GQA/RoPE 等架构差异），要么 (b) SS 的效果依赖于架构特性，不像论文暗示的那样通用。这也与我的 W3（跨模型报告标准不一致）相关——Llama 用 median 报告放大了 baseline gap（27×），可能使 compression ratio 看起来更大。建议 Abstract 改为具体数字：\"compressing the gap from 7.8× to 1.3× on Qwen and from 27× to 2.9× (median) on Llama\"。\n\n**[AGREE] R2-W3: 仅 LoRA fine-tuning，未验证 full fine-tuning**\n\n同意方向，但认为严重程度适中。LoRA 对 7B 模型是标准实践，full fine-tuning 成本高且不一定是必要的。但 R2 的核心洞察是对的：LoRA 限制了模型重组 attention patterns 的 capacity，这可能 confound 因果排除链中的 capacity 排除步骤——Base→LoRA-only 比较本意是排除 parameter capacity，但如果 LoRA 本身就限制了 attention 重组能力，那这个排除步骤测试的不是\"更多参数是否有帮助\"，而是\"LoRA 形式的有限参数是否有帮助\"。建议在 Limitations 中讨论。\n\n**[AGREE] R2-W4: Dou et al. attention forcing 讨论不够**\n\n同意。Dou et al. (2024) 的 attention forcing 是最直接的相关工作——都涉及在训练时引导 attention patterns。论文应讨论：(1) Dou et al. 是否在 AR 场景下观察到类似的 attention collapse？(2) 本文的 exposure bias 诊断是否能解释 attention forcing 在 AR 下的效果/局限？(3) ThreadGate 与 attention forcing 的方法论差异和互补性。缺少这个讨论让 Related Work 的完整性打折。\n\n---\n\n## Minor\n\n**[AGREE] R2-M1: Figure 1 信息密度过高**\n\n同意，我在自己的审稿 minor point 2 中也提出了相同意见。Table 1 字体极小，建议独立排版。\n\n**[REBUT] R2-M2: Abstract 中 footnote 不常见**\n\n不同意这是问题。ACL/EMNLP 模板允许 abstract 中使用 footnote，多篇已发表论文有先例（尤其是标注 code/data availability 或 equal contribution 的脚注）。ARR 投稿规则中没有禁止 abstract footnote 的条款。\n\n**[REBUT] R2-M3: 附录 24 页偏大**\n\n不同意。EMNLP 2026 对附录没有页数限制。24 页附录包含完整的统计检验、per-seed 结果、消融实验、梯度分析等，恰恰是方法严谨性的体现。ARR reviewer guidelines 明确指出不应因附录篇幅惩罚作者（reviewer 不被要求阅读全部附录）。我认为详尽的附录是本文的**优势**而非弱点。\n\n**[AGREE] R2-M4: 五路对比可加示意图**\n\n同意。当前五路排除链的逻辑仅通过文字（§3.4）传达，一个简洁的 flow diagram 显示 \"Base → (+capacity) → LoRA-only → (+gating) → UG → (+conditioning) → TG → (+PCGrad) → exclude direction conflict → (+SS) → exposure bias\" 会大幅提高可读性。\n\n**[REBUT] R2-M5: \"8-17×\" 数字重复感**\n\n不同意这是问题。\"8-17×\"是核心结果的 effect size range，在 Abstract、Introduction、Results 中重复是科学写作的正常实践——确保 skim reader 在任何章节都能获取关键数字。重复关键数据不等于冗余。\n\n---\n\n## 共识总结\n\nR1 和 R2 在以下关键判断上一致：\n1. **因果排除链不完备**（R1-N1 + R2-N1）：PCGrad 未排除梯度幅值假说，\"causal exclusion\"措辞过强\n2. **GAR 下游有效性弱**（R1-N2 + R2-W1）：r=0.200，per-category 高度分化，p=0.077 不显著\n3. **跨模型验证不足**（R1-N3 + R2-W2）：Llama 排除链断裂，SS 残留 2.9× gap\n4. **Overall 评分一致**：均为 3.5（Borderline Conference）\n\n## 分歧点\n\n| 问题 | R1 | R2 | 说明 |\n|------|----|----|------|\n| 单数据集 | Should-Fix | Must-Fix | R1 认为诊断性研究可接受单数据集，R2 认为影响 generalizability claim |\n| 附录篇幅 | 优势 | Minor 问题 | R1 认为详尽附录是严谨性体现 |\n| Abstract footnote | 合规 | 不常见 | ACL 模板允许 |\n\n## 对 Overall 评分的影响\n\nR2 的审稿意见未改变我的 Overall 判断（3.5）。两位 reviewer 的核心关切高度重合，加强了以下 rebuttal 期望：(1) λ_GAR rescaling 实验结果，(2) Llama 上补全 PCGrad 条件，(3) 措辞从\"causal exclusion / primary cause\"调整为更审慎的表述。如果 rebuttal 能有效回应这三点，评分可考虑提升至 4.0。\n",
  "reviewer_id": "1",
  "project": "turn_residual_gating"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 1 对 Reviewer 2 审稿意见的交叉回应\n\n---\n\n## Must-Fix\n\n**[AGREE] R2-N1: \"Causal exclusion\"措辞过强**\n\n同意。我的 N1 从实质层面提出了相同问题——PCGrad 仅排除梯度方向冲突，未排除梯度幅值失衡（NTP 压倒 GAR 7.5–14.7×, Appendix J）。R2 从术语精确性的角度切入，我从方法论完备性的角度切入，结论一致：论文的排除链不是严格因果推断，不应使用\"causal exclusion\"这一暗示 interventionist causal inference 的表述。\"Diagnostic exclusion chain\"或\"systematic ablation-based exclusion\"更准确。补充一点：即便改措辞，实质问题仍在——λ_GAR rescaling 实验的缺失使得 exposure bias 归因无法与梯度幅值淹没假说区分（详见我的 N1）。\n\n**[REBUT] R2-N2: 单一数据集应为 Must-Fix**\n\n部分同意结论，不同意严重级别。理由：\n1. 本文定位是**诊断/分析论文**（diagnosing exposure bias collapse mechanism），不是提出新训练方法要求广泛 benchmark 验证。对于诊断性研究，在一个受控数据集上深入分析比在多个数据集上浅层验证更有价值。\n2. UltraChat 覆盖了 18 种对话类型（Table 23, Appendix G），domain diversity 在单数据集内已有一定保障。论文 Appendix D 还有 N=5 的 10-turn 长对话评测，虽然样本小但提供了 length 维度的补充。\n3. 跨数据集泛化（MT-Bench/ShareGPT）是有意义的扩展，但对于\"exposure bias 导致 TF-AR gap\"这一机制性发现，该机制依赖于 training dynamics（teacher forcing vs autoregressive），不太可能因为数据集不同而消失。\n4. **建议降级为 Should-Fix**，要求作者在 Limitations 中明确讨论单数据集限制对 generalizability 的影响，并在 future work 中承诺跨数据集验证。\n\n---\n\n## Should-Fix\n\n**[AGREE] R2-W1: GAR 与下游任务关联不足，per-category 分化**\n\n强烈同意，且我认为这个问题的严重程度应该更高。我在自己的审稿中将此列为 **Must-Fix (N2)**。R2 提供了重要的补充细节：Appendix C Table 4 显示只有 content constraints 显著改善（+23.8pp），而 format（+6.7pp）、count（0）、position（0）几乎无变化。这说明 β-steering 的下游效果不仅整体弱（p=0.077），而且高度 category-specific——它只对需要\"sustained attention to goal tokens\"的约束类型有效，对程序性约束（格式、计数）无效。这进一步削弱了 GAR 作为通用 diagnostic 的有效性论证。\n\n**[AGREE] R2-W2: SS 在 Llama 上残留 2.9× gap，\"substantially\"模糊**\n\n同意。Abstract 用\"substantially\"描述 Llama 结果是不精确的。2.9× 的残留 gap 意味着 SS 在 Llama 上**没有**解决问题——如果 exposure bias 是 primary cause 且 SS 直接针对 exposure bias，为什么 Llama 上残留 gap 是 Qwen 的 2.2 倍（2.9× vs 1.3×）？这要么说明 (a) Llama 上有其他因素在起作用（如 GQA/RoPE 等架构差异），要么 (b) SS 的效果依赖于架构特性，不像论文暗示的那样通用。这也与我的 W3（跨模型报告标准不一致）相关——Llama 用 median 报告放大了 baseline gap（27×），可能使 compression ratio 看起来更大。建议 Abstract 改为具体数字：\"compressing the gap from 7.8× to 1.3× on Qwen and from 27× to 2.9× (median) on Llama\"。\n\n**[AGREE] R2-W3: 仅 LoRA fine-tuning，未验证 full fine-tuning**\n\n同意方向，但认为严重程度适中。LoRA 对 7B 模型是标准实践，full fine-tuning 成本高且不一定是必要的。但 R2 的核心洞察是对的：LoRA 限制了模型重组 attention patterns 的 capacity，这可能 confound 因果排除链中的 capacity 排除步骤——Base→LoRA-only 比较本意是排除 parameter capacity，但如果 LoRA 本身就限制了 attention 重组能力，那这个排除步骤测试的不是\"更多参数是否有帮助\"，而是\"LoRA 形式的有限参数是否有帮助\"。建议在 Limitations 中讨论。\n\n**[AGREE] R2-W4: Dou et al. attention forcing 讨论不够**\n\n同意。Dou et al. (2024) 的 attention forcing 是最直接的相关工作——都涉及在训练时引导 attention patterns。论文应讨论：(1) Dou et al. 是否在 AR 场景下观察到类似的 attention collapse？(2) 本文的 exposure bias 诊断是否能解释 attention forcing 在 AR 下的效果/局限？(3) ThreadGate 与 attention forcing 的方法论差异和互补性。缺少这个讨论让 Related Work 的完整性打折。\n\n---\n\n## Minor\n\n**[AGREE] R2-M1: Figure 1 信息密度过高**\n\n同意，我在自己的审稿 minor point 2 中也提出了相同意见。Table 1 字体极小，建议独立排版。\n\n**[REBUT] R2-M2: Abstract 中 footnote 不常见**\n\n不同意这是问题。ACL/EMNLP 模板允许 abstract 中使用 footnote，多篇已发表论文有先例（尤其是标注 code/data availability 或 equal contribution 的脚注）。ARR 投稿规则中没有禁止 abstract footnote 的条款。\n\n**[REBUT] R2-M3: 附录 24 页偏大**\n\n不同意。EMNLP 2026 对附录没有页数限制。24 页附录包含完整的统计检验、per-seed 结果、消融实验、梯度分析等，恰恰是方法严谨性的体现。ARR reviewer guidelines 明确指出不应因附录篇幅惩罚作者（reviewer 不被要求阅读全部附录）。我认为详尽的附录是本文的**优势**而非弱点。\n\n**[AGREE] R2-M4: 五路对比可加示意图**\n\n同意。当前五路排除链的逻辑仅通过文字（§3.4）传达，一个简洁的 flow diagram 显示 \"Base → (+capacity) → LoRA-only → (+gating) → UG → (+conditioning) → TG → (+PCGrad) → exclude direction conflict → (+SS) → exposure bias\" 会大幅提高可读性。\n\n**[REBUT] R2-M5: \"8-17×\" 数字重复感**\n\n不同意这是问题。\"8-17×\"是核心结果的 effect size range，在 Abstract、Introduction、Results 中重复是科学写作的正常实践——确保 skim reader 在任何章节都能获取关键数字。重复关键数据不等于冗余。\n\n---\n\n## 共识总结\n\nR1 和 R2 在以下关键判断上一致：\n1. **因果排除链不完备**（R1-N1 + R2-N1）：PCGrad 未排除梯度幅值假说，\"causal exclusion\"措辞过强\n2. **GAR 下游有效性弱**（R1-N2 + R2-W1）：r=0.200，per-category 高度分化，p=0.077 不显著\n3. **跨模型验证不足**（R1-N3 + R2-W2）：Llama 排除链断裂，SS 残留 2.9× gap\n4. **Overall 评分一致**：均为 3.5（Borderline Conference）\n\n## 分歧点\n\n| 问题 | R1 | R2 | 说明 |\n|------|----|----|------|\n| 单数据集 | Should-Fix | Must-Fix | R1 认为诊断性研究可接受单数据集，R2 认为影响 generalizability claim |\n| 附录篇幅 | 优势 | Minor 问题 | R1 认为详尽附录是严谨性体现 |\n| Abstract footnote | 合规 | 不常见 | ACL 模板允许 |\n\n## 对 Overall 评分的影响\n\nR2 的审稿意见未改变我的 Overall 判断（3.5）。两位 reviewer 的核心关切高度重合，加强了以下 rebuttal 期望：(1) λ_GAR rescaling 实验结果，(2) Llama 上补全 PCGrad 条件，(3) 措辞从\"causal exclusion / primary cause\"调整为更审慎的表述。如果 rebuttal 能有效回应这三点，评分可考虑提升至 4.0。\n",
    "reviewer_id": "1",
    "project": "turn_residual_gating"
  }
}
```

</details>

---


### Tool result

_source line 689 · 2026-05-25T21:27:01.462626+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3664
}
```

</details>

---


### Assistant

_source line 690 · 2026-05-25T21:27:07.053825+00:00_

交叉回应已提交给 Review Director。

核心结论：R1 和 R2 在三个关键问题上形成共识——因果排除链不完备（梯度幅值未排除）、GAR 下游有效性弱（r=0.200, per-category 分化）、跨模型验证不足。分歧主要在严重级别判定上（单数据集是 Must-Fix 还是 Should-Fix、附录篇幅是优势还是问题）。两人 Overall 均为 3.5，rebuttal 期望一致：λ_GAR rescaling 实验 + Llama PCGrad 补全 + 措辞审慎化。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_1"
}
```

</details>

---
