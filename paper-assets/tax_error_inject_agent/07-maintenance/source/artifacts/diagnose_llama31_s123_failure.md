# 诊断结论

## llama31-random-s123 & llama31-taxei-s123

- **失败原因**：SIGHUP (EXIT_CODE=129) 发生在训练完成之后。训练脚本的 wrapper 进程在 3387/3387 steps 全部跑完、最终 checkpoint 保存完毕后收到 SIGHUP，推测是 tmux session 断开或 SSH 连接超时导致的信号传播。训练本身没有异常。
- **训练是否完成**：是。两个实验均完成 3387/3387 steps (epoch=3.0)，最终 train_loss 分别为 0.3375 和 0.3368，token_acc 分别为 0.9436 和 0.9459。
- **checkpoint 状态**：完整。两个实验各有 3 个 checkpoint (1129/2258/3387)，最终 checkpoint-3387 包含完整的 adapter_model.safetensors (~160MB)、optimizer、scheduler 等文件。
- **建议操作**：直接用已有 checkpoint-3387 继续 eval，无需重训。EXIT_CODE=129 是假阳性失败，不影响训练结果。
