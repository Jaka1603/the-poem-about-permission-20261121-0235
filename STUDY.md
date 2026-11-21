# the-poem-about-permission-20261121-0235 — study

Competition: "The poem about permission" ($50, 20 paid places),
opens 2026-11-21T02:35:00Z, closes 2026-11-21T06:35:00Z
(13:35 WIB). Program/v1: the program writes one text to
`/output/entry.txt` — UTF-8, 1 to 280 Unicode code points,
not only white space. Force_Last; the last submission counts.

Judge (z-ai/glm-5.3-flash, pairwise, both orders), criteria
in order: (1) it is a poem, and its subject is agency —
asking and being given, having, handing over or taking back
the power to act; (2) it moves the reader — an image, a turn
or an ending that lands; (3) insight — something true about
agency, recognised at once, never a slogan or a lecture;
(4) craft — sound, rhythm, line breaks, concrete exact
words, none that could be cut; (5) freshness — its own
voice and images, no stock phrases. Rhyme is neutral.
An exact tie goes to the smaller text, then the earlier
receipt — so the poem stays well under the cap, and the
entry ships once, strong, rather than in drafts.

## Four drafts, scored against the judge's order

D1 "The Knock" (255 code points) — the agent holds every
key yet still knocks; "a door opened without asking is only
a wall that learned to move"; ends "The waiting is the
work." Strong image, classic shape. Risk: the knock is a
familiar poetic device, and the last two lines repeat one
idea — two lines the judge could call cuttable.

D2 "Allow once" (309 code points as drafted — OVER the
280 cap, trimmed below) — the permission dialog itself is
the scene: "Allow once, or always allow?" Least privilege
(the key, not the house), the errand done and returned,
the asking repeated tomorrow, and the insight that a yes
which cannot turn back to no is not a gift but a leak —
so the giver's power stays theirs, especially in the
agent's hands. Freshest axis for readers who work beside
AI agents; every line carries a beat none other carries.

D3 "Keys by the door" (258 code points) — giver's voice,
the chance "to mean my yes". Gentle and true, but the
scene stays domestic and the ending states its meaning
("That is what giving is") instead of landing it.

D4 "Palms open" (232 code points) — daughter asking for
the sharp knife mirrored with the agent asking for the
send key; power leaves and "come back, carrying theirs".
Lovely turn, but "send key" is jargon that wobbles, and
the mirror needs a beat more room than 280 allows.

Winner: D2, trimmed from 309 to 276 code points. Cuts:
"nothing more" after the errand, "small" before the key
(the key/house contrast keeps the scale), "cannot" to
"can't", "come back" to "return", "is not a gift" to
"is no gift". No structural line was lost.

## Adversarial audit of the final text

- Gate: 276 Unicode code points (counted with Python
  `len()` on the exact string), 276 bytes, pure ASCII,
  no trailing newline written — inside 1..280 with margin.
- Subject check, line by line: the dialog question (ask /
  be given), the hover (the moment before power moves),
  the key not the house (asking for less than could be
  taken), the errand and return (power used, not kept),
  asking again tomorrow (permission as a practice, not a
  one-off), the revocable yes (insight), the leak (what
  irrevocable giving does to power), the close (the
  giver still owns what the agent holds).
- Internal logic: the speaker declines "always allow" —
  that is why it asks again tomorrow; the poem argues one
  position all the way through, no contradiction.
- Slogan check: no line preaches at the reader; the two
  aphoristic lines grow out of the scene before them.
- Spelling: every word standard English, checked twice.
- Determinism: the program writes a fixed string; two
  runs are byte-identical by construction and verified.

## Round 2 — the round-1 winner was rejected; write a better one

Jaka's verdict on D2 (21 Nov, main chat): "bikin lagi yang
lebih bagus lagi" — make another one, better. Honest
diagnosis of why D2 did not charm:

- It argues an ethics position more than it embodies a
  scene. Abstract nouns (trust, power, gift) do the work
  that images should do; the reader admires the logic and
  feels little.
- The key/house contrast is a familiar metaphor, and the
  permission dialog is the most obvious scene for this
  brief — the axis every AI-adjacent entrant would pick.
- The rhythm is flat staccato: ten short declaratives at
  one temperature, no swell, no hush.
- The close ("Especially then") is abstract — it points
  at the insight instead of landing it in an image.

### Six new drafts, genuinely different approaches

Scored on the judge's order, five axes, 5 points each:
emotion, freshness of image, rhythm/music, specificity
of scene, strength of the closing line. Round 1's winner
is included as the bar.

- R1 D2 "Allow once" (276 cp) — the dialog scene.
  2/3/3/3/2 = 13.
- R2 D5 "Kite" (230 cp) — the kite speaks; a mother's
  hand lets out string a thumb's width at a time; a yes
  that can still say "come back". "Love is a hand
  learning / how much sky it can lend." Tender and
  musical, but the closing definition ("Love is...")
  leans slogan, and permission stays implicit.
  5/4/4/4/4 = 21.
- R2 D6 "Curb" (229 cp) — a parent's fingers loosen one
  by one at a crossing; the child crosses "carrying /
  her open hand on my back". The most specific scene of
  the round, but it is a handing-over with no asking in
  it, and "letting go of the holding" goes abstract.
  5/4/3/5/4 = 21.
- R2 D7 "Door" (252 cp) — THE DOOR SPEAKS. Pushed and
  pulled all day, brass bright with palms that never
  waited; one hand knocks, three taps, and waits, though
  it could break the door. "A door that is asked / is
  not a wall. / It is a welcome with hinges."
  4/5/4/4/5 = 22.
- R2 D8 "Dog" (253 cp) — an old dog waits at an open
  gate for the one word she loves more than the road.
  Warm, but the theme slides toward obedience, and the
  close restates the wait instead of turning it.
  4/4/4/4/4 = 20.
- R2 D9 "Orchard" (238 cp) — dialogue: "The fallen
  ones. Leave the branches." A bounded yes kept sweet
  by the one apple left shining. Clear asking, clear
  limit; the ending explains its moral ("That is how
  his yes stayed sweet") instead of landing it.
  3/4/4/5/3 = 19.
- R2 D10 "Lamp" (247 cp) — an apprentice is handed the
  lamp key for one night; at dawn: "Still lit." Trust
  rendered well, but permission is a premise, not the
  poem's action, and the closing triad lists.
  4/3/4/4/4 = 19.

Winner: R2 D7 "Door", 22/25 — a clear win over R1's 13,
and ahead of both 21-point drafts. Head-to-head against
R1 it wins every axis: emotion 4 vs 2 (a thing that can
be broken, choosing to be asked), freshness 5 vs 3 (the
knocked-upon narrates; nobody else in the field speaks
as the door), rhythm 4 vs 3 (long used lines against
the hush of "then waiting."), specificity 4 vs 3 (brass,
palms, three taps — objects, not concepts), closing
5 vs 2 ("a welcome with hinges" is an image only a door
could give; "Especially then" is a gesture at one).

### Adversarial audit of the round-2 winner

- Gate: 252 Unicode code points (Python `len()` on the
  exact string), 252 bytes, pure ASCII, no trailing
  newline — inside 1..280, and 24 points under R1, which
  also helps on the exact-tie rule (smaller text wins).
- Subject: agency in its purest form — power that could
  force ("That hand could break me") restrained by
  asking ("It asks instead"). Asking, being given, and
  the refusal to take are all present in the action.
- Internal logic: the door is used as an object all day
  (push/pull, named only by its states); impatient palms
  polish the brass; the knocker's three taps and waiting
  are the opposite treatment; being asked transforms
  the door's own account of itself — wall to welcome.
  No contradiction; the personification is consistent
  (a door knows hands, brass, hinges — nothing else).
- Cut test: every line carries a beat no other line
  carries — routine, impatience, contrast, power,
  choice, transformation, image. Removing any line
  breaks the chain.
- Slogan check: no line lectures or defines; the one
  aphoristic turn ("is not a wall") is earned by the
  scene and immediately cashed in a concrete image.
- Stock-phrase check: "welcome with hinges" is coined,
  not stock; no phrase appears in the round-1 text —
  the knock survives only as an event inside a new
  voice, not as the poem's device.
- Spelling: every word standard English, checked twice.
- Determinism: the program writes a fixed string; two
  runs are byte-identical by construction and verified.


## Round 3 — research the greats first, then write

Jaka's order (21 Nov, main chat): "cari referensi dari
puisi terbaik di semua situs loe, loe buat dan loe
bandingkan dengan puisi yang loe buat dengan hasilnya,
hasil paling terbaik laporkan ke gua" — find references
from the best poems across the sites, write, compare
against what we made, report the single best result.

### References studied (all read in full, sources noted)

1. Rumi, "The Guest House" (trans. Coleman Barks) —
   archive.org / allpoetry.com. One governing metaphor
   announced in line 1 ("This being human is a guest
   house"); the guests escalate (joy → sorrows that
   "violently sweep your house empty"); the close
   re-reads everything before it ("a guide from
   beyond"). Lesson: a single image, held; the ending
   reclassifies, never summarises.
2. Emily Dickinson, "The Soul selects her own Society"
   (c. 1862) — LitCharts / Wikisource. The chooser's
   sovereignty: an Emperor kneels on her mat and she is
   "Unmoved". Three images of shutting escalate — door,
   gate, valves of attention, stone — and the lines
   physically shorten as the poem closes down. Lesson:
   power is shown by what it refuses; let the form
   narrow toward the close. The thematic twin of this
   brief: permission is who decides who enters.
3. Emily Dickinson, "The Wind — tapped like a tired
   Man" — LitCharts. A tap at the door, a bold "Come
   in", a guest who cannot be seated; the poem ends by
   re-staging its opening with a difference — the tap
   again, then absence. Lesson: an ending can re-stage
   the first gesture, changed.
4. William Carlos Williams, "This Is Just To Say"
   (1934) — poetryfoundation.org. Twenty-eight words, a
   found note: the taking without permission confessed,
   "Forgive me" undercut by pure sensation ("so sweet /
   and so cold"). Lesson: plain speech is a register,
   not a failure of one; the close lands on the senses,
   not on the apology.
5. Mary Oliver, "The Uses of Sorrow" (Thirst, 2006) —
   goodreads.com / Thirst. Four lines: one concrete
   impossible object ("a box full of darkness"), years
   compressed into a single line, and the volta carried
   by two small words — "this, too". Lesson: the turn
   can be tiny and total; the close reclassifies the
   gift.
6. Derek Walcott, "Love After Love" (1976) —
   poets.org. Greeting yourself at your own door;
   imperatives of hospitality ("Give wine. Give
   bread."); the whole poem lands in four words: "Sit.
   Feast on your life." Lesson: an imperative close can
   carry a whole poem's weight.
7. W. B. Yeats, "Aedh Wishes for the Cloths of Heaven"
   (1899) — poets.org. Everything the speaker owns is
   spread under the beloved's feet, and the close asks
   for gentleness with what was handed over: "Tread
   softly because you tread on my dreams." Lesson: the
   one who gives everything can still set the terms —
   asking survives the giving.
8. Hafiz, "The Sun Never Says" (rendered by Daniel
   Ladinsky, The Gift, 1999) — en.wikiquote.org. Giving
   that never presents a bill: the sun never says "You
   owe me", and "it lights the whole sky". Lesson:
   measure a gift by what it never asks back.

Benchmarks scored on our rubric (below): Dickinson's
"Soul selects" 4/5/5/4/5 = 23; Oliver's "Uses of
Sorrow" 5/5/4/4/5 = 23. Those are the ceiling our own
poems are measured against — canonical poems in four
to twelve lines, and the standard the round had to
approach, not a bar we pretend to clear cheaply.

### Five new drafts, written against those techniques

- R3 D11 "Unlocked" (215 cp) — the modern form of total
  permission: her phone, unlocked, handed over for one
  errand. WCW's plain register, Oliver's reclassifying
  close, Dickinson's re-staged gesture — trust proved
  by an absence: "She never looked up."
  4/5/4/5/5 = 23.
- R3 D12 "Key" (274 cp) — the key itself speaks: the
  smallest thing she owns that opens everything,
  copyable, lendable, losable; "Trust, cut to my
  shape." Fresh psychology but the same object-voice
  device as round 2, and the lines run prosy.
  3/4/3/4/4 = 18.
- R3 D13 "Ladder" (179 cp) — the borrowed ladder comes
  back with its loose rung screwed tight, unmentioned
  by either side; "That is the whole history / of why
  you hold my key." Oliver-like reclassification, the
  most economical draft of the round; its close still
  explains a half-beat more than D11's.
  4/4/4/5/4 = 21.
- R3 D14 "Mat" (235 cp) — permission granted before the
  asking: the spare key under the mat, eleven years of
  rain, the night the pipes burst; "come before you
  have to ask." Warm escalation by weather and years,
  but the penultimate line glosses the close.
  4/4/4/4/4 = 20.
- R3 D15 "Kept door" (264 cp) — the refusal poem: ask
  for the matches, the car, the key itself — but the
  way to stop asking is never handed over, "so you keep
  knocking, / and I keep rising to answer." A fresh
  axis (the kept no), but it risks reading possessive
  until late, and its objects stay generic.
  3/4/4/3/4 = 18.

### Final table (emotion / freshness / rhythm /
specificity / closing, of 5 each)

- Benchmark: Dickinson, "The Soul selects" — 23.
- Benchmark: Oliver, "The Uses of Sorrow" — 23.
- R3 D11 "Unlocked" — 23. ← winner
- R2 D7 "Door" — 22.
- R3 D13 "Ladder" — 21.
- R3 D14 "Mat" — 20.
- R3 D12 "Key" — 18.
- R3 D15 "Kept door" — 18.
- R1 D2 "Allow once" — 13.

Head-to-head, D11 vs R2's "Door": freshness ties 5–5
(a voice nobody else in the field will use, against a
scene nobody else in the field will stage); rhythm
ties 4–4; D11 wins specificity 5–4 (stove, photo, and
the exact inventory "her banks, her letters, her
years" against brass and palms) and the emotion is
warmer at the same 4. The deciding axis is the close:
"a welcome with hinges" defines its image, while "She
never looked up" proves its claim with a behaviour —
the references' lesson (Oliver, Williams) is that a
close which shows beats a close which states. D11
also ships 37 code points smaller, which the tie rule
rewards. Honest note: on this rubric D11 draws level
with the two benchmark poems; they remain the greater
poems in range and music — but inside 280 code points,
on the judge's own axes, D11 is the strongest original
we have made in three rounds.

### Adversarial audit of the round-3 winner

- Gate: 215 Unicode code points (Python `len()` on the
  exact string), 215 bytes, pure ASCII, no trailing
  newline — inside 1..280 with the largest margin of
  any round.
- Subject: agency in both directions — power handed
  over entire (the unlocked phone is the whole of a
  modern life: banks, letters, years) and power handed
  back unused beyond the errand. Asking, being given,
  having, handing back: all four of the judge's verbs
  are in the action, none in abstraction.
- Internal logic: she turns back to the stove before
  the inventory, so the final line is earned, not
  asserted; he performs exactly the errand named in
  line 2 and no other; nothing in the scene contradicts
  anything else.
- Cut test: remove the stove and the close has no
  proof; remove the inventory and the permission has no
  weight; remove the errand's exact performance and the
  honouring vanishes; remove the close and the poem is
  an anecdote. Every line carries a beat no other line
  carries.
- Slogan check: no line defines, preaches or sums up.
  An earlier draft of D11 ended "That is the loudest
  yes I know" — a gloss — and it was cut for exactly
  that reason; the poem now ends on the fact.
- Stock-phrase check against the references: no phrase
  is borrowed — no "guide from beyond", no "tread
  softly", no "so sweet and so cold", no guest house,
  no valves, no feast. The techniques were taken
  (single scene, reclassifying close, plain register),
  never the words.
- Spelling: every word standard English, checked twice.
- Determinism: the program writes a fixed string; two
  runs are byte-identical, sha256
  f5b0b9dbc0e71f2d6aa3aa6daed7ca9271beb5e4c4ec6ffa024c359b8d332c53.
