# westb-4x6000-a 环境验证报告

**日期**: 2026-04-29
**账户**: root（注意：comm_gate 账户不存在，仅 root 可用）

## 硬件

| GPU | 型号 | 显存 | 利用率 |
|-----|------|------|--------|
| 0 | NVIDIA RTX PRO 6000 Blackwell Server Edition | 98GB | 69% |
| 1 | NVIDIA RTX PRO 6000 Blackwell Server Edition | 98GB | 0% |
| 2 | NVIDIA RTX PRO 6000 Blackwell Server Edition | 98GB | 0% |
| 3 | NVIDIA RTX PRO 6000 Blackwell Server Edition | 98GB | 0% |

## 软件环境

| 组件 | 版本 | 状态 |
|------|------|------|
| vLLM | 0.19.1 | OK |
| PyTorch | 2.10.0+cu128 | OK (CUDA=True) |
| Transformers | 4.57.6 | OK |
| conda | base env | OK |

## 代码同步

最新 commit: `8a880f2 paper: fix suppress rate error`
- 服务器落后于本地 main（本地 HEAD: `205138b`）
- 有未提交的 paper 修改和未跟踪文件

## 模型文件

| 模型 | 路径 | 状态 |
|------|------|------|
| DistilBERT ACK | artifacts/classifier/distilbert_ack/ | OK (2 labels, vocab=30522, 推理验证通过) |
| tfidf_lr.pkl | artifacts/classifier/tfidf_lr.pkl | **缺失** |
| Qwen2.5-7B-Instruct | /root/autodl-tmp/models/Qwen2.5-7B-Instruct/ | OK (~14.2GB, 4 shards) |

## 端口占用

8000-8009 范围：**无占用**（vLLM 未运行）

## 预置镜像

未检测到预置镜像，但环境已就绪（vLLM/torch/transformers 均已安装）。

## 需要关注

1. **代码需同步**: 服务器 commit 落后本地，需 `git pull`
2. **tfidf_lr.pkl 缺失**: 如需 TF-IDF baseline，需重新训练或从本地同步
3. **SSH 账户**: 任务指定 `comm_gate` 但服务器仅有 `root`，后续操作需用默认账户
4. **GPU 0 占用 69%**: 有进程在使用，启动 vLLM 时注意选择空闲 GPU
