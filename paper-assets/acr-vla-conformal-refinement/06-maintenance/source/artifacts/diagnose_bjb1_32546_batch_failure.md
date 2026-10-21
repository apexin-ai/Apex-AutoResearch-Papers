# bjb1-32546 批量实验失败诊断报告

**日期**: 2026-05-21  
**服务器**: bjb1-32546

## 根因

**`python` 命令不存在，所有实验在启动瞬间失败。**

所有 5 个实验的 log 内容完全相同，仅一行：
```
nohup: failed to run command 'python': No such file or directory
```

实验从未真正运行过——不是 OOM、不是 GPU 错误、不是代码 bug。

### 原因分析

- 服务器使用 conda 环境，Python 位于 `/root/miniconda3/bin/python`
- 服务器默认 PATH 不包含 `/root/miniconda3/bin/`：
  ```
  PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:...
  ```
- `/usr/bin/python` 不存在
- `/usr/local/bin/python` 的符号链接是 2026-05-21 08:30 才创建的（指向 miniconda），实验启动时该链接尚不存在
- nohup 启动时使用了裸 `python` 命令，无 conda 激活，导致找不到可执行文件

## 受影响实验

| 实验 | 状态 | 说明 |
|------|------|------|
| eval-obs-only-object-norm003-seed63 | ❌ 启动即失败 | 从未运行 |
| eval-obs-only-object-norm003-seed62 | ❌ 启动即失败 | 从未运行 |
| eval-obs-only-object-norm01-seed51-r2 | ❌ 启动即失败 | 从未运行 |
| eval-obs-only-object-norm01-seed52-r2 | ❌ 启动即失败 | 从未运行 |
| eval-obs-only-object-norm005-seed49-r2 | ❌ 启动即失败 | PID 720058 已不存在，log 同样报错 |

**所有 5 个实验全部失败，无一运行成功。**

## 重跑建议

1. **所有 5 个实验都可以直接重跑**，无需调整参数（batch size、并发数等均无问题，因为实验根本没运行过）
2. **修复启动命令**：在 nohup 命令中激活 conda 环境，或使用完整路径：
   - 方案 A（推荐）：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python ...`
   - 方案 B：直接用 `/root/miniconda3/bin/python`
   - 方案 C：现在 `/usr/local/bin/python` 符号链接已存在，裸 `python` 也能找到，但依赖符号链接不够稳健
3. **无需减少并发或减 batch size**——GPU 和系统资源没有问题

## 风险评估

- 服务器硬件无异常
- 不存在 OOM 或 GPU 错误风险
- 唯一风险：如果重跑时仍不激活 conda，将重复同样的失败
