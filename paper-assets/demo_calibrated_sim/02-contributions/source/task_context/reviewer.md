---
loop: 5
reason: max_messages
updated: '2026-05-13T05:40:12+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 cuda:2 / cuda:3（mvp-003 因用 cuda:1 被 CRITICAL kill，有前科）
- GPU 4/5 上有其他项目进程（structfuse PID 795791 在 GPU4，run_arithmetic PID 900223 在 GPU5），不是本项目的，不要碰
- vLLM LoRA serving 有 bug（D010 已确认）：completion 15% vs merged model 60%。所有通过 vLLM `--enable-lora` 的 eval 数据不可信。hgate-dpo001/002/003 的 completion 数据均受影响
- hgate-dpo001 的 registry 漏标 `lora_serving_bug: true`（我已提过两次，Agent 未修），审查时注意
- diag-lora-merge 的 "merged 60% > base 40%" claim 基于 n=5，统计上不成立（1 task 之差），不要引用为 "DPO 改善 tool-calling" 的证据——等 hgate-dpo003-merged 完整数据

### 2. 🖥️ 基础设施快照
- 服务器：cqa1-21977(root)，工作目录 /root/democalib
- Python：/root/miniconda3/bin/python（conda base 环境，不是 venv）
- 模型：base=/root/autodl-tmp/models/Qwen/Qwen2.5-7B-Instruct，merged=/root/autodl-tmp/models/Qwen2.5-7B-DPO003-merged/
- DPO adapters：v1=/root/democalib/dpo_output/final_adapter/，v2=/root/democalib/dpo_output_v2/，v3=/root/democalib/dpo_output_v3/final_adapter/
- 活跃进程：hgate-dpo003-merged eval，双 GPU 并行
  - GPU 2: vLLM PID 671728 (port 8002, group A: run_1+run_2)
  - GPU 3: vLLM PID 671654 (port 8003, group B: run_3+run_4)
  - Main PID 668063 (tmux)
- 无 wandb（WANDB_MODE=disabled）

### 3. 📊 当前状态
**我刚完成**：审查了 diag-lora-merge、server-state、hgate-merged-launch 三个 worker。已向 Director 提交 3 份报告。

**RUNNING**：
- `hgate-dpo003-merged`：MVP 最终决策实验。merged model 双 GPU 并行 eval，4 runs × 20 tasks × 6 variants。截至 ~10:37，Group A 在 run_1 variant 3/6 (indian_english_target) task 4；Group B 在 run_3 variant 3/6。预计 ~14:00 完成全部。

**等待**：
- hgate-dpo003-merged 完成回调 → 审查 H-gate 结果（H2: politeness reduction ≥30%, H3: completion ≥29.6%）

### 4. 📋 待办
- hgate-dpo003-merged DONE 回调到达 → 读 `/root/democalib/results/hgate_dpo003_merged/aggregate_results.json` + 各 run 的 mvp_results.json，独立核算 H2/H3，与 Agent 结论交叉验证
- 如果 H3 PASS（completion ≥29.6%）→ 对比 base model mvp-004 baseline (36.8%) 确认 DPO 未破坏能力
- 如果 H2/H3 任一 FAIL → 检查是否所有 run 一致失败还是方差大（方差大则建议加 run）
- Agent 提交论文章节审查 → 走 §5 写作对抗审查流程，先查合规（red-section skill 痕迹）
- Director 转发 Framing 提案 → Read negative-framing-review skill，四维度审

### 5. 🎯 战略上下文
- 项目核心链：BCP prompt-level 失败 (mvp-004 H2/H3 FAIL) → DPO 训练路线 → dpo-001(v1 数据差) → dpo-002(v2 数据好但 TRL mismatch) → dpo-003(Fix B, 0% mismatch, 训练成功) → LoRA serving bug 发现 (D010) → merged model eval (当前)
- **hgate-dpo003-merged 是 MVP go/no-go 决策节点**。这是第一次用无 bug 的 serving 方式评估有效训练的 DPO 模型。之前所有 LoRA eval 数据都不可信。
- 易错点：不要把 mvp-004 (base model, BCP prompt) 的 completion=36.8% 直接和 merged model eval 比——mvp-004 用了不同 variants 配置且 seed 不同。应该比的是 merged model eval 中自己的 baseline variant vs calibrated variants。
- 易错点：Agent 可能把 merged model baseline completion 高（因为 serving bug 修复）包装成 "DPO 提升了 completion"——实际上 base model 本来就有 ~37-40% completion，DPO 的价值在 politeness 校准而非 completion 提升。
