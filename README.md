# json-inspect

A command-line tool for inspecting and working with JSON files. Current sub-commands supported include

* `histo`

Each sub-command provides an individual utility for inspecting JSON files and each is documented separately
below.

## Instsallation

The utility comes as a single Python script. It can be installed simply as

```sh
mkdir -p $HOME/bin
curl -O $HOME/bin/json-inspect https://raw.githubusercontent.com/JohnMurray/json-inspect/master/json-inspect
chmod 0755 $HOME/bin/json-inspect
```

Also ensure that the path `$HOME/bin` is on your `$PATH`. If you are using bash, then you can run

```sh
echo 'PATH=$HOME/bin:$PATH' >> $HOME/.bashrc
```

## Sub-Commands

Each sub-command has it's own help file and options and serves different purposes. Please be sure to read the
docs for each command as it may not work like the others.

### histo

TODO: write this part.. haha
