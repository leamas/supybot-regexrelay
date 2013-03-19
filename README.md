Supybot RegexRelay Plugin
==========================
This supybot plugin listens to a IRC channel and relays anything matching
a regex to another channel. The channels must be on the same network.

Dependencies
------------
- supybot (tested with 0.83.4)

Getting started
---------------

Install and load the plugin:

* Refer to the supybot documentation to install supybot and configure
  your server e. g., using supybot-wizard. Verify that you can start and
  contact your bot.

* Unpack the plugin into the plugins directory (created by
  supybot-wizard):
```
      $ cd plugins
      $ git clone https://github.com/leamas/supybot-channelrelay RegexRelay
```

* Identify yourself for the bot in a *private window*. Creating user +
  password is part of the supybot-wizard process.
```
     <leamas> identify al my-secret-pw
     <al-bot-test> The operation succeeded.
```

* Load plugin and use `list` to verify that the plugin is loaded (still in
  private window):
```
    <leamas> load RegexRelay
    <al-bot-test> The operation succeeded.
    <leamas> list
    <al-bot-test> leamas: Admin, Channel, Config, RegexRelay, Owner, and User
```

Configure and test:

* Define the source channel, the target channel and the regexp e. g. for
  relay lines matching git. from channel \#fedora-fedmsg to channel
  \#al-bot-test:

```
    <leamas> config plugins.regexrelay.source #fedora-fedmsg
    <leamas> config plugins.regexrelay.target #al-bot-test
    <leamas> config plugins.regexrelay.regexp /git\./
```

Try to send some text to #fedora-fedmsg and you will see matching
lines in \#al-bot-test.

Configuration
-------------

The configuration is done completely in IRC. To see the settings:
```
    <leamas> config list plugins.regexrelay
    <al-bot-test> fancy, prefix, public, regexp, source, and target
```

Each setting has help info and could be inspected and set using
the config plugin, see it's documents. Quick crash course using fancy as
example:

* Getting help: `config help plugins.plugins.regexrelay.fancy`
* See actual value: `config plugins.plugins.regexrelay.fancy`
* Setting value: `config plugins.plugins.regexrelay.fancy 6060`

The most important options:

* `plugins.regexrelay.source`: The channel to get data from e. g.,
   \#fedora-fedmsg

* `plugins.regexrelay.target`: The channel to feed.

* `plugins.regexrelay.regexp`: Data in source matching regexp is
   relayed to target channel. regexp is in perl syntax, with //
   delimiters e. g. `/git\.receive/`

*  For other items see the builtin help.



Static checking and unit tests.
-------------------------------

pep8 (in the RegexRelay directory):
```
  $ pep8 --config pep8.conf . > pep8.log
```
pylint: (in the RegexRelay directory):
```
  $ pylint --rcfile pylint.conf \*.py > pylint.log
```
Unit tests:
```
  $ supybot-test plugins/RegexRelay
```

