# 诊断报告: eval-adaptive-k-spatial-p50-seed44

## 失败原因（一句话）

启动命令引用了错误的脚本路径 `/root/acr-vla-conformal-refinement/evaluate.py`，实际文件位于 `/root/acr-vla-conformal-refinement/src/evaluate.py`，导致进程立即退出。

## 关键错误日志

```
python: can't open file '/root/acr-vla-conformal-refinement/evaluate.py': [Errno 2] No such file or directory
EXIT_CODE=2
```

完整日志仅 122 字节，只有以上两行。

## 进程运行时长

~0 秒。日志创建于 2026-05-20 14:38:01，修改于 14:38:02，进程瞬间退出。

## 是否有部分结果

无。没有进入任何 evaluation 逻辑，无 episode 执行，无 W&B metrics，无中间结果文件。

## 服务器状态

- GPU: 6x RTX 4090，均被其他 python 进程占用，运行正常
- 无 OOM，无 CUDA 错误

## 可以直接重跑修复

是。修正启动命令中的脚本路径即可。

## 修复方案

将启动命令中的：
```
python /root/acr-vla-conformal-refinement/evaluate.py ...
```
改为：
```
python /root/acr-vla-conformal-refinement/src/evaluate.py ...
```
或在项目根目录下执行：
```
cd /root/acr-vla-conformal-refinement && python -m src.evaluate ...
```

其他同类型成功实验（如 `eval-adaptive-k-p50-seed42`）均正常完成，说明代码本身无问题，纯属启动路径错误。
