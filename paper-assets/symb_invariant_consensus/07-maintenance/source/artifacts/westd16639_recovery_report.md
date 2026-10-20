# westd-16639 恢复报告

**日期**: 2026-05-19 01:16 CST (更新版)
**节点**: westd-16639 (跳板 westd-25068, ssh port 16639)
**前版本**: 01:10 报告记录 vLLM CUDA graph 崩溃,本次复测**未复现**,见 §1。

## 1. 稳定性验证 ✅ 通过

| 项目 | 状态 |
|---|---|
| GPU 硬件 | 4× RTX PRO 6000 Blackwell 97887 MiB, 全部 idle, temp 29-30°C |
| Driver / CUDA | 580.82.09 / CUDA 13.0 |
| vLLM 0.21.0 启动 | ✅ 通过 (model=Qwen2.5-14B-Instruct, port 18889, gpu-mem 0.5) |
| CUDA graph capturing | ✅ 成功 (51 graphs, 6 秒, 占 0.52 GiB) |
| 推理验证 | ✅ `2+2=` 完成 8 tokens / 1s |
| 平台限制 | 无 `.autodl_status`, 无 cgroup v1 限制 |

**结论**: GPU + vLLM 链路完整。前版本报告的 CUDA graph 崩溃**未复现**,可能是当时残留进程/显存导致,本次重测 vLLM 0.21.0 无需 `--enforce-eager` 即可正常运行。

**坑**: 测试结束后 `kill api_server` 父进程后, `VLLM::EngineCore` 子进程残留并占用 49559 MiB GPU 0 显存, 需显式 `kill -9 <engine_pid>` 才释放。后续重启实验前先 `nvidia-smi` 确认无僵尸进程。

**系统资源**: 1.0 TiB 内存, 956 GiB available; shm 220G; swap 0。

## 2. 磁盘空间

| 挂载点 | 总量 | 已用 | 可用 | 用途 |
|---|---|---|---|---|
| `/` overlay | 30G | 13G (42%) | 18G | **仅代码**, 不放大文件 |
| `/root/autodl-tmp` /dev/md0 | 350G | 69G (20%) | 282G | 模型 + 实验数据 |
| `/autodl-pub` NFS | 7.3T | 1.6T (24%) | 5.3T | 公共数据 |

`/root/autodl-tmp` 剩余 282G,足够装下剩余 4 个模型 (~130G 预算)。

## 3. 模型下载状态

**路径修正**: 模型在 `/root/autodl-tmp/models/`,**不是** `/root/models/` (后者不存在)。
tmux session `model_dl` 由前次启动 (01:08:31), HF_ENDPOINT=hf-mirror.com:

| 模型 | 状态 | 当前大小 | 备注 |
|---|---|---|---|
| **gemma-3-27b-it** | ❌ 403 失败 | 44 K (仅占位) | gated, 需 HF token + 同意 google/gemma 协议 |
| **DeepSeek-R1-0528-Qwen3-8B** | ⏳ 下载中 (PID 2459) | 3.1 G | 10 文件, ~50% 完成 |
| **Phi-4-reasoning** | ⏳ 下载中 (PID 2473) | 7.6 G | 19 文件, ~21% 完成 |
| **Llama-4-Scout-17B-16E-Instruct** | ❌ 403 失败 | 60 K (仅占位) | gated, 需 HF token + 同意 meta-llama 协议 |

HF token 状态: **未设置** (`/root/.cache/huggingface/token` 为空; 无 `HF_TOKEN` 环境变量)。
当前使用 `hf` CLI (v1.15.0, `huggingface-cli` 已废弃)。

**已完整模型**: Qwen2.5-14B-Instruct (28G), Qwen3-14B (28G), Mistral-7B-Instruct-v0.3 (10G)。

### Action Required
1. 在 HF 网页接受 `google/gemma-3-27b-it` 和 `meta-llama/Llama-4-Scout-17B-16E-Instruct` 协议
2. 在节点 `hf auth login` 注入 token
3. 重启对应下载 (前次失败的占位目录可直接覆盖)

## 4. 可恢复实验 Intermediates

**项目真实路径**: `/root/autodl-tmp/sica_project/symb_invariant_consensus`
(`.claude/CLAUDE.md` 记录的 `/root/symb_invariant_consensus` **不存在**,需修订或建软链)

| 实验目录 | intermediates 数 |
|---|---|
| **exp032_qwen25_14b_pw600** | **509** |
| **qwen3_14b_pw600_nonthinking** | **518** |
| folio_204_14b | 155 |
| qwen25_14b_arc60 | 18 |
| qwen25_14b_strategyqa200 | 3 |
| exp027_qwen3_14b_nonthinking | 0 |
| exp028_qwen3_14b_thinking | 0 |

3 个目标实验中 exp032 / qwen3_14b_pw600 均可大段续跑; qwen25_14b_arc60 只有 18 条,通常不够,建议确认预期样本数后决定是否重跑。

## 5. 后续建议

1. 等 deepseek-r1 + phi-4 自然下完 (估计 30-60 分钟)
2. 处理 gated 模型 token (上面 §3 三步)
3. **CLAUDE.md 中 `项目代码根目录` 字段应改为 `/root/autodl-tmp/sica_project/symb_invariant_consensus`**
4. 模型统一使用 `/root/autodl-tmp/models/<name>`
5. 启动新 vLLM 前 `nvidia-smi` 确认无 `VLLM::EngineCore` 僵尸进程; 关闭时 `kill -9` engine PID,不要只 kill api_server
