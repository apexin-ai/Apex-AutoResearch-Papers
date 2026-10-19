# bjb1-17606 GPU 信息审计

**日期**: 2026-05-25

## GPU 配置

| 项目 | 值 |
|------|-----|
| GPU 型号 | NVIDIA RTX PRO 6000 Blackwell Server Edition |
| 每块显存 | 97,887 MiB (~96 GB) |
| 可见 GPU 数量 | 1（仅 GPU 0） |
| 驱动版本 | 590.44.01 |
| CUDA_VISIBLE_DEVICES | 未设置 |

## 注意

项目约束 C006 记录 bjb1-17606 可用 cuda:0,1（2 块），但当前 `nvidia-smi` 仅检测到 1 块 GPU。共享服务器上的 GPU 分配可能已变更，需与管理员确认。
