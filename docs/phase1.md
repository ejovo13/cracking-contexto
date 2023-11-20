# Data Collection

For reasons that will be explained later, datasets will only be collected after game 427.

Starting from game 427, (at least) two modifications were made to contexto's dictionary. Firstly, the lemma[^1] of "sharpies" was changed from "sharpies" to "sharpie". Something else happened with the word "sunglass" but I'm not able to reproduce what changed.

Nevertheless, [here's](https://github.com/ejovo13/cracking-contexto/blob/main/data/rankings/rankings_all.csv) a csv file for days 427-430

```
         word  day_427  day_428  day_429  day_430
0          aa     5739    18459     7253    16595
1         aaa     8137    11759     6307     8406
2         aah    24927    28650    40725    38940
3        aahs    43739    43141    55117    58449
4         aal    34812    30636    61011    46156
...       ...      ...      ...      ...      ...
53797    zulu    12503    11317    21831    41775
53798    zuni    23117    16465    25057    53228
53799  zurich     6728    18185     7723    41771
53800  zydeco    15068    32115    37231    66251
53801  zygote    59413    48176    51316    46670
```

[^1]: The stem of our word. For example, "eat", "eating", and "ate" all map to the lemma "eat".