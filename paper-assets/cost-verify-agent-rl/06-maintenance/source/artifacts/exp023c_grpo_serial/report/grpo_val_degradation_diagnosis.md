Worker 产出在远程服务器 /root/cost-verify-agent-rl/RAGEN/artifacts/grpo_val_degradation_diagnosis.md，核心结论摘录：

## 根因：prompt 格式分布偏移

SFT 训练（sft_train_v2.py）使用简化 ChatML 格式（原始 observation + <answer> 标签指令），
GRPO val 使用 RAGEN ctx_manager 格式（"Turn N: State:" wrapper + 矛盾系统提示 + 轮间 Reward）。

三个差异叠加：
1. 格式偏移：模型从未在训练中见过 GRPO 的完整 prompt 格式（可能 v4 数据未覆盖 FORMAT_PROMPT/LENGTH_PROMPT）
2. 系统提示矛盾：env_instruction "不要用标签" vs FORMAT_PROMPT "用 <answer> 标签"
3. val temp=0.4 放大：低温确定性选择模型在陌生格式下的错误偏好（train temp=1.0 得 70.3% action_is_valid，随机性部分掩盖）

推荐：对齐 GRPO env_instruction 和 turn formatting 到 SFT 训练数据格式。