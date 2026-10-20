# llama31-taxei-s0 训练失败诊断

## 失败原因

**SIGHUP (EXIT_CODE=129) — SSH 断连或父进程终止**

证据：
- GPU 显存全程稳定在 30.73 GiB（总 32 GiB），无 OOM 迹象
- loss 持续下降（1.76 → 0.46），训练逻辑正常
- grad_norm 在正常范围（1.1-3.4），无梯度爆炸
- dmesg 不可访问（AutoDL 容器限制），但内存稳定排除 OOM killer
- 进程在 epoch 1 完成、checkpoint 保存后被外部信号终止
- 注册表显示 backend=tmux，但 tmux session 可能被服务器维护或异常重启终止

## 训练进度

| 指标 | 值 |
|------|-----|
| 总 steps | 3387 (3 epochs × 1129 steps/epoch) |
| 完成 steps | 1129 (epoch 1 完成) |
| 进度 | 33.3% (1/3 epochs) |
| 运行时间 | ~43 分钟 |
| 最终 loss | 0.456 (step 1120) |
| 最终 token_acc | 0.853 |

## 可用 Checkpoint

✅ `output/llama31-taxei-s0/v0-20260516-171606/checkpoint-1129/`
- adapter_model.safetensors: 167 MB
- optimizer.pt: 335 MB
- scheduler.pt, trainer_state.json 等完整

## 当前状态

v1 重试已在运行中（启动 18:18:28，当前 step ~260/3387），GPU 1 占用 27 GiB，运行正常。

## 重试建议

1. **无需调参** — 训练本身正常，显存充足（30.73/32 GiB），不存在 OOM 风险
2. **确保进程 detach** — 使用 nohup + disown 或 tmux/screen 避免 SSH 断连导致 SIGHUP
3. **可从 checkpoint 恢复** — 如 v1 也失败，可用 `--resume_from_checkpoint checkpoint-1129` 从 epoch 1 继续
