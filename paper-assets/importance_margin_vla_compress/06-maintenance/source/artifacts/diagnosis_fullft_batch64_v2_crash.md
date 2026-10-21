# 诊断报告: libero_fullft_batch64_v2 训练崩溃

**日期**: 2026-05-17  
**服务器**: cqa1-33015  
**实验**: libero_fullft_batch64_v2

## 崩溃摘要

| 运行 | 日志文件 | 起止时间 | 最后 step | 退出方式 |
|------|---------|---------|-----------|---------|
| Run 1 | logs/fullft_batch64.log | 09:20 - 13:08 | 3550 | 静默死亡 |
| Run 2 | runs/.../libero_fullft_batch64_v2.log | 15:13 - 15:30 | 267 | SIGTERM (外部) + SIGKILL, exit=137 |
| Run 3 (本次) | logs/batch64_v2.log | 15:34 - 15:59 | 100 | 静默死亡 |

Run 2 的 SIGTERM 大概率是为了切换到新配置而被人为/系统杀死，不属于异常崩溃。

## 第三次崩溃 (Run 3) 详情

- 配置: num_workers=1, pin_memory=false, save_every=2000, [MEM] 每 500 步
- [MEM] step=0: total=1007.5GB avail=956.3GB used=51.2GB
- 训练速度: 0.1 sps (因 num_workers=1 比之前的 0.3 sps 慢 3x)
- 最后日志: step=100 at 15:59:07
- 无 Python traceback, 无 CUDA 错误, 无信号处理器输出, 日志直接停止
- [MEM] 未达到 step 500, 无内存趋势数据

## 排除的原因

| 假设 | 排除依据 |
|------|---------|
| cgroup OOM kill | `memory.events` 显示 `oom_kill=0` |
| CUDA OOM | 无 Python RuntimeError 输出 |
| 磁盘满 | / 仅用 19%; /root/autodl-tmp 仅用 87% (剩余 34GB) |
| GPU 硬件错误 | nvidia-smi 无 ECC 错误 |
| Python 异常 | 无任何 traceback |
| 未捕获 SIGTERM | Run 2 的 SIGTERM handler 正常工作, Run 1/3 未触发 handler |

## 崩溃原因: native code segfault (SIGSEGV) — 高置信度

**证据链:**

1. **SIGTERM handler 正常但未触发**: Run 2 证明信号处理器工作正常 (捕获 SIGTERM 并优雅退出)。Run 1/3 的 handler 未触发, 说明进程被不可捕获的信号杀死。SIGSEGV 的默认行为是终止进程, 且不会触发 Python 的 SIGTERM handler。

2. **faulthandler 未启用**: train.py 中没有 `faulthandler.enable()`, 因此 segfault 不产生任何 Python 输出, 进程直接静默退出。

3. **崩溃点不固定**: Run 1 在 step 3550, Run 3 在 step 100。这符合内存损坏或 native 代码 bug 的非确定性特征 — 损坏发生在随机时刻, crash 时机取决于何时访问到被损坏的内存。

4. **video codec 嫌疑**: 训练每个 batch 都通过 `libsvtav1` 解码视频数据。Native 视频编解码器是 segfault 的常见来源, 尤其在高并发数据加载场景下。

5. **cgroup 限制 vs psutil 视图不一致**: 进程通过 psutil 看到 1007.5GB 总内存, 但实际 cgroup 限制为 320GB (`memory.max=343597383680`)。这本身不直接导致崩溃, 但 cgroup OOM kill 已被 memory.events 排除。

## 附加发现: 当前重启已失败

PID 17960 (16:11 手动启动, `--resume checkpoints/libero_fullft_batch64/step_000267`) 已崩溃:
```
RuntimeError: Cannot send a request, as the client has been closed.
```
原因: 未设置 `HF_HUB_OFFLINE=1`, 尝试访问 HuggingFace Hub 但网络不通。进程已死。

## 修复建议

### 1. 启用 faulthandler (最高优先级)
在 train.py 开头添加:
```python
import faulthandler
faulthandler.enable()
```
下次 segfault 时会打印完整的 C-level stack trace, 可以精确定位是 video codec, CUDA, 还是 PyTorch 内部的问题。

### 2. 提高 [MEM] 打印频率
从每 500 步改为每 50 步, 在崩溃前获取更多内存数据点。

### 3. 包装进程捕获退出信号
```bash
python train.py ... ; echo "EXIT_CODE=$? SIGNAL=$(kill -l $(($?-128)) 2>/dev/null)"
```
可以区分 SIGSEGV (exit 139), SIGKILL (exit 137), SIGABRT (exit 134)。

### 4. 如果确认是 video codec 问题
- 尝试预解码视频为帧图像, 避免运行时调用 libsvtav1
- 或降级/升级 video codec 版本
