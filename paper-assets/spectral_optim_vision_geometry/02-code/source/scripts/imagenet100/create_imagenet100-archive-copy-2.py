# DEPRECATED: 本脚本定义的子集与实际使用数据不同，见 D061
"""Create ImageNet-100 subset from ImageNet-1K via symlinks.

Uses the first 100 classes sorted by WordNet ID (deterministic, reproducible).
Works for both train/ and val/ splits.

Usage:
    python create_imagenet100.py --src /path/to/imagenet-1k --dst /path/to/imagenet-100
"""
import argparse
import os


IN100_CLASSES = [
    "n01440764", "n01443537", "n01484850", "n01491361", "n01494475",
    "n01496331", "n01498041", "n01514668", "n01514859", "n01518878",
    "n01530575", "n01531178", "n01532829", "n01534433", "n01537544",
    "n01558993", "n01560419", "n01580077", "n01582220", "n01592084",
    "n01601694", "n01608432", "n01614925", "n01616318", "n01622779",
    "n01629819", "n01630670", "n01631663", "n01632458", "n01632777",
    "n01641577", "n01644373", "n01644900", "n01664065", "n01665541",
    "n01667114", "n01667778", "n01669191", "n01675722", "n01677366",
    "n01682714", "n01685808", "n01687978", "n01688243", "n01689811",
    "n01692333", "n01693334", "n01694178", "n01695060", "n01697457",
    "n01698640", "n01704323", "n01728572", "n01728920", "n01729322",
    "n01729977", "n01734418", "n01735189", "n01737021", "n01739381",
    "n01740131", "n01742172", "n01744401", "n01748264", "n01749939",
    "n01751748", "n01753488", "n01755581", "n01756291", "n01768244",
    "n01770081", "n01770393", "n01773157", "n01773549", "n01773797",
    "n01774384", "n01774750", "n01775062", "n01776313", "n01784675",
    "n01795545", "n01796340", "n01797886", "n01798484", "n01806143",
    "n01806567", "n01807496", "n01817953", "n01818515", "n01819313",
    "n01820546", "n01824575", "n01828970", "n01829413", "n01833805",
    "n01843065", "n01843383", "n01847000", "n01855032", "n01855672",
]

assert len(IN100_CLASSES) == 100


def create_subset(src_root, dst_root):
    for split in ["train", "val"]:
        src_split = os.path.join(src_root, split)
        if not os.path.isdir(src_split):
            print(f"SKIP {split}/ (not found at {src_split})")
            continue
        dst_split = os.path.join(dst_root, split)
        os.makedirs(dst_split, exist_ok=True)
        linked = 0
        for cls_id in IN100_CLASSES:
            src_cls = os.path.join(src_split, cls_id)
            dst_cls = os.path.join(dst_split, cls_id)
            if not os.path.isdir(src_cls):
                print(f"  WARN: {cls_id} not found in {split}/")
                continue
            if os.path.exists(dst_cls):
                continue
            os.symlink(src_cls, dst_cls)
            linked += 1
        n_imgs = sum(
            len(os.listdir(os.path.join(dst_split, c)))
            for c in IN100_CLASSES
            if os.path.isdir(os.path.join(dst_split, c))
        )
        print(f"{split}/: {linked} new links, 100 classes, {n_imgs} images total")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--src", required=True, help="ImageNet-1K root (contains train/ and val/)")
    parser.add_argument("--dst", required=True, help="Output ImageNet-100 root")
    args = parser.parse_args()
    create_subset(args.src, args.dst)
