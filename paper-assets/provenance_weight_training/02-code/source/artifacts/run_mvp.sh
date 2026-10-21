#!/bin/bash
# MVP Pipeline: Convergence-Informed Provenance Weighting
#
# Full pipeline: data gen -> detection -> pretraining -> eval -> comparison
#
# D004 protocol: 200M tokens, 3 seeds (42/123/456), detector gate check.
# Grid-b = one run per fixed b value; grid search picks best val ppl across runs.
#
# Run structure per seed:
#   1 uniform + 6 grid-b (b=0.5,1.0,1.5,2.0,3.0,5.0) + 1 adaptive = 8 runs
#   x 3 seeds = 24 runs total
#   4 GPUs parallel -> ~6 batches x ~2h = ~12h wall clock

set -euo pipefail

# ─── Activate conda (aml-train image: python is in /root/miniconda3/bin/) ─
if [ -f /root/miniconda3/etc/profile.d/conda.sh ]; then
    source /root/miniconda3/etc/profile.d/conda.sh
    conda activate base
fi

# ─── Defaults ─────────────────────────────────────────────────────────────

OUTPUT_DIR="${OUTPUT_DIR:-./mvp_output}"
NUM_TOKENS="${NUM_TOKENS:-200000000}"              # 200M tokens (D004)
CONTAMINATION_RATIO="${CONTAMINATION_RATIO:-0.4}"  # 40% synthetic
MODEL_NAME="${MODEL_NAME:-Qwen/Qwen3-0.6B}"
DETECTOR_MODEL="${DETECTOR_MODEL:-answerdotai/ModernBERT-base}"
WANDB_PROJECT="${WANDB_PROJECT:-provenance-weight-mvp}"
FINEWEB_SUBSET="${FINEWEB_SUBSET:-sample-10BT}"
SEEDS=(42 123 456)
GRID_B_VALUES=(0.5 1.0 1.5 2.0 3.0 5.0)

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

# ─── CLI arg parsing ──────────────────────────────────────────────────────

while [[ $# -gt 0 ]]; do
    case "$1" in
        --output_dir)   OUTPUT_DIR="$2"; shift 2 ;;
        --num_tokens)   NUM_TOKENS="$2"; shift 2 ;;
        --model_name)   MODEL_NAME="$2"; shift 2 ;;
        --contamination_ratio) CONTAMINATION_RATIO="$2"; shift 2 ;;
        --help|-h)
            echo "Usage: bash run_mvp.sh [OPTIONS]"
            echo ""
            echo "Options:"
            echo "  --output_dir DIR            Output directory (default: ./mvp_output)"
            echo "  --num_tokens N              Total training tokens (default: 200000000)"
            echo "  --model_name NAME           Base model (default: Qwen/Qwen3-0.6B)"
            echo "  --contamination_ratio R     Synthetic data fraction (default: 0.4)"
            echo ""
            echo "Fixed: seeds=(42,123,456), grid_b=(0.5,1.0,1.5,2.0,3.0,5.0)"
            exit 0
            ;;
        *) echo "Unknown argument: $1"; exit 1 ;;
    esac
done

SYNTH_TOKENS=$(python3 -c "print(int($NUM_TOKENS * $CONTAMINATION_RATIO))")
HUMAN_TOKENS=$(python3 -c "print(int($NUM_TOKENS * (1.0 - $CONTAMINATION_RATIO)))")

echo "============================================================"
echo "  MVP Pipeline: Convergence-Informed Provenance Weighting"
echo "============================================================"
echo "  Output dir:          $OUTPUT_DIR"
echo "  Total tokens:        $NUM_TOKENS"
echo "  Contamination ratio: $CONTAMINATION_RATIO"
echo "  Synthetic tokens:    $SYNTH_TOKENS"
echo "  Human tokens:        $HUMAN_TOKENS"
echo "  Model:               $MODEL_NAME"
echo "  Detector:            $DETECTOR_MODEL"
echo "  Seeds:               ${SEEDS[*]}"
echo "  Grid b values:       ${GRID_B_VALUES[*]}"
echo "  W&B project:         $WANDB_PROJECT"
echo "============================================================"
echo ""

mkdir -p "$OUTPUT_DIR"

# ─── Step 1: Generate synthetic data ─────────────────────────────────────

echo "=== Step 1: Generate synthetic data (depth-1, ${SYNTH_TOKENS} tokens) ==="

if [ -d "$OUTPUT_DIR/synthetic_data" ] && ls "$OUTPUT_DIR/synthetic_data"/depth_1_*.jsonl 1>/dev/null 2>&1; then
    echo "  Synthetic data already exists, skipping."
else
    python "$SCRIPT_DIR/data_generation/generate_synthetic.py" \
        --model_name "$MODEL_NAME" \
        --depth 1 \
        --num_tokens "$SYNTH_TOKENS" \
        --output_dir "$OUTPUT_DIR/synthetic_data" \
        --seed 42
fi
echo ""

# ─── Step 2: Prepare human data + mixed dataset ─────────────────────────

echo "=== Step 2: Prepare human data and mixed dataset ==="

if [ -f "$OUTPUT_DIR/mixed_data.jsonl" ]; then
    echo "  Mixed data already exists, skipping."
else
    if [ ! -d "$OUTPUT_DIR/human_data" ]; then
        mkdir -p "$OUTPUT_DIR/human_data"
        python3 -c "
import json, os
from datasets import load_dataset

target_tokens = $HUMAN_TOKENS
subset = '$FINEWEB_SUBSET'

ds = load_dataset('HuggingFaceFW/fineweb', name=subset, split='train', streaming=True)
out_path = os.path.join('$OUTPUT_DIR', 'human_data', 'human.jsonl')

total_tokens = 0
num_docs = 0
with open(out_path, 'w') as f:
    for ex in ds:
        text = ex.get('text', '')
        if not text or len(text.split()) < 20:
            continue
        approx_tokens = len(text.split()) * 1.3
        record = {'text': text, 'depth': 0, 'source': 'fineweb'}
        f.write(json.dumps(record, ensure_ascii=False) + '\n')
        total_tokens += int(approx_tokens)
        num_docs += 1
        if num_docs % 10000 == 0:
            print(f'  Collected {num_docs} docs, ~{total_tokens} tokens')
        if total_tokens >= target_tokens:
            break

print(f'  Done: {num_docs} human documents, ~{total_tokens} tokens')
"
    fi

    python3 -c "
import json, os, random

random.seed(42)
records = []

human_path = os.path.join('$OUTPUT_DIR', 'human_data', 'human.jsonl')
with open(human_path) as f:
    for line in f:
        records.append(line.strip())

synth_dir = os.path.join('$OUTPUT_DIR', 'synthetic_data')
for fname in sorted(os.listdir(synth_dir)):
    if fname.endswith('.jsonl'):
        with open(os.path.join(synth_dir, fname)) as f:
            for line in f:
                records.append(line.strip())

random.shuffle(records)

out_path = os.path.join('$OUTPUT_DIR', 'mixed_data.jsonl')
with open(out_path, 'w') as f:
    for r in records:
        f.write(r + '\n')

print(f'  Mixed dataset: {len(records)} documents -> {out_path}')
"
fi
echo ""

# ─── Step 3: Train detector + gate check ─────────────────────────────────

echo "=== Step 3: Train synthetic-vs-human detector ==="

if [ -d "$OUTPUT_DIR/detector/final_model" ] && [ -f "$OUTPUT_DIR/detector/final_model/model.safetensors" -o -f "$OUTPUT_DIR/detector/final_model/pytorch_model.bin" ]; then
    echo "  Detector already trained, skipping."
else
    python "$SCRIPT_DIR/detector/train_detector.py" \
        --human_data_dir "$OUTPUT_DIR/human_data" \
        --synthetic_data_dir "$OUTPUT_DIR/synthetic_data" \
        --model_name "$DETECTOR_MODEL" \
        --output_dir "$OUTPUT_DIR/detector" \
        --seed 42
fi

echo ""
echo "--- Detector Gate Check (AUC >= 0.95, ECE <= 0.05) ---"
python3 -c "
import json, sys
cal_path = '$OUTPUT_DIR/detector/calibration_results.json'
with open(cal_path) as f:
    cal = json.load(f)
test = cal.get('test', cal.get('val', {}))
auc = test.get('auc', 0)
ece = test.get('ece', 1)
print(f'  AUC = {auc:.4f}  (gate: >= 0.95)')
print(f'  ECE = {ece:.4f}  (gate: <= 0.05)')
if auc < 0.95:
    print(f'  GATE FAILED: AUC {auc:.4f} < 0.95')
    sys.exit(1)
if ece > 0.05:
    print(f'  GATE FAILED: ECE {ece:.4f} > 0.05')
    sys.exit(1)
print('  GATE CHECK PASSED')
"
echo ""

# ─── Step 4: Score mixed data with calibrated detector ───────────────────

echo "=== Step 4: Score mixed data with calibrated detector ==="

if [ -f "$OUTPUT_DIR/scored_data.jsonl" ]; then
    echo "  Scored data already exists, skipping."
else
    python3 -c "
import json, os, torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer
from tqdm import tqdm

model_dir = os.path.join('$OUTPUT_DIR', 'detector', 'final_model')
tokenizer = AutoTokenizer.from_pretrained(model_dir)
model = AutoModelForSequenceClassification.from_pretrained(model_dir, torch_dtype=torch.float16)
model.eval()
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model.to(device)

temp_path = os.path.join(model_dir, 'temperature.pt')
T = 1.0
if os.path.exists(temp_path):
    temp_data = torch.load(temp_path, map_location='cpu')
    T = float(temp_data['temperature'])
    print(f'  Loaded temperature T={T:.4f}')
else:
    print('  WARNING: temperature.pt not found, using T=1.0')

input_path = os.path.join('$OUTPUT_DIR', 'mixed_data.jsonl')
output_path = os.path.join('$OUTPUT_DIR', 'scored_data.jsonl')
batch_size = 64

lines = open(input_path).readlines()
out_f = open(output_path, 'w')

for i in tqdm(range(0, len(lines), batch_size), desc='Scoring'):
    batch_lines = lines[i:i+batch_size]
    batch_records = [json.loads(l) for l in batch_lines]
    texts = [r['text'][:2048] for r in batch_records]

    inputs = tokenizer(texts, padding=True, truncation=True, max_length=512, return_tensors='pt').to(device)
    with torch.no_grad():
        logits = model(**inputs).logits
        scaled_logits = logits / T
        probs = torch.softmax(scaled_logits, dim=-1)
        q_scores = probs[:, 1].cpu().tolist()

    for rec, q in zip(batch_records, q_scores):
        rec['q_score'] = q
        out_f.write(json.dumps(rec, ensure_ascii=False) + '\n')

out_f.close()
print(f'  Scored {len(lines)} documents -> {output_path}')
"
fi
echo ""

# ─── Step 5: Pretraining — 3 seeds x (1 uniform + 6 grid-b + 1 adaptive) = 24 runs

echo "=== Step 5: Pretraining (24 runs: 3 seeds x 8 configs) ==="

for SEED in "${SEEDS[@]}"; do
    # 5a: Uniform
    run_name="uniform_seed${SEED}"
    run_dir="$OUTPUT_DIR/models/$run_name"
    echo "--- Training: $run_name ---"
    if [ -d "$run_dir/final" ]; then
        echo "  Already trained, skipping."
    else
        accelerate launch "$SCRIPT_DIR/training/pretrain_weighted.py" \
            --data_path "$OUTPUT_DIR/scored_data.jsonl" \
            --output_dir "$run_dir" \
            --weighting_method uniform \
            --model_name "$MODEL_NAME" \
            --num_train_tokens "$NUM_TOKENS" \
            --wandb_project "$WANDB_PROJECT" \
            --wandb_run_name "$run_name" \
            --seed "$SEED"
    fi
    echo ""

    # 5b: Grid-b — one run per fixed b value
    for B_VAL in "${GRID_B_VALUES[@]}"; do
        b_tag=$(echo "$B_VAL" | tr '.' 'p')
        run_name="grid_b${b_tag}_seed${SEED}"
        run_dir="$OUTPUT_DIR/models/$run_name"
        echo "--- Training: $run_name (b=$B_VAL) ---"
        if [ -d "$run_dir/final" ]; then
            echo "  Already trained, skipping."
            continue
        fi
        accelerate launch "$SCRIPT_DIR/training/pretrain_weighted.py" \
            --data_path "$OUTPUT_DIR/scored_data.jsonl" \
            --output_dir "$run_dir" \
            --weighting_method grid \
            --grid_b_value "$B_VAL" \
            --model_name "$MODEL_NAME" \
            --num_train_tokens "$NUM_TOKENS" \
            --wandb_project "$WANDB_PROJECT" \
            --wandb_run_name "$run_name" \
            --seed "$SEED"
        echo ""
    done

    # 5c: Adaptive b*
    run_name="adaptive_seed${SEED}"
    run_dir="$OUTPUT_DIR/models/$run_name"
    echo "--- Training: $run_name ---"
    if [ -d "$run_dir/final" ]; then
        echo "  Already trained, skipping."
    else
        accelerate launch "$SCRIPT_DIR/training/pretrain_weighted.py" \
            --data_path "$OUTPUT_DIR/scored_data.jsonl" \
            --output_dir "$run_dir" \
            --weighting_method adaptive \
            --contamination_ratio "$CONTAMINATION_RATIO" \
            --model_name "$MODEL_NAME" \
            --num_train_tokens "$NUM_TOKENS" \
            --wandb_project "$WANDB_PROJECT" \
            --wandb_run_name "$run_name" \
            --seed "$SEED"
    fi
    echo ""
done
echo ""

# ─── Step 6: Evaluate all models ─────────────────────────────────────────

echo "=== Step 6: Evaluate all 24 models ==="

for SEED in "${SEEDS[@]}"; do
    # Eval uniform
    run_name="uniform_seed${SEED}"
    eval_dir="$OUTPUT_DIR/eval/$run_name"
    echo "--- Evaluating: $run_name ---"
    if [ -f "$eval_dir/eval_results.json" ]; then
        echo "  Already evaluated, skipping."
    else
        python "$SCRIPT_DIR/evaluation/eval_pipeline.py" \
            --model_path "$OUTPUT_DIR/models/$run_name/final" \
            --output_dir "$eval_dir" \
            --seed "$SEED"
    fi

    # Eval grid-b variants
    for B_VAL in "${GRID_B_VALUES[@]}"; do
        b_tag=$(echo "$B_VAL" | tr '.' 'p')
        run_name="grid_b${b_tag}_seed${SEED}"
        eval_dir="$OUTPUT_DIR/eval/$run_name"
        echo "--- Evaluating: $run_name ---"
        if [ -f "$eval_dir/eval_results.json" ]; then
            echo "  Already evaluated, skipping."
            continue
        fi
        python "$SCRIPT_DIR/evaluation/eval_pipeline.py" \
            --model_path "$OUTPUT_DIR/models/$run_name/final" \
            --output_dir "$eval_dir" \
            --seed "$SEED"
    done

    # Eval adaptive
    run_name="adaptive_seed${SEED}"
    eval_dir="$OUTPUT_DIR/eval/$run_name"
    echo "--- Evaluating: $run_name ---"
    if [ -f "$eval_dir/eval_results.json" ]; then
        echo "  Already evaluated, skipping."
    else
        python "$SCRIPT_DIR/evaluation/eval_pipeline.py" \
            --model_path "$OUTPUT_DIR/models/$run_name/final" \
            --output_dir "$eval_dir" \
            --seed "$SEED"
    fi
done
echo ""

# ─── Step 7: Multi-seed comparison + MVP pass check ──────────────────────

echo "=== Step 7: Multi-seed comparison and MVP pass check ==="

python "$SCRIPT_DIR/evaluation/compare_results.py" \
    --eval_base_dir "$OUTPUT_DIR/eval" \
    --output_path "$OUTPUT_DIR/mvp_summary.json"

echo ""
echo "============================================================"
echo "  MVP Pipeline Complete"
echo "  Results: $OUTPUT_DIR/mvp_summary.json"
echo "============================================================"
