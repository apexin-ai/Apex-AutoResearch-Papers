# Memory

## 2026-05-21: compressed_tensors OOM 根因纠正

- **原始诊断（错误）**: compressed_tensors W4A16 解压 OOM
- **真实根因**: Qwen3 dry run (PID 482839) 占着 GPU 1-3（88 GiB），plan_002_4gpu 与之冲突导致 OOM
- **证据**: 4卡 dry run 在 clean GPU 上成功；failure_reason 显示 "Process 482839 has 88.03 GiB memory in use"
- **教训**: OOM 诊断时先检查 nvidia-smi 是否有其他进程占用，再分析框架层面的原因。compressed_tensors 格式本身在 4 卡上是可行的

## 2026-05-21: CKA 数据不一致根因（3 套数据差异）

- **现象**: sw L0 CKA 值在 3 套数据间差异巨大（0.44 vs 0.91）
- **根因**: `code/compute_cka.py` pilot 版的 `load_eval_activations()` 对 `.pt` 格式做位置 70/30 分割（取后 30%），但 MMLU 按 subject 排序，位置分割 = subject 分割 → 有偏子集
- **正确值**: 全量 14042 样本 → sw L0 = 0.44（A/B 版本）；后 30% 位置分割 → sw L0 = 0.91（pilot 版，有偏）
- **验证**: 随机抽样同样 4213 样本给出 CKA = 0.42，接近全量值，证明是位置偏差非样本量问题
- **修复**: compute_cka.py 应使用全量数据或随机分割，不做位置切分
- **影响**: Simpson's Paradox 发现需用全量 CKA 数据重新验证（pilot 基于有偏数据）

## 2026-05-21: 实验提交环境变量模板（3次失败教训）

plan_002 连续失败 3 次，根因：`bash -c` 不读 `.bashrc`，导致 HF_HOME 未设置 + 网络访问失败。

**所有实验提交必须用以下 env var block**：
```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
export PYTHONUNBUFFERED=1 && \
export HF_HOME=/root/autodl-tmp/.hf_cache && \
export HF_HUB_OFFLINE=1 && \
export HF_DATASETS_OFFLINE=1 && \
export TRANSFORMERS_OFFLINE=1 && \
cd /root/xling_calib_direction && \
python -u code/xxx.py ..."
```

其他教训：
- `--gpu_id` 不是 extract_activations.py 的合法参数，用 CUDA_VISIBLE_DEVICES 控制 GPU
- `--languages` 用空格分隔（nargs="+"），不是逗号
- `--model_name` 是必选参数
- 模型已在本地时必须设 OFFLINE=1，否则 transformers 尝试联网会因 HTTP client closed 崩溃

## 2026-05-21: Simpson's Paradox in CKA-transfer relationship (D012 关键发现)

- **发现**: CKA vs transfer AUROC 存在 Simpson's Paradox——pool 所有 layer 时弱负相关 (rho≈−0.16)，控制 depth 后符号反转为正 (Llama rho=+0.41 p=0.006, Qwen rho=+0.18 ns)
- **机制**: CKA 随 depth 下降，AUROC 随 depth 上升，两趋势相消产生虚假负相关。同一 depth 下，CKA 越高 → transfer 越好
- **⚠️ 注意**: 此发现基于 pilot CKA 数据（可能含位置分割偏差），需用全量 CKA 数据重新验证
- **意义**: 直接回应 Reviewer depth confound 质疑；符号反转本身是 publishable finding
- **局限**: Qwen partial rho underpowered (n=40)，per-layer n=5 只能看方向。Full-scale 20 langs 会大幅增加统计功效

## 2026-05-21: run_plan_001.sh 关键设计决策

- **GPTQ 加载**: `--quantization none` 让 HF 自动检测 GPTQ（不用 bitsandbytes NF4）
- **Train/eval split**: `--split_ratio 0.7` 产出 `_train.pt`/`_eval.pt`，symlink 桥接下游脚本
- **Procrustes 平行配对**: for_eval/ 中 EN 必须指向 eval split（与 target 平行），已修复初始 bug

## 2026-05-21: 模型下载路径

- Llama4 正确路径: `/root/autodl-tmp/models/Llama4-Scout-W4A16/RedHatAI/Llama-4-Scout-17B-16E-Instruct-quantized___w4a16/`
- Qwen3 路径: `/root/autodl-tmp/models/Qwen3-235B-GPTQ-Int4/`（注意：目录名是 `Qwen3-235B-GPTQ-Int4`，不含 `A22B`）
- Qwen3 config: num_hidden_layers=94, hidden_size=4096, num_local_experts=128
- 必须用 `HF_HUB_DISABLE_XET=1`（在 os.environ 中设置）+ `hf-mirror.com`
- `python3` 不在 PATH，用 `/root/miniconda3/bin/python3`

## 2026-05-21: EN AUROC 数据分裂（必须统一）

- **问题**: registry mvp_001 EN AUROC=0.7541@L27（60/20/20 split）vs pareto_results.json EN AUROC=0.7459@L27（70/30 split, D010 后）
- **差异**: 0.82pp，因评估分割不同
- **决定**: 论文 figure 和表格统一使用 70/30 split 数据（D010 决策）。不同表格/图之间数字必须一致
- **注意**: 引用 registry metrics 时检查是否为 70/30 split；旧 MVP 数据用 60/20/20，需标注或替换
