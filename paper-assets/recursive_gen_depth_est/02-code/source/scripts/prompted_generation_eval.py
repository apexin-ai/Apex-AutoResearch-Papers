"""
Prompted generation ecological validity (plan_016).
Verifies depth signal persists with topic-prompted continuation vs BOS-seeded generation.
Uses GPT-2 XL as generator, Pythia-1.4B as reference for feature extraction.
50 prompts x 100 samples = 5000 per depth, 4 depths, RF 5-fold CV.
"""

import argparse
import gc
import json
import os
import time

import numpy as np
import torch
from collections import Counter
from scipy.stats import skew, kurtosis, entropy
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import accuracy_score, roc_auc_score, classification_report
from transformers import (
    AutoTokenizer, AutoModelForCausalLM,
    TrainingArguments, Trainer, DataCollatorForLanguageModeling,
)
from peft import LoraConfig, get_peft_model, PeftModel
from torch.utils.data import Dataset
from tqdm import tqdm

MODEL_PATH = "/root/autodl-tmp/models/gpt2-xl"
REF_MODEL_PATH = "/root/autodl-tmp/models/pythia-1.4b"
PROJECT_DIR = "/root/autodl-tmp/recursive_gen_depth_est"
DATA_DIR = os.path.join(PROJECT_DIR, "data/prompted_gen")
CKPT_DIR = os.path.join(PROJECT_DIR, "checkpoints/prompted_gen")
RESULTS_DIR = os.path.join(PROJECT_DIR, "results/prompted_generation")

NUM_DEPTHS = 4
SAMPLES_PER_PROMPT = 100
GEN_BATCH = 16
GEN_MAX_NEW = 512
GEN_TOP_P = 0.95
GEN_TEMP = 1.0
LORA_R = 16
LORA_ALPHA = 32
TARGET_MODULES = ["c_attn", "c_proj"]
TRAIN_EPOCHS = 3
TRAIN_LR = 2e-4
TRAIN_BATCH = 8
TRAIN_GRAD_ACCUM = 2
FEAT_BATCH = 16
RF_N = 200
SEED = 42
CV_FOLDS = 5

FEATURE_NAMES = [
    "mean_ppl", "var_ppl", "skewness_ppl", "kurtosis_ppl",
    "p10_ppl", "p25_ppl", "p50_ppl", "p75_ppl", "p90_ppl",
    "mean_surprisal", "var_surprisal", "entropy_of_surprisal",
    "type_token_ratio", "hapax_ratio", "bigram_entropy", "trigram_entropy",
    "rep_2gram", "rep_3gram", "rep_4gram",
]

PROMPTS = [
    "The following article discusses recent advances in quantum computing. ",
    "A new study published in Nature reveals important findings about ",
    "Researchers at MIT have discovered a novel approach to ",
    "The field of neuroscience has recently made progress in understanding ",
    "Climate scientists have developed new models that predict ",
    "The latest policy changes in international trade agreements have ",
    "Political analysts are debating the implications of recent electoral reforms ",
    "Government officials announced new measures to address ",
    "The relationship between national security and civil liberties has become ",
    "Recent diplomatic negotiations between major powers focused on ",
    "The development of autonomous vehicles has reached a critical stage where ",
    "Cybersecurity experts warn about emerging threats in ",
    "The semiconductor industry faces new challenges related to ",
    "Advances in renewable energy technology are transforming ",
    "The integration of machine learning into healthcare diagnostics has ",
    "Medical researchers have identified new biomarkers for early detection of ",
    "The global response to infectious disease outbreaks has evolved since ",
    "Nutritional science studies suggest that dietary patterns affect ",
    "Mental health awareness campaigns have increased attention to ",
    "Pharmaceutical companies are investing heavily in developing treatments for ",
    "Environmental conservation efforts in tropical rainforests have shown ",
    "Ocean acidification continues to threaten marine ecosystems by ",
    "Urban planning strategies for reducing carbon emissions include ",
    "The impact of deforestation on local water cycles has been studied ",
    "Biodiversity loss in freshwater habitats has accelerated due to ",
    "The global supply chain disruptions have led to significant changes in ",
    "Central banks around the world are adjusting monetary policy to combat ",
    "The rise of digital currencies has implications for traditional banking ",
    "Labor market trends indicate a growing demand for workers in ",
    "International trade patterns have shifted dramatically as countries seek ",
    "Higher education institutions are adapting their curricula to address ",
    "The effectiveness of online learning platforms has been debated since ",
    "Early childhood education programs have demonstrated lasting effects on ",
    "STEM education initiatives aim to prepare students for careers in ",
    "The role of standardized testing in measuring student achievement remains ",
    "Professional athletes are increasingly using data analytics to improve ",
    "The economics of major sporting events have changed significantly with ",
    "Sports medicine research has advanced our understanding of injury prevention ",
    "The governance of international athletic competitions faces challenges from ",
    "Youth sports participation rates have fluctuated in recent years due to ",
    "Contemporary art museums are exploring new ways to engage audiences through ",
    "The music industry has undergone fundamental changes driven by streaming ",
    "Independent filmmakers are finding new distribution channels that allow ",
    "The preservation of cultural heritage sites requires balancing tourism with ",
    "Literary criticism has evolved to incorporate perspectives from diverse ",
    "Archaeological discoveries in the Mediterranean region have shed light on ",
    "The industrial revolution transformed social structures by creating ",
    "Historical analysis of ancient trade routes reveals connections between ",
    "The development of democratic institutions can be traced through ",
    "Wartime innovations in communication technology led to lasting changes in ",
]


class TextDataset(Dataset):
    def __init__(self, path, tokenizer, max_len=512):
        self.examples = []
        with open(path) as f:
            for line in f:
                rec = json.loads(line.strip())
                enc = tokenizer(rec["text"], truncation=True,
                                max_length=max_len, padding=False)
                self.examples.append(enc)

    def __len__(self):
        return len(self.examples)

    def __getitem__(self, idx):
        return {k: torch.tensor(v) for k, v in self.examples[idx].items()}


def _save_jsonl(path, records):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        for r in records:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")


def generate_prompted(model, tokenizer, prompts, samples_per_prompt,
                      max_new, top_p, temp, batch_size, depth, device):
    model.eval()
    results = []
    total = len(prompts) * samples_per_prompt
    generated = 0

    for pi, prompt in enumerate(prompts):
        ids = tokenizer.encode(prompt, add_special_tokens=False)
        prompt_len = len(ids)

        for bs in range(0, samples_per_prompt, batch_size):
            be = min(bs + batch_size, samples_per_prompt)
            n = be - bs
            input_ids = torch.tensor([ids] * n, device=device)
            attn = torch.ones_like(input_ids)

            with torch.no_grad():
                out = model.generate(
                    input_ids=input_ids, attention_mask=attn,
                    max_new_tokens=max_new, do_sample=True,
                    top_p=top_p, temperature=temp,
                    pad_token_id=tokenizer.pad_token_id,
                )

            for i in range(n):
                cont = out[i][prompt_len:]
                text = tokenizer.decode(cont, skip_special_tokens=True).strip()
                results.append({
                    "text": text, "depth": depth,
                    "prompt_idx": pi, "seed_id": generated,
                    "token_count": len(cont),
                })
                generated += 1

        if (pi + 1) % 10 == 0:
            print(f"  [{pi+1}/{len(prompts)}] {generated}/{total} samples")

    print(f"  Generated {generated} samples for depth {depth}")
    return results


def finetune_lora(data_path, out_dir, tokenizer):
    print(f"  Loading base model for LoRA...")
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_PATH, torch_dtype=torch.bfloat16)
    config = LoraConfig(
        r=LORA_R, lora_alpha=LORA_ALPHA, target_modules=TARGET_MODULES,
        lora_dropout=0.05, bias="none", task_type="CAUSAL_LM",
    )
    model = get_peft_model(model, config)
    model.print_trainable_parameters()

    ds = TextDataset(data_path, tokenizer)
    print(f"  Dataset: {len(ds)} samples")

    training_args = TrainingArguments(
        output_dir=out_dir, num_train_epochs=TRAIN_EPOCHS,
        per_device_train_batch_size=TRAIN_BATCH,
        gradient_accumulation_steps=TRAIN_GRAD_ACCUM,
        learning_rate=TRAIN_LR, bf16=True,
        logging_steps=50, save_strategy="epoch", save_total_limit=1,
        seed=SEED, report_to="none", remove_unused_columns=False,
        dataloader_pin_memory=True, dataloader_num_workers=4,
    )

    trainer = Trainer(
        model=model, args=training_args, train_dataset=ds,
        data_collator=DataCollatorForLanguageModeling(
            tokenizer=tokenizer, mlm=False),
    )

    result = trainer.train()
    print(f"  Final loss: {result.training_loss:.4f}")
    model.save_pretrained(out_dir)
    tokenizer.save_pretrained(out_dir)

    del model, trainer
    gc.collect()
    torch.cuda.empty_cache()


def _lexical_features(token_ids):
    total = len(token_ids)
    if total == 0:
        return {"type_token_ratio": 0.0, "hapax_ratio": 0.0,
                "bigram_entropy": 0.0, "trigram_entropy": 0.0}
    counts = Counter(token_ids)
    unique = len(counts)
    ttr = unique / total
    hapax = sum(1 for c in counts.values() if c == 1)
    hapax_ratio = hapax / unique if unique > 0 else 0.0

    bigrams = [tuple(token_ids[i:i+2]) for i in range(total - 1)]
    bg_ent = 0.0
    if bigrams:
        bg_freq = np.array(list(Counter(bigrams).values()), dtype=np.float64)
        bg_freq /= bg_freq.sum()
        bg_ent = float(entropy(bg_freq))

    trigrams = [tuple(token_ids[i:i+3]) for i in range(total - 2)]
    tg_ent = 0.0
    if trigrams:
        tg_freq = np.array(list(Counter(trigrams).values()), dtype=np.float64)
        tg_freq /= tg_freq.sum()
        tg_ent = float(entropy(tg_freq))

    return {"type_token_ratio": ttr, "hapax_ratio": hapax_ratio,
            "bigram_entropy": bg_ent, "trigram_entropy": tg_ent}


def _rep_rate(ids, n):
    if len(ids) < n:
        return 0.0
    ngrams = [tuple(ids[i:i+n]) for i in range(len(ids) - n + 1)]
    c = Counter(ngrams)
    repeated = sum(v - 1 for v in c.values() if v > 1)
    return repeated / len(ngrams) if ngrams else 0.0


def _surprisal_entropy(surprisals, n_bins=50):
    if len(surprisals) < 2:
        return 0.0
    hist, _ = np.histogram(surprisals, bins=n_bins, density=True)
    hist = hist[hist > 0]
    if len(hist) == 0 or hist.sum() == 0:
        return 0.0
    hist = hist / hist.sum()
    return float(entropy(hist))


def extract_features_batch(model, tokenizer, texts, trunc_len, device):
    encoded = [tokenizer.encode(t, add_special_tokens=False)[:trunc_len]
               for t in texts]
    max_len = max(len(e) for e in encoded)
    pad_id = tokenizer.pad_token_id or tokenizer.eos_token_id

    input_ids_list, attn_list = [], []
    for e in encoded:
        pad_len = max_len - len(e)
        input_ids_list.append(e + [pad_id] * pad_len)
        attn_list.append([1] * len(e) + [0] * pad_len)

    input_ids = torch.tensor(input_ids_list, dtype=torch.long, device=device)
    attn_mask = torch.tensor(attn_list, dtype=torch.long, device=device)

    with torch.no_grad():
        logits = model(input_ids=input_ids, attention_mask=attn_mask).logits

    shift_logits = logits[:, :-1, :].contiguous()
    shift_labels = input_ids[:, 1:].contiguous()
    per_token_loss = torch.nn.CrossEntropyLoss(reduction="none")(
        shift_logits.view(-1, shift_logits.size(-1)),
        shift_labels.view(-1),
    ).view(shift_logits.size(0), shift_logits.size(1))

    results = []
    for i in range(len(texts)):
        seq_len = len(encoded[i])
        surprisals = (per_token_loss[i, :seq_len - 1].cpu().numpy().astype(np.float64)
                      if seq_len > 1 else np.array([0.0]))
        ppl = np.exp(np.clip(surprisals, 0, 20))

        token_ids = encoded[i]
        lex = _lexical_features(token_ids)

        results.append({
            "mean_ppl": float(np.mean(ppl)),
            "var_ppl": float(np.var(ppl)),
            "skewness_ppl": float(skew(ppl)) if len(ppl) > 2 else 0.0,
            "kurtosis_ppl": float(kurtosis(ppl)) if len(ppl) > 3 else 0.0,
            "p10_ppl": float(np.percentile(ppl, 10)),
            "p25_ppl": float(np.percentile(ppl, 25)),
            "p50_ppl": float(np.percentile(ppl, 50)),
            "p75_ppl": float(np.percentile(ppl, 75)),
            "p90_ppl": float(np.percentile(ppl, 90)),
            "mean_surprisal": float(np.mean(surprisals)),
            "var_surprisal": float(np.var(surprisals)),
            "entropy_of_surprisal": _surprisal_entropy(surprisals),
            **lex,
            "rep_2gram": _rep_rate(token_ids, 2),
            "rep_3gram": _rep_rate(token_ids, 3),
            "rep_4gram": _rep_rate(token_ids, 4),
        })

    return results


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--gpu", type=int, default=1)
    args = parser.parse_args()

    os.environ["CUDA_VISIBLE_DEVICES"] = str(args.gpu)
    os.environ["HF_HOME"] = "/root/autodl-tmp/.hf_cache"
    os.environ["HF_HUB_DISABLE_XET"] = "1"
    torch.manual_seed(SEED)
    device = torch.device("cuda:0")

    t0 = time.time()

    os.makedirs(DATA_DIR, exist_ok=True)
    with open(os.path.join(DATA_DIR, "prompts.json"), "w") as f:
        json.dump(PROMPTS, f, indent=2)
    print(f"Saved {len(PROMPTS)} prompts")

    # ── Phase 1: Generate d0-d3 ──
    print("\n" + "=" * 60)
    print("PHASE 1: Prompted generation (d0-d3)")
    print("=" * 60)

    tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    d0_path = os.path.join(DATA_DIR, "depth_0.jsonl")
    if not os.path.exists(d0_path):
        print("\n--- d0: base GPT-2 XL + topic prompts ---")
        model = AutoModelForCausalLM.from_pretrained(
            MODEL_PATH, torch_dtype=torch.bfloat16).to(device)
        samples = generate_prompted(model, tokenizer, PROMPTS, SAMPLES_PER_PROMPT,
                                    GEN_MAX_NEW, GEN_TOP_P, GEN_TEMP,
                                    GEN_BATCH, 0, device)
        _save_jsonl(d0_path, samples)
        del model
        gc.collect()
        torch.cuda.empty_cache()
    else:
        print(f"d0 exists, skipping")

    for depth in range(1, NUM_DEPTHS):
        prev = depth - 1
        prev_data = os.path.join(DATA_DIR, f"depth_{prev}.jsonl")
        adapter_dir = os.path.join(CKPT_DIR, f"lora_depth_{prev}")
        cur_data = os.path.join(DATA_DIR, f"depth_{depth}.jsonl")

        if os.path.exists(cur_data):
            print(f"d{depth} exists, skipping")
            continue

        if not os.path.exists(os.path.join(adapter_dir, "adapter_config.json")):
            print(f"\n--- LoRA fine-tune on d{prev} ---")
            finetune_lora(prev_data, adapter_dir, tokenizer)
        else:
            print(f"LoRA adapter d{prev} exists, skipping")

        print(f"\n--- d{depth}: LoRA + topic prompts ---")
        base = AutoModelForCausalLM.from_pretrained(
            MODEL_PATH, torch_dtype=torch.bfloat16)
        model = PeftModel.from_pretrained(base, adapter_dir).to(device)
        samples = generate_prompted(model, tokenizer, PROMPTS, SAMPLES_PER_PROMPT,
                                    GEN_MAX_NEW, GEN_TOP_P, GEN_TEMP,
                                    GEN_BATCH, depth, device)
        _save_jsonl(cur_data, samples)
        del model, base
        gc.collect()
        torch.cuda.empty_cache()

    # ── Phase 2: Feature extraction ──
    print("\n" + "=" * 60)
    print("PHASE 2: Feature extraction (Pythia-1.4B)")
    print("=" * 60)

    features_path = os.path.join(DATA_DIR, "features.jsonl")
    if not os.path.exists(features_path):
        ref_tok = AutoTokenizer.from_pretrained(REF_MODEL_PATH)
        if ref_tok.pad_token is None:
            ref_tok.pad_token = ref_tok.eos_token

        depth_medians = {}
        for d in range(NUM_DEPTHS):
            fpath = os.path.join(DATA_DIR, f"depth_{d}.jsonl")
            lengths = []
            with open(fpath) as f:
                for line in f:
                    ids = ref_tok.encode(
                        json.loads(line.strip())["text"],
                        add_special_tokens=False)
                    lengths.append(len(ids))
            med = int(np.median(lengths))
            depth_medians[d] = med
            print(f"  d{d}: n={len(lengths)}, median={med}, "
                  f"min={min(lengths)}, max={max(lengths)}")
        trunc_len = min(depth_medians.values())
        print(f"  Truncation: {trunc_len} tokens")

        ref_model = AutoModelForCausalLM.from_pretrained(
            REF_MODEL_PATH, torch_dtype=torch.float16).to(device)
        ref_model.eval()

        out_f = open(features_path, "w")
        sid = 0
        for d in range(NUM_DEPTHS):
            texts = []
            with open(os.path.join(DATA_DIR, f"depth_{d}.jsonl")) as f:
                for line in f:
                    texts.append(json.loads(line.strip())["text"])
            for start in tqdm(range(0, len(texts), FEAT_BATCH),
                              desc=f"d{d} features"):
                batch = texts[start:start + FEAT_BATCH]
                feats = extract_features_batch(
                    ref_model, ref_tok, batch, trunc_len, device)
                for feat in feats:
                    row = {"depth": d, "sample_id": sid}
                    row.update(feat)
                    out_f.write(json.dumps(row) + "\n")
                    sid += 1
        out_f.close()
        print(f"Features: {sid} samples -> {features_path}")

        del ref_model
        gc.collect()
        torch.cuda.empty_cache()
    else:
        print(f"Features exist, skipping")

    # ── Phase 3: RF classification ──
    print("\n" + "=" * 60)
    print("PHASE 3: RF classification (5-fold CV)")
    print("=" * 60)

    records = []
    with open(features_path) as f:
        for line in f:
            if line.strip():
                records.append(json.loads(line))

    X = np.array([[r[k] for k in FEATURE_NAMES] for r in records],
                 dtype=np.float64)
    y = np.array([r["depth"] for r in records], dtype=np.int64)
    X = np.nan_to_num(X, nan=0.0, posinf=0.0, neginf=0.0)
    print(f"Data: {X.shape[0]} x {X.shape[1]}")
    print(f"Distribution: {dict(Counter(y))}")

    skf = StratifiedKFold(n_splits=CV_FOLDS, shuffle=True, random_state=SEED)
    fold_accs = []
    all_yt, all_yp, all_yprob = [], [], []

    for fold, (tr, te) in enumerate(skf.split(X, y)):
        rf = RandomForestClassifier(
            n_estimators=RF_N, random_state=SEED, n_jobs=-1)
        rf.fit(X[tr], y[tr])
        pred = rf.predict(X[te])
        prob = rf.predict_proba(X[te])
        acc = accuracy_score(y[te], pred)
        fold_accs.append(acc)
        all_yt.extend(y[te])
        all_yp.extend(pred)
        all_yprob.extend(prob)
        print(f"  Fold {fold+1}: {acc:.4f}")

    all_yt = np.array(all_yt)
    all_yp = np.array(all_yp)
    all_yprob = np.array(all_yprob)

    mean_acc = np.mean(fold_accs)
    std_acc = np.std(fold_accs)
    ci = [round(mean_acc - 1.96 * std_acc / np.sqrt(CV_FOLDS), 4),
          round(mean_acc + 1.96 * std_acc / np.sqrt(CV_FOLDS), 4)]

    pair_auc = {}
    for d1 in range(NUM_DEPTHS):
        for d2 in range(d1 + 1, NUM_DEPTHS):
            mask = np.isin(all_yt, [d1, d2])
            if mask.sum() < 2:
                continue
            yt_bin = (all_yt[mask] == d2).astype(int)
            if len(np.unique(yt_bin)) < 2:
                continue
            auc = roc_auc_score(yt_bin, all_yprob[mask, d2])
            pair_auc[f"d{d1}_vs_d{d2}"] = round(auc, 4)

    rf_all = RandomForestClassifier(
        n_estimators=RF_N, random_state=SEED, n_jobs=-1)
    rf_all.fit(X, y)
    imp = rf_all.feature_importances_
    top5_idx = np.argsort(imp)[::-1][:5]
    top5 = [(FEATURE_NAMES[i], round(float(imp[i]), 4)) for i in top5_idx]

    print(f"\n  Accuracy: {mean_acc:.4f} [{ci[0]}, {ci[1]}]")
    print(f"  Pairwise AUC: {pair_auc}")
    print(f"  Top-5 features: {top5}")
    print(f"\n{classification_report(all_yt, all_yp, target_names=[f'd{d}' for d in range(NUM_DEPTHS)])}")

    baseline = 0.833
    delta = round((mean_acc - baseline) * 100, 2)

    summary = {
        "experiment": "prompted_gen_gpt2xl_001",
        "model": "gpt2-xl",
        "reference_model": "pythia-1.4b",
        "generation_mode": "topic_prompted",
        "num_prompts": len(PROMPTS),
        "samples_per_prompt": SAMPLES_PER_PROMPT,
        "samples_per_depth": len(PROMPTS) * SAMPLES_PER_PROMPT,
        "four_class_accuracy": round(mean_acc, 4),
        "accuracy_ci_95": ci,
        "fold_accuracies": [round(a, 4) for a in fold_accs],
        "pairwise_auc": pair_auc,
        "top5_features": top5,
        "baseline_bos_seeded_acc": baseline,
        "delta_vs_baseline_pp": delta,
        "elapsed_hours": round((time.time() - t0) / 3600, 2),
    }

    os.makedirs(RESULTS_DIR, exist_ok=True)
    summary_path = os.path.join(RESULTS_DIR, "summary.json")
    with open(summary_path, "w") as f:
        json.dump(summary, f, indent=2)

    print(f"\n{'=' * 60}")
    print(f"  RESULT: {mean_acc:.4f} [{ci[0]}, {ci[1]}]")
    print(f"  BASELINE (BOS-seeded): {baseline}")
    print(f"  DELTA: {delta:+.1f}pp")
    print(f"  Time: {(time.time() - t0)/3600:.1f}h")
    print(f"{'=' * 60}")
    print(f"Summary: {summary_path}")


if __name__ == "__main__":
    main()
