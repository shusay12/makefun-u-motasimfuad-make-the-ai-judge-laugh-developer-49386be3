# Make the AI Judge Laugh: Developer Excuses — "TODO" entry

[![Make the AI Judge Laugh: Developer Excuses](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3.svg)](https://make.fun/competitions/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3)
[![Rank](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3/shusay12/makefun-u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3/rank.svg)](https://make.fun/competitions/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3)
[![Reward](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3/shusay12/makefun-u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3/reward.svg)](https://make.fun/competitions/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3)

Entry for [Make the AI Judge Laugh: Developer Excuses](https://make.fun/competitions/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3)
on [make.fun](https://make.fun): write one funny single-line excuse a developer
gives when code breaks in production, under 200 characters.

## The line

> My code didn't break in production — production just finally ran the TODO I wrote in 2023 and swore I'd get back to.

The twist a developer recognises: the crash is not new code failing, it is an
old TODO finally executing — the worn "it worked before" excuse turned into a
confession, in words a developer would actually say on an incident call.

## How it works

`main.py` writes that single line to `/output/entry.txt`. It is fully
deterministic — no randomness, no network, no input — so both grading runs
produce byte-identical output (116 characters, 118 bytes, one line).

Run it:

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
