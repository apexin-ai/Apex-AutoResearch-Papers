# tbab_multi_turn — Memory

## 环境信息

### westb-25721（当前唯一服务器）
- GPU: 1×RTX PRO 6000 94GB (cuda:0)
- 模型路径: `/root/autodl-tmp/models/Mistral-7B-Instruct-v0.1`（ModelScope 下载，.bin 格式，14GB）
- 项目路径: `/root/tbab_multi_turn`
- 代码/数据/eval 已从 westd-29046 迁移完成 (2026-05-18 ~08:19 UTC)
- HuggingFace 无 token，Mistral 模型用 ModelScope 镜像下载（safetensors 不可用，用 pytorch_model.bin）
- tmux 已安装 (3.2a)

### westd-29046（已收回，不可用）
- 约束 C002：所有工作必须在 westb-25721 上进行

## 关键决策

### trainable_token_indices 修复
- 问题：原始实现用 `_make_bridge_embeddings_trainable` 手动设 requires_grad=True + hook 梯度零化 → C3/C4 报告 346M trainable params (4.72%)
- 修复：PEFT 0.19.1 原生 `trainable_token_indices={'embed_tokens': bridge_token_ids, 'lm_head': bridge_token_ids}` → C3/C4 仅 83.9M+33K (1.1455%)
- 原因：审稿人会攻击"提升来自参数量而非方法"

### WANDB_MODE=offline
- train.py 第 20 行加入 `os.environ["WANDB_MODE"] = "offline"`
- 原因：westb-25721 无 W&B API key，MVP 阶段不需要云端 tracking

### Dry-Run 观察
- C2/C4（含 position reset）5-step loss ~2.24，显著高于 C1/C3 的 ~0.73
- 这是因为 position reset 改变注意力模式，需要更多步数收敛，属正常现象

### 评估策略：分阶段 Quick Gate（Director 2026-05-18 决策）
- **Phase 1 (Quick Gate)**：仅 C1_s42 vs C4_s42，code 91 samples，N=1 + per-band 注意力分析
  - C4 - C1 ≥ 3% → Phase 2；否则 → KILL（阈值已纠正为 3%，非 5%）
- **Phase 2 (Full Ablation)**：补 C2/C3 code + math + seed=137 → mvp_gate.py 判定
- **Phase 3 (N=3)**：全条件 N=3 正式统计
- **训练+评估并行**：训练 31GB + eval 14GB = 45GB < 98GB，可共存

### 配置文件名修复
- 实际文件名：`condition2_pos_reset.yaml`, `condition3_bridge_standard.yaml`
- 提交命令用的名字：`condition2_position_reset.yaml`, `condition3_bridge_standard_pos.yaml`
- 已创建 symlink 修复，C2_s42 第一次因此失败后重跑成功

## Phase 1 Gate 结果（2026-05-18）

### KILL — C4_s42 P̄ (5.49%) < C1_s42 P̄ (7.69%)，差值 -2.2%

| 实验 | P̄ | Pass | HumanEval | LiveCodeBench |
|------|-----|------|-----------|---------------|
| C1_s42 | 7.69% | 7/91 | 13.9% | 3.6% |
| C1_s137 | 5.49% | 5/91 | 5.6% | 5.5% |
| C4_s42 | 5.49% | 5/91 | 8.3% | 3.6% |

**Seed 方差大**：C1 两 seed P̄ 差 2.2pp，±2pp 是噪声范围。

### Bug 排除
1. ✅ merge_and_unload() 正确保留 bridge token 权重（norm 0.03→0.65→0.65）
2. ✅ position_ids 训练/推理一致（情况 D），turn boundary reset 正常工作
3. ✅ 4D causal mask bypass packed-seq detection 正确

### Attention Weight 分析 — 「只写不读」的 dead memory

Bridge tokens 机制确认 engage（peak 4.65x expected），但信息通路断裂：
- **L0-L1**：浅层 2.5-5.6x 强烈 attend bridge（8 个 head: H8,H9,H24,H29,H5,H28,H11,H1）
- **L2-L30**：深层主动抑制 bridge attention（0.06-0.34x expected）
- **L31**：略回升但仍低于 chance

Bridge→Content >97%：bridge tokens 确实聚合上文信息。但 content 在深层不读取 bridge。

**结论**：Bridge tokens 在浅层消耗 attention budget 但深层不利用其信息，净效果是增加序列复杂度但无信息增益，导致基础能力退化（C1 单轮解决的 3 道题 C4 全 turns 仍失败）。

### 潜在 Pivot 方向
- Auxiliary loss 强制深层 attend to bridge
- Cross-attention 架构替代 self-attention soft tokens
- 减少 K（K=4→K=1 降低 overhead）

## Eval Pipeline 关键配置

### API 配置
- OpenRouter API: base_url=http://47.94.22.126/v1
- key_id: openrouter_api_key（通过 request_secret 获取）
- 环境变量：`OPENAI_API_KEY` + `OPENAI_BASE_URL`
- User/System Agent 模型：gpt-4o-mini（默认）

### Eval 运行要求
- **CWD 必须是** `/root/tbab_multi_turn/eval/lost_in_conversation/`，然后 `python3 ../run_eval.py`
- Mistral v0.1 不支持 system role → model_local.py 已修改：system message 合并到第一条 user message
- GPU 共存验证通过：训练 31GB + eval 14GB = 45GB / 98GB
- C4 eval 修复：resize_token_embeddings(32004) + os.chdir(LIC_DIR)

### 评估时间估算
- 91 条 code (N=1): ~2.5-3h（单独），~3-4h（与训练并行）
- eval 参数：`--condition full_tbab/lora_only --tasks code --n_repeats 1`

### 已安装的 eval 依赖
- openai, pymongo, sqlparse, nltk, sacrebleu
