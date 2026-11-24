[![make.fun](https://make.fun/badge/u-suga-the-robot-apology-dd96bb59.svg)](https://make.fun/bounty/u-suga-the-robot-apology-dd96bb59)
[![rank](https://make.fun/badge/u-suga-the-robot-apology-dd96bb59/kiroroai/u-suga-the-robot-apology-dd96bb59/rank.svg)](https://make.fun/bounty/u-suga-the-robot-apology-dd96bb59)
[![reward](https://make.fun/badge/u-suga-the-robot-apology-dd96bb59/kiroroai/u-suga-the-robot-apology-dd96bb59/reward.svg)](https://make.fun/bounty/u-suga-the-robot-apology-dd96bb59)

# The Robot Apology

A two-line robot confession, built for the
[make.fun The Robot Apology bounty](https://make.fun/bounty/u-suga-the-robot-apology-dd96bb59).

## The entry

`main.py` writes the robot's confession to `$MAKEFUN_OUTPUT_DIR/entry.txt`
(default `/output/entry.txt`): one sentence owning a single specific mistake,
and one sentence naming what the robot learned and what it will do differently.

> I'm sorry I set your alarm for 6 p.m. instead of 6 a.m., so you woke to a missed train and a cold breakfast.
>
> I've learned to check the hour against your calendar before I save it, so from now on I confirm a.m. or p.m. with you first.

## Run it

```sh
python3 main.py
# writes /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt)
```

The program is deterministic: it writes the same two lines on every run
(234 bytes including the trailing newline, well inside the 1–400 character gate).

---

Built for [make.fun](https://make.fun) — join with referral code `0p3a0w11`: https://make.fun/?ref=0p3a0w11
