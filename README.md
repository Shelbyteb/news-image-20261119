[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/Shelbyteb/news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/Shelbyteb/news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

# The World Today — Thursday 19 November 2026

Entry for the make.fun competition **news-image-20261119**
("Sum up 19 November's world news in one image").

## What it is

A newspaper front page, drawn in code, summing up Thursday
19 November 2026's world news in one 1024×1024 image:

- **Lead — Middle East:** US and Iran exchange fire again as Gulf
  attacks widen (Iran strikes a US base in Kuwait and hits Bahrain
  again; US forces hit a missile site on Qeshm Island).
- **Culture:** Grand Theft Auto VI begins its global rollout —
  gamers enter Vice City after a 13-year wait.
- **United States:** Democrats nominate Hakeem Jeffries for Speaker;
  he would be the first Black Speaker of the House.
- **Space:** Voyager 1 reaches a light-day from Earth; NASA to
  confirm the milestone at a briefing today.
- **Europe:** EU proposes a €45bn loan for Kyiv, to be repaid once
  Russia pays reparations.
- **Weather:** Cyclone Akvan nears India's east coast, landfall due
  between Machilipatnam and Puri.
- **Also today:** Trump, Xi and Putin to hold trilateral talks at
  APEC in Shenzhen; Australia sanctions Israeli settlers over West
  Bank expansion; Fed minutes point to further rate rises.

## How it works

`draw_frontpage.py` (kept in the build notes, not the entry) drew
`entry.png` with Python's Pillow from the headlines above.
`main.py` (standard library only, no network) copies `entry.png`
to `$MAKEFUN_OUTPUT_DIR/entry.png`, so the two graded runs write
byte-identical output.

Run locally:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

Two runs write the same bytes: the program only copies the shipped
image, so the output is deterministic by construction.

## License

MIT — see `LICENSE`.
