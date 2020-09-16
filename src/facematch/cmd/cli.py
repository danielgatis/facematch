import argparse
import json
import sys

from ..face import EncodingError, match


def main():
    ap = argparse.ArgumentParser()

    ap.add_argument(
        "-t",
        "--threshold",
        type=float,
        default=0.6,
        help="How much distance between faces to consider it a match. Lower is more strict. (default=0.6)",
    )

    ap.add_argument(
        "-o",
        "--output",
        type=argparse.FileType("wb"),
        help="Path to the debug png image.",
    )

    ap.add_argument(
        "input1", type=argparse.FileType("rb"), help="Path to the first input image.",
    )

    ap.add_argument(
        "input2", type=argparse.FileType("rb"), help="Path to the second input image.",
    )

    args = ap.parse_args()

    try:
        result, distance, data = match(
            args.input1.read(), args.input2.read(), args.threshold
        )
    except EncodingError as err:
        print(err)
        sys.exit(2)

    if args.output:
        args.output.write(data)

    if result:
        print(json.dumps(dict(match=True, distance=distance)))
        sys.exit(0)
    else:
        print(json.dumps(dict(match=False, distance=distance)))
        sys.exit(1)


if __name__ == "__main__":
    main()
