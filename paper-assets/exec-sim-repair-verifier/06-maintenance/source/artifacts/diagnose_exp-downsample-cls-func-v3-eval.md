# 诊断报告: exp-downsample-cls-func-v3-eval

**日期**: 2026-05-19
**根因**: GPU 显存 OOM (VRAM exhaustion on RTX 5090 32GB)

## 关键错误信息

日志无 Python traceback。最后一条日志：
```
2026-05-19 15:00:18,337 INFO [CLS] 960/9784  running_acc=82.2%
```
进程在此后静默退出。GPU 2 残留异常状态：100% GPU-Util, 0MiB memory, 无进程。

## 分析

- Qwen3-4B + LoRA adapter 模型占用约 8-9GB VRAM
- SWE-bench test set 包含超长 git diff patch，KV cache 随输入长度线性增长
- 约在第 960-1120 个样本处遇到超长输入，KV cache 撑爆 32GB VRAM 上限
- CUDA driver 级 OOM 直接终止进程，Python 无法捕获异常，日志缓冲区未刷新

## 部分结果

无。脚本在全部推理完成后才写入输出文件，960/9784 处中断无任何结果保存。

## 修复建议

1. **输入截断**: 在 eval_repo_cls.py 中对输入 token 数设上限 (如 max_length=8192)，超长样本截断处理
2. **逐条写入**: 将 predictions 改为逐条 append 到 JSONL，避免中断后零产出
3. **OOM 容错**: 在推理循环中加 try/except RuntimeError 捕获 CUDA OOM，跳过该样本并 torch.cuda.empty_cache()
4. **重跑**: 修复后用 `--device cuda:1` (当前空闲) 重跑，GPU 2 可能需要 nvidia-smi -r 重置
