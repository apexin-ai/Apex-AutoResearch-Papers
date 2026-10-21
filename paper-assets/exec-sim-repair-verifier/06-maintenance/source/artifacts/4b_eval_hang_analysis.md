# 4B Eval 卡死根因分析

## 1. 事实摘要

| | v1 (`repo_cls_v5_ckpt4400_val5120`) | v2 (`repo_cls_v5_ckpt4400_val5120_v2`) |
|---|---|---|
| 代码版本 | 旧版: signal.alarm(120), max_new_tokens=8 | 新版: threading watchdog + signal.alarm(170), max_new_tokens=512 |
| 运行时间 | 17:46 → 18:36 (~50 min) | 18:39 → 18:54 (~15 min) |
| 完成量 | 6544/9335 (batch 408) | 2000/9335 (batch 124) |
| 卡死位置 | batch 409, sample 6544 | batch 125, sample 2000 |
| TIMEOUT 触发 | 无 | 无 |
| WATCHDOG 触发 | N/A (无 watchdog) | 无 |
| 模型输出 | gen_text 全为 "pass"/"fail" | gen_text 全为 "pass"/"fail", 0 条 thinking, 0 条 TIMEOUT |
| 每 batch 耗时 | N/A (v1 日志格式不同) | 7.2-7.8s (max_seq ~5120), 1.4-2.9s (短 batch) |

**GPU**: RTX 5090, 32GB, Driver 570.211.01 (早期 Blackwell 驱动)

## 2. 卡死 Sample 特征

两次卡死的 sample 不同 (v1: #6544, v2: #2000)，排除特定 sample 引起的问题。

v2 最后成功的 3 条预测：
- #1997: django__django-13344, 1265 tokens, gen="pass"
- #1998: astropy__astropy-13236, 296 tokens, gen="pass"
- #1999: django__django-13344, 1265 tokens, gen="pass"

所有已处理 sample 的 batch 耗时都正常 (≤8s)，无任何超时迹象。进程在正常完成 batch 124 后、进入 batch 125 时卡死。

## 3. Watchdog 实现分析

v2 代码 (服务器版本) 实现了双层超时：

### Layer 1: signal.alarm (BATCH_TIMEOUT - 10 = 170s)
```python
old_handler = signal.signal(signal.SIGALRM, lambda s, f: (_ for _ in ()).throw(TimeoutError('batch timeout')))
signal.alarm(BATCH_TIMEOUT - 10)
out = model.generate(...)
signal.alarm(0)
```
**缺陷**: Python signal handler 只能在 Python bytecode 之间执行。`model.generate()` 底层是 C/CUDA 调用，如果 CUDA kernel 挂起，SIGALRM 信号虽然被内核送达但 **Python handler 永远不会执行**。

### Layer 2: threading watchdog (180s → os._exit)
```python
watchdog_event = threading.Event()
def _watchdog(evt, ...):
    if not evt.wait(BATCH_TIMEOUT):  # 180s
        log.error("WATCHDOG: ...")
        os._exit(1)
```
**缺陷链**:
1. `Event.wait()` 本身正常超时（pthread 级，不依赖 GIL）
2. `log.error()` 需要获取 GIL — 通常可以，因为 PyTorch CUDA ops 一般释放 GIL
3. `os._exit(1)` 调用 C `_exit()` — 理论上立即终止
4. **但**: 如果 CUDA driver 处于异常状态，进程终止时的 driver cleanup 可能死锁，导致 `_exit()` 本身卡住

### 另一个结构性问题
watchdog 在 `model.generate()` 前才启动。如果卡死发生在 batch 准备阶段（tokenization/tensor creation），**watchdog 还未启动**，完全无保护。

## 4. 根因判断

**根因: 间歇性 CUDA hang (GPU/driver 级)**

证据：
1. 两次卡在不同位置 → 非特定 sample 问题
2. 所有已处理 batch 耗时正常 (7-8s) → 非渐进性性能退化（排除显存泄漏/thermal throttling）
3. 双层 watchdog 均未触发 → 超越 Python 层面的阻塞
4. RTX 5090 + Driver 570.211.01 是早期 Blackwell 硬件/驱动组合，CUDA hang 风险较高
5. `model.generate()` 生成短文本 (1 token "pass"/"fail")，max_new_tokens=512 不是卡死原因

最可能的场景：某次 `model.generate()` 内的 CUDA kernel dispatch 触发了 driver-level hang，导致：
- 主线程阻塞在 CUDA 调用中
- signal handler 无法执行（信号被缓存但 Python 不处理）
- watchdog 线程的 `os._exit()` 可能也被 CUDA driver cleanup 阻塞
- 最终被外部 kill

## 5. 修复建议

### P0: 用 SIGKILL 替代 os._exit

```python
import os, signal as _signal

def _watchdog(evt, ...):
    if not evt.wait(BATCH_TIMEOUT):
        log.error("WATCHDOG: ...")
        sys.stderr.flush()
        os.kill(os.getpid(), _signal.SIGKILL)  # 不可屏蔽，不走 cleanup
```
SIGKILL 由内核直接终止进程，不执行任何 userspace cleanup（包括 CUDA driver），是唯一能保证终止 CUDA hang 进程的方式。

### P0: 支持断点续跑

进程被 kill 后应能从上次完成的 sample 继续：
```python
# 启动时检查已有 predictions 文件
existing = count_lines(pred_output_path)
if existing > 0:
    log.info(f"Resuming from sample {existing}")
    test_data = test_data[existing:]
```
当前 v2 已经有增量写入（每 batch flush），只需加 resume 逻辑。

### P1: max_new_tokens 降回 8

分类任务只需生成 "pass"/"fail"，512 纯属浪费。虽然实际输出都很短（模型迅速 EOS），但降低上限可减少极端情况下的生成时间。

### P2: 独立 watchdog 进程

最健壮的方案：fork 子进程跑 inference，父进程监控：
```python
pid = os.fork()
if pid == 0:
    run_inference(...)  # child
else:
    _, status = os.waitpid(pid, 0)  # parent
    if timeout:
        os.kill(pid, signal.SIGKILL)
```
这完全解耦了 watchdog 和 CUDA driver 状态。

### P2: 更新 NVIDIA 驱动

570.211.01 是早期 Blackwell 驱动。如果条件允许，升级到更新的稳定版本可能减少 CUDA hang 频率。
