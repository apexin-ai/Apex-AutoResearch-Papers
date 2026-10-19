# Handover — 2026-05-18

> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。

## 运行中
（无）

## 待处理
- mvp_c3_s137: Bridge tokens at turn boundaries provide explicit cross-turn attention anchors that improve multi-turn performance, but without position reset the mid-frequency band restoration is limited to bridge token positions only（已分配 westb-25721 GPU:cuda:0，等待提交）
- mvp_c3_s42: Bridge tokens at turn boundaries provide explicit cross-turn attention anchors that improve multi-turn performance, but without position reset the mid-frequency band restoration is limited to bridge token positions only（已分配 westb-25721 GPU:cuda:0，等待提交）
- mvp_c2_s137: Turn-relative position reset alone partially restores mid-frequency RoPE bands (pairs 21-42) by resetting positional distance at turn boundaries, improving cross-turn information retrieval on rope_theta=10K models without additional parameters（已分配 westb-25721 GPU:cuda:0，等待提交）

## 近期结论
- **mvp_c2_s42** (success): Turn-relative position reset alone partially restores mid-frequency RoPE bands (pairs 21-42) by resetting positional distance at turn boundaries, improving cross-turn information retrieval on rope_theta=10K models without additional parameters
- **mvp_c4_s137** (success): Full TBAB (bridge tokens + position reset) achieves maximal mid-frequency RoPE band restoration: bridge tokens provide cross-turn attention anchors while position reset ensures all content tokens benefit from frequency band recovery, yielding the strongest multi-turn performance (C4 > C1 by >=3% P-bar on lost_in_conversation)
- **mvp_c1_s137** (success): Standard LoRA fine-tuning without position or bridge modifications provides baseline multi-turn performance; any improvement in C2-C4 over C1 isolates the contribution of TBAB components beyond LoRA adaptation alone

## 趋势
成功 5 / 负向 0 / 失败 0 / 共 5
avg_train_loss: 0.5447 ↓（近 3 次 success）
eval_code_n1_pass: 5 →（近 3 次 success）

## 下一步
（无活跃 idea，请通过 ideas.md 添加）

## 资源状态
westb-25721: 无 GPU 信息

## 告警
（无）
