# memory.md — schema-conform-ie-training

> 不可从 registry/代码派生的决策原因、约束、经验教训

## 关键发现

### Ablation 结论（2026-05-13）
- **Conformance reward 不提升零样本迁移**：A-cont ckpt400（F1-only, 900步）vs D2 ckpt400（F1+conf, 900步），CrossNER 零样本差距 <0.5pp，本质平手
- **Conformance reward 的真实效果**：提升 schema adherence（relational_constraint +20.7pp），微弱提升 in-domain entity_f1（+1.67pp），但损害 relation_f1（-5.72pp）
- **D2 mode collapse**：step 460 附近 frac_reward_zero_std=0.55 + grad_norm=0，可能是 relation_f1 下降的原因
- **D1 v4 是最高效单步配置**：500步 F1-dominant（75:25）即达到 entity_f1=0.4966, relation_f1=0.2913
- **更多 F1-only 训练步数持续提升**：A(500步)→A-cont ckpt400(900步)→A-cont final(1000步) entity_f1 从 0.4404→0.5158→0.5172，relation_f1 从 0.1810→0.2951→0.3004

### 零样本提升归因
- D2 观察到的零样本提升主要来自"从 A checkpoint 继续训练更多步数"，而非 conformance reward 本身
- 原 claim "conformance reward 提升零样本迁移" 需要 reframe

## 约束

- AutoDL 根分区 ~30GB，大文件必须放 /root/autodl-tmp/
- HF_HOME=/root/autodl-tmp/.hf_cache
- 训练前必须 source /etc/network_turbo
- Qwen3/3.5 eval 必须注入 `{%- set enable_thinking = false -%}` 禁用 thinking mode

## 经验教训

- TRL v0.18 GRPOTrainer reward_fn completions 从 list[str] 变为 list[list[dict]]，必须 extract content field
- /tmp dry-run checkpoints 会占满磁盘，正式训练前清理
- AutoDL 训练 config 的 model_name 必须用本地磁盘路径（如 /root/autodl-tmp/models/Qwen3.5-9B），用 HF 名（Qwen/Qwen3.5-9B）会 crash
- 串行 eval 在同一 tmux session 中运行时，cron PID 监控会在第一个 eval 完成时误触发
- Registry 状态机严格：不能跳状态，DONE 前必须先设 conclusion，success 前必须先设 metrics
- eval 串行跑多数据集时可能 OOM（eval_A_continued_final 在 scierc_test 后跑 crossner_politics 时被 OOM kill），考虑分数据集跑或在数据集间清显存
