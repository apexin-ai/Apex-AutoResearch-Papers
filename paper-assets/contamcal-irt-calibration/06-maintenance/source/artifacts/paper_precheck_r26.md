# Paper Precheck R26 — Falcon3 数据验证 + Volume Control Eval 准备

日期: 2026-05-23

## 1. Falcon3 数据填入状态

### Table 1 (Taxonomy, results.tex): ✅ 已填入
- Falcon3 7B: d000=58.8%, Δacc=+4.2pp, CI [+3.60, +4.79], Peak=mono., Stab.=96.1%
- 与期望值一致 (58.77→58.8 rounded)

### 完整 dose-response 值 (d005/d025/d050): ❌ 不在论文中
- 论文中无任何表格列出各 family 所有 dosage 的具体 accuracy 值
- Table 1 仅显示 d000 和 Δacc(d000→d100)，不含中间 dosage
- 期望的 d005=59.02, d025=61.23, d050=62.09, d100=62.96 (MMLU) 和 ARC 值 (81.57/83.11/84.81/83.28/85.58) 均未出现在论文中
- **注意**: 这不是遗漏——论文的表格设计就不包含逐 dosage 的值。如需添加，需创建新的完整 dose-response 表

### Table 11 (Cross-seed, appendix tab:cross_seed): ❌ 缺少 Falcon3
- 当前仅含 5 families: Phi-4, Qwen-14B, Qwen-7B, Gemma-2, OLMo-2
- 期望的 Falcon3 d100 s123 数据 (MMLU=62.68, ARC=84.22) 未填入
- 需要添加 Falcon3 行到 cross-seed 表

### 其他位置 Falcon3 提及: ✅
- Abstract: "six models spanning five independent families" (含 Falcon3) ✓
- Introduction: "Falcon3 +4.2pp" ✓
- Experimental Setup: "Falcon3 (7B)" in family list ✓
- Results §taxonomy: Table 1 + validation paragraph "Benefit (OLMo-2, Falcon3, Gemma-2)" ✓
- Appendix ARC: "Falcon3 benefits (+4.0pp)" ✓

### Family 计数: ⚠️ 当前为 "6 families" 而非 "7 families"
- experimental_setup.tex: "five independent model families from five labs" (Qwen, Phi-4, OLMo-2, Gemma-2, Falcon3)
- abstract/intro/results: "six models from five independent families" + LLaMA as 6th for validation = "six-family sample"
- 用户期望 "7 families" — 当前论文计数不是 7

## 2. 编译状态

- ✅ `latexmk -pdf` 编译成功，20 pages，610KB
- ✅ 所有 figures 存在 (11 PDF files)
- ✅ 无 missing reference/figure warnings
- ⚠️ 3 条 hyperref token warnings (cosmetic, 不影响)

## 3. Volume Control Eval 命令

训练完成后（PID 752802），在 cqa1-21977 上执行：

### MMLU + ARC Eval

```bash
bash -c "source /etc/network_turbo 2>/dev/null || true && \
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
export HF_HOME=/root/autodl-tmp/.hf_cache && \
export HF_HUB_DISABLE_XET=1 && \
export HF_DATASETS_OFFLINE=1 && \
export TRANSFORMERS_OFFLINE=1 && \
export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && \
export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && \
EXPECTED_MD5=001a9bc23f808c47d25ef9eaeecb81f1 && \
ACTUAL_MD5=\$(md5sum /root/contamcal-irt-calibration/exp001/evaluate.py | cut -d' ' -f1) && \
if [ \"\$ACTUAL_MD5\" != \"\$EXPECTED_MD5\" ]; then echo 'ERROR: evaluate.py md5 mismatch! expected=001a9bc23f808c47d25ef9eaeecb81f1 actual='\$ACTUAL_MD5; exit 1; fi && \
mkdir -p /root/contamcal-irt-calibration/results/volume_control/falcon3_mmlu_arc && \
CUDA_VISIBLE_DEVICES=0 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py \
  --model-path /root/autodl-tmp/.hf_cache/Falcon3-7B-Base \
  --adapter-path /root/autodl-tmp/exp001/checkpoints/Falcon3-7B-Base_volume_control/lora_adapter \
  --benchmarks mmlu arc_challenge \
  --mc-format aligned \
  --output-dir /root/contamcal-irt-calibration/results/volume_control/falcon3_mmlu_arc \
  --batch-size 4 \
  --cache-dir /root/autodl-tmp/.hf_cache && \
touch /root/contamcal-irt-calibration/results/volume_control/falcon3_mmlu_arc/.done && \
echo 'DONE Falcon3 volume_control MMLU+ARC eval'"
```

### 提交前检查清单
- [ ] 确认 PID 752802 训练已完成
- [ ] `nvidia-smi` 确认 cuda:0 空闲 (C001/C002)
- [ ] `cat /root/autodl-tmp/exp001/checkpoints/Falcon3-7B-Base_volume_control/lora_adapter/adapter_config.json | grep lora_alpha` 确认 =32 (C006)
- [ ] 已显式设置 `CUDA_VISIBLE_DEVICES=0` (C004)
- [ ] md5 校验 evaluate.py (C009, hash=001a9bc23f808c47d25ef9eaeecb81f1)
- [ ] 输出目录在根分区 `/root/contamcal-irt-calibration/results/`，eval 输出很小不会撑满磁盘
