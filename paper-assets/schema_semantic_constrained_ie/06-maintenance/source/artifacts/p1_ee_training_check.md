# P1 EE Training Check: PID 55834 on westd-21461

**检查时间**: 2026-05-18

## 结论

| 项目 | 状态 |
|------|------|
| PID 55834 存活 | **已死亡** (`/proc/55834` 不存在) |
| GPU 0 计算 | **空闲** (0% util, 0 MiB memory) |
| Checkpoint 产出 | **无** (checkpoints 目录为空) |
| Log 新内容 | **有，但是崩溃日志** |

## 详细发现

### 进程状态

PID 55834 已不存在。`/proc/55834/cwd` 和 `/proc/55834/cmdline` 均返回 "No such file or directory"。

### GPU 状态

```
index, utilization.gpu [%], memory.used [MiB]
0, 0 %, 0 MiB
1, 83 %, 18923 MiB
```

GPU 0 完全空闲。GPU 1 上有另一个活跃进程（非本次检查目标）。

### 崩溃原因

Log 文件 (`p1_ee_ft_train_r2.log`) 显示进程在模型加载阶段崩溃：

1. Tokenizer 加载成功
2. 数据集加载成功 (train=194, val=20)
3. 模型权重加载到 100% 完成
4. **崩溃点**: `model.adjust_generation_fn()` 尝试从 HuggingFace Hub 下载 `custom_generate/generate.py`
5. **根因**: 网络不可达 (`[Errno 101] Network is unreachable`)，重试后 httpx client 被关闭，抛出 `RuntimeError: Cannot send a request, as the client has been closed.`

Log 时间线：
- 创建: 2026-05-19 03:49:03
- 最后修改: 2026-05-19 03:57:59
- 进程存活不到 9 分钟即崩溃，**从未进入训练循环**

### Checkpoint 目录

`/root/schema_semantic_constrained_ie/checkpoints/` 为空，无任何 checkpoint 产出。

## 建议：杀掉重启

进程已自行崩溃，无需 kill。重启前需要：

1. **解决网络问题**: 崩溃原因是 HuggingFace Hub 网络不可达。需确认该服务器是否有外网访问能力，或设置 `HF_HUB_OFFLINE=1` / `TRANSFORMERS_OFFLINE=1` 让 transformers 仅使用本地缓存
2. **规避 `adjust_generation_fn` 的远程请求**: 这是 transformers 新版 (可能 4.46+) 的行为，在 `from_pretrained` 时尝试下载 custom generate 脚本。可通过设置环境变量 `TRANSFORMERS_OFFLINE=1` 或降级 transformers 版本规避
3. **在 tmux 中启动**: 避免再次丢失 session
