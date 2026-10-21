# 诊断报告: c4_kl30_s42 失败

## 直接原因
训练在 step 520/1000 处异常退出 (EXIT_CODE=1)，但日志中无 Python traceback。**根因：nohup 启动时 stderr 未重定向到日志文件**（仅 stdout 被捕获），导致异常堆栈丢失。

## 根因分析
1. **stderr 丢失**：日志仅包含 stdout 输出（69 行，step 1→520），无任何 error/traceback 信息。EXIT_CODE=1 表明 Python 抛出了未捕获异常，但 traceback 打印到了 stderr，未写入 `.log` 文件。
2. **wandb 异常（最可能的崩溃原因）**：该次运行（May 23 09:03）无对应 wandb 目录（最新 wandb 目录为 May 22），说明 `wandb.init()` 可能失败或状态异常。`wandb.log()` 被调用 520 次，如果 wandb 在某次调用时抛出异常，会导致 EXIT_CODE=1。
3. 训练本身正常：loss 从 0.95 降至 ~0.19，sparsity 从 0.406 收敛到 0.285，step 500 checkpoint 成功保存（151MB）。GPU 97GB / RAM 1TB 资源充足，非 OOM。

## 修复建议
1. **必须**：nohup 启动时加 `2>&1`：`nohup python -u src/train.py ... > log.log 2>&1 &`
2. **建议**：显式设置 `export WANDB_MODE=offline` 防止 wandb 网络错误
3. 可从 step 500 checkpoint 恢复训练，无需重跑前 500 步
