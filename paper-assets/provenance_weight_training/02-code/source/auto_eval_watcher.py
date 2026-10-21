"""Watch all experiment checkpoints and auto-run eval_perplexity.py on completion.

GPU selection: env EVAL_GPU overrides; otherwise picks GPU with lowest memory usage via nvidia-smi.
"""
import glob
import logging
import os
import subprocess
import sys
import time

BASE_DIR = "/root/provenance_weight_training"
MODELS_DIR = os.path.join(BASE_DIR, "output/models")
EVAL_DIR = os.path.join(BASE_DIR, "output/eval_results")
EVAL_SCRIPT = os.path.join(BASE_DIR, "eval_perplexity.py")
DATA_PATH = os.path.join(BASE_DIR, "data/human/eval_holdout.jsonl")
LOG_PATH = os.path.join(BASE_DIR, "logs/auto_eval_watcher.log")
SCAN_INTERVAL = 60
MIN_FREE_MB = 15000

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(LOG_PATH),
        logging.StreamHandler(sys.stdout),
    ],
)
log = logging.getLogger(__name__)


def get_least_loaded_gpu():
    env_gpu = os.environ.get("EVAL_GPU")
    if env_gpu is not None:
        log.info(f"Using EVAL_GPU from env: {env_gpu}")
        return env_gpu
    try:
        result = subprocess.run(
            ["nvidia-smi", "--query-gpu=index,memory.used,memory.total",
             "--format=csv,noheader,nounits"],
            capture_output=True, text=True, timeout=10,
        )
        if result.returncode != 0:
            log.warning(f"nvidia-smi failed (rc={result.returncode}), falling back to GPU 0")
            return "0"
        best_idx, best_used, best_free = "0", float("inf"), 0
        for line in result.stdout.strip().split("\n"):
            parts = [p.strip() for p in line.split(",")]
            if len(parts) < 3:
                continue
            idx, used, total = parts[0], int(parts[1]), int(parts[2])
            free = total - used
            if used < best_used:
                best_idx, best_used, best_free = idx, used, free
        if best_free < MIN_FREE_MB:
            log.warning(f"Best GPU {best_idx} has only {best_free}MB free (need {MIN_FREE_MB}MB), using it anyway")
        log.info(f"Selected GPU {best_idx} (used={best_used}MB, free={best_free}MB)")
        return best_idx
    except Exception as e:
        log.warning(f"GPU detection failed ({e}), falling back to GPU 0")
        return "0"


def extract_exp_id(dirname):
    return os.path.basename(dirname)


def find_ready_checkpoints():
    ready = []
    for d in sorted(glob.glob(os.path.join(MODELS_DIR, "*"))):
        if not os.path.isdir(d):
            continue
        exp_id = extract_exp_id(d)
        final_dir = os.path.join(d, "final")
        if os.path.isdir(final_dir) and os.path.isfile(os.path.join(final_dir, "model.safetensors")):
            result_name = f"{exp_id}_eval.json"
            result_path = os.path.join(EVAL_DIR, result_name)
            if not os.path.exists(result_path):
                ready.append((exp_id, final_dir, result_path))
    return ready


def run_eval(exp_id, checkpoint_path, output_path):
    eval_gpu = get_least_loaded_gpu()
    cmd = [
        sys.executable, EVAL_SCRIPT,
        "--checkpoints", checkpoint_path,
        "--data_path", DATA_PATH,
        "--output_path", output_path,
    ]
    env = os.environ.copy()
    env["CUDA_VISIBLE_DEVICES"] = eval_gpu
    log.info(f"Starting eval: {exp_id} on GPU {eval_gpu} -> {output_path}")
    log.info(f"  cmd: {' '.join(cmd)}")
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, env=env, timeout=1800)
        if proc.returncode == 0:
            log.info(f"Eval succeeded: {exp_id}")
            if proc.stdout:
                for line in proc.stdout.strip().split("\n")[-5:]:
                    log.info(f"  {line}")
            return True
        else:
            log.error(f"Eval failed (rc={proc.returncode}): {exp_id}")
            if proc.stderr:
                for line in proc.stderr.strip().split("\n")[-10:]:
                    log.error(f"  {line}")
            if "CUDA out of memory" in (proc.stderr or ""):
                log.info(f"GPU OOM, retrying on CPU: {exp_id}")
                env["CUDA_VISIBLE_DEVICES"] = ""
                proc2 = subprocess.run(cmd, capture_output=True, text=True, env=env, timeout=3600)
                if proc2.returncode == 0:
                    log.info(f"CPU eval succeeded: {exp_id}")
                    return True
                log.error(f"CPU eval also failed: {exp_id}")
            return False
    except subprocess.TimeoutExpired:
        log.error(f"Eval timed out: {exp_id}")
        return False
    except Exception as e:
        log.error(f"Eval exception: {exp_id}: {e}")
        return False


def main():
    os.makedirs(EVAL_DIR, exist_ok=True)
    os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)
    log.info("=" * 60)
    log.info("Auto eval watcher started")
    log.info(f"  Models dir: {MODELS_DIR}")
    log.info(f"  Eval dir:   {EVAL_DIR}")
    log.info(f"  GPU select: dynamic (least loaded) | env EVAL_GPU overrides")
    log.info(f"  Min free:   {MIN_FREE_MB}MB")
    log.info(f"  Interval:   {SCAN_INTERVAL}s")
    log.info("=" * 60)

    evaluated = set()
    while True:
        try:
            ready = find_ready_checkpoints()
            if ready:
                log.info(f"Found {len(ready)} checkpoint(s) to eval")
            for exp_id, ckpt_path, result_path in ready:
                if exp_id in evaluated:
                    continue
                success = run_eval(exp_id, ckpt_path, result_path)
                if success:
                    evaluated.add(exp_id)
                else:
                    evaluated.add(exp_id)
                    log.warning(f"Skipping {exp_id} after failure (won't retry)")
        except Exception as e:
            log.error(f"Scan error: {e}")
        time.sleep(SCAN_INTERVAL)


if __name__ == "__main__":
    main()
