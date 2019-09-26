# Joker 🎤

Now you can generate jokes* in the style of your favorite comedian!

### Usage

#### Generating the models

First, you need to acquire transcripts from your chosen comedian. I recommend getting them from scrapsfromtheloft.com. Download a bunch and put them in single directory.

For example:
```
├── README.md
├── data
│   ├── hedberg,\ mitch
│   │   └── 1999_comedy_central_special.txt
│   ├── jeselnik,\ anthony
│   │   ├── 2013_caligula.txt
│   │   ├── 2015_thoughts_and_prayers.txt
│   │   └── 2019_fire_in_the_maternity_ward.txt
│   ├── mulaney,\ john
│   │   ├── 2012_new_in_town.txt
│   │   ├── 2015_comeback_kid.txt
│   │   ├── 2018_kid_gorgeous.txt
│   │   └── 2018_snl.txt
│   ├── regan,\ brian
│   │   ├── 2007_standing_up.txt
│   │   └── 2017_nunchucks_and_flamethrowers.txt
├── generate.py
└── joke.py
```

With that, you need to generate the markov chains. This is done with
```
$> ./generate.py <path/to/directory> <outfile>
```

For example:

```
./generate.py data/regan,\ brian/ brian_regan
```

This will create a model named `brian_regan` and put it in a folder `models`. You will end up with a folder like this:

```
models
├── brian_regan
├── doug_stanhope
├── john_mulaney
└── mitch_hedberg
```

#### Generating jokes

Now that these are all generated, you can run the models! To do this:

```
$ ./joke.py <path/to/model> <number-of-words>
```

For example:
```
$> ./joke.py models/john_mulaney 4
And if you went to school, cause that ’s my wife!
I am very small.
He got feminine hips!
She was in Connecticut recently, and I was younger, Oh, me?
$>
```

*not necessarily funny.
