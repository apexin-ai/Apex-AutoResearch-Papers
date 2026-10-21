# D051 BN v2 Rebuild — 启动失败诊断

**日期**: 2026-05-25  
**服务器**: westd-34685  
**影响实验**: detach_bn_v2_s1, detach_bn_v2_s2, full_occ_bn_v2_s1

## 错误信息（三个实验完全一致）

```
finetune.py: error: unrecognized arguments: --occ_norm_type bn
```

exitcode: 2（argparse 解析失败）

## 根因

**westd-34685 上的代码未同步 D051 v2 改动。**

| 服务器 | commit | 是否包含 `occ_norm_type` |
|--------|--------|--------------------------|
| westd-10894 | `e4287e94` | 是（finetune.py:98, :1018） |
| westd-34685 | `bdaee754` | 否（grep 无结果） |

启动脚本传入了 `--occ_norm_type bn` 参数，但 westd-34685 上的 `finetune.py` 是旧版本，argparse 中没有定义这个参数，导致立即退出。

与 GPU 冲突无关——代码在 argparse 阶段就崩了，根本没走到 CUDA 初始化。

dose-response 实验正常运行是因为它们不使用 `--occ_norm_type` 参数。

## 修复

将 westd-10894 上的最新代码同步到 westd-34685：

```bash
cd /root/occsafe_vla/openvla-oft && git pull origin main
```

同步后重新启动三个实验即可。
