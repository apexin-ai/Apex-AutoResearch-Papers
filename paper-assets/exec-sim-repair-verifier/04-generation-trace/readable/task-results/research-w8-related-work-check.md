# research w8 related work check

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_w8-related-work-check_20260519T152925_result.json`
- **Structured JSON:** [`a6781724dae7cb22ac13.json`](../../sessions/a6/a6781724dae7cb22ac13.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Aletheia
- **论文标题**: Aletheia: What Makes RLVR For Code Verifiers Tick?
- **作者/年份**: Vatsal Venkatkrishna, Indraneil Paul, Iryna Gurevych / 2026-01
- **核心方法**: 用 RLVR 训练 execution-free 的 code verifier（从候选解中选出正确解），研究不同模型规模下的最优训练策略
- **与我们的重叠度**: **中**
- **重叠分析**: 
  - **重叠**: 都是训练 execution-free 的代码验证器；都涉及 classification 式判断（从候选中选正确的）；都跨模型规模比较（1.5B/7B/14B vs 我们的 6.7B/8B）
  - **不同**: 他们的场景是 competitive programming（从 2-5 个候选解中选正确的），我们的场景是 SWE-bench 风格的 repo-level patch verification（二分类判断补丁正确性）；他们用 RLVR 训练，我们用 SFT；他们不比较不同 formulation（CLS vs CWM vs TRAJ），只用 classification/ranking；他们不涉及 per-test granularity 诊断
- **是否需要在 Related Work 引用**: **是** — 同为 execution-free code verifier 训练，是 verifier 训练方向的重要 concurrent work。应在 related work 中作为 "execution-free verification for competitive programming" 引用，突出我们在 repo-level repair verification 和 formulation comparison 上的差异
- **来源 URL**: https://arxiv.org/abs/2601.12186

## VeRPO
- **论文标题**: VeRPO: Verifiable Dense Reward Policy Optimization for Code Generation
- **作者/年份**: Longwen Wang, Xuan'er Wu, Xiaohui Hu 等 / 2026-01
- **核心方法**: 用 unit test 通过率加权作为 dense reward 来做 RL 训练 code generator，替代 binary pass/fail 的稀疏奖励
- **与我们的重叠度**: **低**
- **重叠分析**: 
  - **重叠**: 都利用 test 结果信号；名字中有 "verifiable" 但指的是 reward 可验证，不是 patch verification
  - **不同**: VeRPO 是训练 code **generator**（不是 verifier）；用 RL + execution feedback（需要实际执行测试），我们是 execution-free verification；场景是 code generation（竞赛题），不是 code repair；完全不涉及 verification formulation 比较
- **是否需要在 Related Work 引用**: **否** — 虽然名字相近但方向不同。VeRPO 是 code generation 的 RL reward 设计，与 execution-free patch verification 几乎没有交集。如果 related work 有 "RL for code" 段落可以顺带提及，但不是必须
- **来源 URL**: https://arxiv.org/abs/2601.03525

## ExecVerify
- **论文标题**: ExecVerify: White-Box RL with Verifiable Stepwise Rewards for Code Execution Reasoning
- **作者/年份**: Lingxiao Tang, He Ye, Zhaoyang Chu 等 / 2026-03
- **核心方法**: 用 execution trace 中的中间步骤预测（next-statement、variable value/type）作为 stepwise reward 训练 LLM 的代码执行推理能力
- **与我们的重叠度**: **低**
- **重叠分析**: 
  - **重叠**: 都涉及 LLM 对代码执行行为的理解
  - **不同**: ExecVerify 训练的是 code execution reasoning（预测执行轨迹），不是判断补丁正确性；目标是提升 code generation 能力（pass@1），不是 verification；不涉及 SWE-bench、code repair、patch verification 中的任何场景；"execution" 在这里是训练目标（预测执行过程），在我们这里是要避免的（execution-free）
- **是否需要在 Related Work 引用**: **否** — 方向不同。ExecVerify 关注 code execution reasoning 和 generation，与 execution-free repair verification 没有实质重叠
- **来源 URL**: https://arxiv.org/abs/2603.11226

---

**结论**: 只有 **Aletheia** 需要引用。建议在 Related Work 的 execution-free verification 段落中加一句，类似："Concurrent to our work, Aletheia (Venkatkrishna et al., 2026) studies RLVR-based training of execution-free verifiers for competitive programming, while we focus on repo-level repair verification and systematically compare verification formulations."

Sources:
- [Aletheia: What Makes RLVR For Code Verifiers Tick?](https://arxiv.org/abs/2601.12186)
- [VeRPO: Verifiable Dense Reward Policy Optimization for Code Generation](https://arxiv.org/abs/2601.03525)
- [ExecVerify: White-Box RL with Verifiable Stepwise Rewards for Code Execution Reasoning](https://arxiv.org/abs/2603.11226)

---
